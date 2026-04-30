import os         
import sys        
import shutil     
import tempfile   
import re         
import json
import html
import subprocess
import threading
from turtle import reset
import requests
import pyttsx3    
from gtts import gTTS  
from tqdm import tqdm
GLOBAL_TTS_ENGINE = None
VOICE_RATE = 180
VOICE_LANG = "en" 
def init_tts_engine_once():
    """全局只初始化一次 TTS 引擎（内部用）"""
    global GLOBAL_TTS_ENGINE
    if GLOBAL_TTS_ENGINE is None:
        GLOBAL_TTS_ENGINE = pyttsx3.init()
        GLOBAL_TTS_ENGINE.setProperty('rate', VOICE_RATE)
        GLOBAL_TTS_ENGINE.setProperty('volume', 1.0)

# 程序启动时就初始化（一次就行）
init_tts_engine_once()




#基础配置
TARGET_URL = "https://base.bestsch.com/BschZncp2/front/index.html"

# 接口地址
ZUOYE_LIST_URL = "https://base.bestsch.com/BschZncp2/api/FindMyZuoye"
ZUOYE_DETAIL_URL = "https://base.bestsch.com/BschZncp2/api/FindUserZuoye2"
ANSWER_RECORD_URL = "https://base.bestsch.com/BschZncp2/api/findUserAnswerRecordAll"
SAVE_ANSWER_URL = "https://base.bestsch.com/BschZncp2/api/saveUserAnswerRecordNew"

# 禁用SSL警告
requests.packages.urllib3.disable_warnings()

# 语音配置
VOICE_RATE = 150  # 朗读语速
VOICE_LANG = 'en' 
#函数
def openwebsite():
    """打开Edge 浏览器并访问网站"""
    try:
        subprocess.Popen(f'start msedge {TARGET_URL}', shell=True)
    except Exception as e:
        print(f" 启动Edge失败：{str(e)}")


def fetch_zuoye_list(session):
    """获取所有作业列表"""
    all_zuoye = []
    page = 1
    page_size = 10
    total = 0
    print(f"{BLUE} 正在获取所有作业列表...{END} ")
    
    while True:
        params = {"page": page, "count": page_size}
        try:
            resp = session.get(ZUOYE_LIST_URL, params=params, headers=HEADERS, timeout=15, verify=False)
            result = resp.json()
            if result.get("code") != 0:
                print(f" {RED}第{page}页获取失败：{result.get('msg')}{END}")
                break
            data = result.get("data", {})
            total = data.get("total", 0)
            zuoye_list = data.get("content", [])
            if not zuoye_list:
                break
            all_zuoye.extend(zuoye_list)
            if page == 1:
                pbar = tqdm(total=total, desc=" 作业获取进度", colour="blue")
            # 更新进度条：每次增加当前页获取到的作业数量
            pbar.update(len(zuoye_list))
            print(f" {GREEN}第{page}页获取成功，当前累计：{len(all_zuoye)}/{total}条{END}")
            if len(all_zuoye) >= total:
                break
            page += 1
        except Exception as e:
            print(f" {RED}第{page}页请求异常：{str(e)}{END}")
            break
    if 'pbar' in locals():
        pbar.close()
    print(f"\n {BLUE}共获取到 {len(all_zuoye)} 条作业{END}")
    return all_zuoye

def extract_json_from_response(text):
    """
    从可能包含非JSON内容的响应中提取并解析JSON对象。
    """
    if not text:
        return None
    text = text.strip()
    try:
        #  第一次尝试：直接按标准JSON解析
        return json.loads(text)
    except json.JSONDecodeError:
        pass
    # 智能提取：用正则表达式 查找 { ... } 格式的内容（强行找JSON）
    match = re.search(r'(\{.*\})', text, re.DOTALL)
    if match:
        # 拿到找到的 { ... } 字符串
        json_str = match.group(1)
        # 去掉最后一个多余逗号
        json_str = re.sub(r',\s*}', '}', json_str)
        json_str = re.sub(r',\s*]', ']', json_str)
        try:
            return json.loads(json_str)
        except json.JSONDecodeError as e:
            print(f" {RED} JSON二次解析失败: {e}{END}")
            error_pos = e.pos
            start = max(0, error_pos - 50)
            end = min(len(json_str), error_pos + 50)
            print(f"   {YELLOW}错误位置附近: ...{json_str[start:end]}...{END}")
    return None




def clean_text(text, base_url="https://base.bestsch.com"):
    """
    清理文本：将整个<img>标签替换为 '!' + 图片绝对URL + '!'，
    去除其他HTML标签，转换实体，合并空白。
    """
    if not text:
        return ""
    text = str(text)

    # 匹配整个<img>标签并提取src，替换为 !URL!
    def img_replacer(match):
        src = match.group(1)
        if src.startswith("http"):
            full_url = src
        else:
            if not src.startswith("/"):
                src = "/" + src
            full_url = base_url + src
        return f"!{full_url}!"  # 用 ! 包裹图片URL

    text = re.sub(r'<img\s+[^>]*src="([^">]+)"[^>]*>', img_replacer, text)
    text = re.sub(r"<[^>]+>", "", text)
    text = html.unescape(text)
    text = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f\x7f-\x9f]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text



def fix_json_text(raw_text):
    """
    修复不标准的JSON文本：去除可能的前缀/后缀，删除多余的逗号。
    """
    if not raw_text:
        return "{}"
    raw_text = raw_text.strip()
    match = re.search(r'(\{.*\})', raw_text, re.DOTALL)
    if match:
        raw_text = match.group(1)
    raw_text = re.sub(r',\s*}', '}', raw_text)
    raw_text = re.sub(r',\s*]', ']', raw_text)
    return raw_text




def extract_question_info(question_dict):
    """
    从单个题目对象中提取结构化信息，图片已嵌入到文本中。
    新增：识别单词朗读题，提取纯英文朗读文本
    """
    # 初始化一个空字典
    info = {
        "qid": "",                         # 新增：题目ID
        "title": "",
        "options": [],
        "correct_answer": "",
        "explanation": "",
        "media_urls": [],
        "type": "single_choice",           # 默认单选题，后续根据选项判断
        "is_word_reading": False,          # 新增：标记是否为单词朗读题
        "word_text": ""                    # 新增：纯英文朗读文本
    }

    # 题目ID
    info["qid"] = question_dict.get("id", "") or question_dict.get("zuoyeQestId", "")

    # 标题（含内联图片）
    title_html = question_dict.get("name", "")
    info["title"] = clean_text(title_html)

    # 新增：识别单词朗读题
    read_keywords = ["单词朗读", "朗读", "read aloud", "pronounce"]
    if any(keyword in info["title"] or keyword in str(question_dict) for keyword in read_keywords):
        info["is_word_reading"] = True
        # 过滤中文，只保留英文单词/短语（如“基于 based on”→“based on”）
        info["word_text"] = re.sub(r'[\u4e00-\u9fa5]', '', info["title"]).strip()

    # 选项提取：从config字段解析
    config_str = question_dict.get("config", "{}")
    if config_str and config_str != "{}":
        try:
            fixed_config = fix_json_text(config_str)
            config = json.loads(fixed_config)
            opt_list = config.get("options", [])
            for opt_html in opt_list:
                info["options"].append(clean_text(opt_html))

            # 判断题型
            if not info["options"]:
                info["type"] = "fill_blank"
            elif len(info["options"]) > 4:
                info["type"] = "multiple_choice"
            else:
                info["type"] = "single_choice"

        except Exception as e:
            print(f"{RED} 从config解析选项失败: {e}{END}")
            alt_opts = question_dict.get("options") or question_dict.get("optionList")
            if alt_opts:
                for opt_html in alt_opts:
                    info["options"].append(clean_text(opt_html))
                info["type"] = "single_choice" if len(info["options"]) <= 4 else "multiple_choice"
            else:
                info["type"] = "fill_blank"

    # 正确答案
    raw_answer = question_dict.get("answer", "")
    answer_clean = clean_text(raw_answer).strip("[]")
    try:
        answer_idx = int(answer_clean)
        option_labels = ["A", "B", "C", "D", "E", "F"]
        info["correct_answer"] = option_labels[answer_idx] if answer_idx < len(option_labels) else raw_answer
    except:
        info["correct_answer"] = raw_answer

    # 解析（含内联图片）
    explanation_html = question_dict.get("solve", "")
    info["explanation"] = clean_text(explanation_html)

    # 媒体文件（音频、视频等）
    for file_obj in question_dict.get("zuoyeQuestionFiles", []):
        web_path = file_obj.get("webPath")
        if web_path:
            if not web_path.startswith("/"):
                web_path = "/" + web_path
            info["media_urls"].append("https://base.bestsch.com" + web_path)

    media_path = question_dict.get("webPath")
    if media_path:
        if media_path.startswith("http"):
            full_media_url = media_path
        else:
            if not media_path.startswith("/"):
                media_path = "/" + media_path
            full_media_url = "https://base.bestsch.com" + media_path
        info["media_urls"].append(full_media_url)

    info["media_urls"] = list(set(info["media_urls"]))
    return info




def fetch_zuoye_detail(session, zuoye_id, user_zuoye_id):
    """请求作业详情接口，返回题目列表"""
    print(f"\n{YELLOW}正在请求作业详情 | zuoyeId={zuoye_id} | userZuoyeId={user_zuoye_id}{END}")
    params = {"zuoyeId": zuoye_id, "userZuoyeId": user_zuoye_id}
    try:
        resp = session.get(ZUOYE_DETAIL_URL, params=params, headers=HEADERS, timeout=30, verify=False)
        data = extract_json_from_response(resp.text)
        if data is None:
            print(f"{RED} 无法从响应中提取JSON{END}")
            return []
        if data.get("code") != 0:
            print(f"{RED} 作业详情请求失败：{data.get('msg', '未知错误')}{END}")
            return []
        q_list = data.get("data", {}).get("zuoyeQestionList", [])
        if not q_list:
            q_list = data.get("data", {}).get("zuoyeQuestions", [])
        # 先保存原始题目列表
        global raw_q_list
        raw_q_list= q_list

        questions = []
        for q in q_list:
            questions.append(extract_question_info(q))
        return questions
    except Exception as e:
        print(f"{RED} 作业详情请求异常：{str(e)}{END}")
        return []



def print_question(q_info, idx, show_user_info=False):
    """
    格式化打印一道题目，图片URL已内联在文本中。
    """
    CYAN    = "\033[38;5;14m"  
    type_map = {
        "single_choice": "【单选题】",
        "multiple_choice": "【多选题】",
        "fill_blank": "【填空题】"
    }
    print(f"{YELLOW}第{idx}题【ID:{q_info['qid']}】{type_map.get(q_info['type'], '')}:{END}")
    print(f"{PURPLE}  {q_info['title']}{END}")

    if q_info["media_urls"]:
        print(f"{YELLOW}【媒体链接（音频/视频等）】{END}")
        for url in q_info["media_urls"]:
            print(f"{YELLOW}    {url}{END}")

    if q_info["options"]:
        for opt_idx, opt_text in enumerate(q_info["options"]):
            opt_label = chr(ord('A') + opt_idx)
            print(f"{CYAN}  {opt_label}. {opt_text}{END}")

    if q_info["correct_answer"]:
        print(f"{GREEN}  正确答案：{q_info['correct_answer']}{END}")

    if q_info["explanation"]:
        print(f"{YELLOW}  【解析】{q_info['explanation']}{END}")

    if show_user_info:
        if "user_answer" in q_info:
            print(f"{YELLOW}   用户答案：{q_info['user_answer']}  得分：{q_info.get('score', 'N/A')}{END}")

    print(f"{BLUE}{'-' * 80}{END}")



def fetch_answer_record(session, user_zuoye_id):
    """请求答题记录接口，返回带用户答案的题目列表"""
    print(f"\n{YELLOW}正在请求答题记录 | userZuoyeId={user_zuoye_id}{END}")
    params = {"userZuoyeId": user_zuoye_id}
    try:
        resp = session.get(ANSWER_RECORD_URL, params=params, headers=HEADERS, timeout=30, verify=False)
        data = resp.json()
        if data.get("code") != 0:
            print(f"{RED} 答题记录请求失败：{data.get('msg', '未知错误')}{END}")
            return []
        record_list = data.get("data", [])
        questions = []
        for item in record_list:
            q_dict = item.get("userAnswer", {}).get("zuoyeQestion", {})
            if q_dict:
                info = extract_question_info(q_dict)
                user_ans = item.get("userAnswer", {}).get("answer", "")
                score = item.get("userAnswer", {}).get("fenshu", "")
                info["user_answer"] = user_ans
                info["score"] = score
                questions.append(info)
        return questions
    except Exception as e:
        print(f"{RED} 答题记录请求异常：{str(e)}{END}")
        return []





def text_to_speech_audio(text, lang=VOICE_LANG):
    """
    【离线版】将文本转为音频文件，解决文件占用问题
    :param text: 要朗读的文本
    :param lang: 语言（en/zh-CN）
    :return: 临时音频文件路径
    """
    if not text:
        raise ValueError("朗读文本不能为空")
    
    # 初始化临时目录（系统自动清理）
    temp_folder = "temp_audio"
    os.makedirs(temp_folder, exist_ok=True)
    # 创建唯一临时音频文件
    unique_name = f"tts_{os.urandom(4).hex()}.wav"  # 随机8位字符
    temp_path = os.path.join(temp_folder, unique_name)
    
    
    def generate():
        # 关键：使用全局引擎，不重复创建、关闭
        engine = GLOBAL_TTS_ENGINE

        # 直接生成音频
        engine.save_to_file(text, temp_path)
        engine.runAndWait()

    
    t = threading.Thread(target=generate, daemon=True)
    t.start()
    t.join()  # 等待音频生成完成再退出函数
    #  返回最终生成好的音频路径（temp_audio/xxx.wav）
    print(f"{GREEN} 音频生成完成：{temp_path}{END}")
    return temp_path





def submit_audio_answer(session, user_zuoye_id, zuoye_qest_id, audio_path):
    """
    提交音频答案（适配wav格式）
    """
    if not os.path.exists(audio_path):
        return {"success": False, "msg": "音频文件不存在"}
    file_obj = None  # 文件句柄，用于手动关闭，解决占用
    try:
        file_obj = open(audio_path, 'rb')
        # 构造文件上传表单（修改content-type为wav）
        files = {
            "file": (os.path.basename(audio_path), file_obj, "audio/wav")
        }
        data = {
            "userZuoyeId": user_zuoye_id,
            "zuoyeQestId": zuoye_qest_id,
            "answerType": "2",  
            "answer": ""        
        }
        
        # 提交音频（自动处理multipart/form-data）
        resp = session.post(
            SAVE_ANSWER_URL,
            data=data,
            files=files,
            timeout=30,
            verify=False
        )
        
        result = extract_json_from_response(resp.text)
        if result and result.get("code") == 0:
            return {"success": True, "msg": "音频答案提交成功"}
        else:
            err_msg = result.get("msg", "接口异常") if result else f"响应：{resp.text[:200]}"
            return {"success": False, "msg": err_msg}
    except Exception as e:
        return {"success": False, "msg": f"音频提交异常：{str(e)}"}
    finally:
        try:
            if file_obj:  # 如果文件打开过，就关闭
                file_obj.close()
        except:
            pass

        # 提交后立即删除临时音频文件
        if os.path.exists(audio_path):
            try:
                os.remove(audio_path)
                print(f"{GREEN} 已删除临时音频文件：{audio_path}{END}")
            except:
                # 删除失败也不报错，不影响主流程
                pass






def save_user_answer(session, user_zuoye_id, zuoye_qest_id, answer_content):
    """提交单个题目的文本答案"""
    try:
        data = {
            "userZuoyeId": user_zuoye_id,
            "zuoyeQestId": zuoye_qest_id,
            "answer": answer_content
        }
        resp = session.post(
            SAVE_ANSWER_URL,
            data=data,
            headers=HEADERS,
            timeout=20,
            verify=False
        )
        result = extract_json_from_response(resp.text)
        if result and result.get("code") == 0:
            return {"success": True, "msg": "提交成功"}
        else:
            err_msg = result.get("msg", "接口异常") if result else "解析失败"
            return {"success": False, "msg": err_msg}
    except Exception as e:
        return {"success": False, "msg": f"请求异常：{str(e)}"}







def format_fill_blank_answer(user_input):
    """
    将填空题答案中的比较符号替换为图片标签，并包装成 JSON 数组格式。
    """
    mapping = {
        "<=": '<img class="formula" src="https://math.jianshu.com/math?formula=%5Cleq" data-latex="\\\\leq">',
        ">=": '<img class="formula" src="https://math.jianshu.com/math?formula=%5Cgeq" data-latex="\\\\geq">',
        "<": '<img class="formula" src="https://math.jianshu.com/math?formula=%3C" data-latex="&lt;">',
        ">": '<img class="formula" src="https://math.jianshu.com/math?formula=%3E" data-latex="&gt;">'
    }
    pattern = re.compile('|'.join(re.escape(k) for k in sorted(mapping.keys(), key=len, reverse=True)))
    replaced = pattern.sub(lambda m: mapping[m.group(0)], user_input)
    return json.dumps([replaced], ensure_ascii=False)





def print_original_english_word(raw_question_list):
    """从原始题目对象提取 name 字段英文单词并打印"""
    print("\n===== 提取英文单词 =====")
    for item in raw_question_list:
        word = item.get("name", "").strip()
        if word:
            print(word)

def show_english_words(questions):
    print("\n===== 提取英文单词 =====")
    for q in questions:
        word = q.get("name", "").strip()
        if word:
            print(word)







def submit_raw_word_answer(session, user_zuoye_id, zuoye_qest_id, word_text):
    """直接提交原英文单词作为答案，不翻译"""
    try:
        data = {
            "userZuoyeId": user_zuoye_id,
            "zuoyeQestId": zuoye_qest_id,
            "answer": word_text
        }
        resp = session.post(
            SAVE_ANSWER_URL,
            data=data,
            headers=HEADERS,
            timeout=20,
            verify=False
        )
        result = extract_json_from_response(resp.text)
        if result and result.get("code") == 0:
            return {"success": True, "msg": "单词提交成功"}
        else:
            err_msg = result.get("msg", "接口异常") if result else "解析失败"
            return {"success": False, "msg": err_msg}
    except Exception as e:
        return {"success": False, "msg": f"请求异常：{str(e)}"}


def batch_submit_raw_word(session, user_zuoye_id, raw_question_list):
    """批量提取原题英文单词 → 直接原样提交"""
    print(f"\n{YELLOW}===== 开始批量提交原英文单词 ====={END}")
    submit_count = 0
    skip_count = 0

    for idx, item in enumerate(raw_question_list, 1):
        qid = item.get("id") or item.get("zuoyeQestId", "")
        # 提取原题name里的单词
        raw_title = item.get("name", "").strip()
        # 清理掉html、只留纯文本单词
        word_only = clean_text(raw_title)
        # 过滤掉中文，只保留英文
        word_only = re.sub(r'[\u4e00-\u9fa5]', '', word_only).strip()

        if not qid or not word_only:
            print(f"{YELLOW}第{idx}题：无ID或无有效英文单词，跳过{END}")
            skip_count += 1
            continue

        print(f"{YELLOW}第{idx}题 单词：{word_only}{END}")
        res = submit_raw_word_answer(session, user_zuoye_id, qid, word_only)
        if res["success"]:
            print(f"  {GREEN}✅ 提交成功{END}")
            submit_count += 1
        else:
            
            skip_count += 1
        print(f"{BLUE}{'-' * 60}{END}")

    print(f"\n{GREEN}批量提交完成：成功 {submit_count} 题 | 跳过 {skip_count} 题{END}")

def batch_submit_answers(session, user_zuoye_id, questions):
    """
    批量提交答案：
    1. 一次性确认整个作业是否为音频作业
    2. 音频题自动提取题目文本作为朗读内容
    """
    print(f"\n{YELLOW} 开始批量提交答案 | 共 {len(questions)} 道题目{END}")
    

    is_show_words = input(f"{YELLOW}是否提取英文单词？(y=是/回车=否)：{END}").strip().lower()
    if is_show_words == "y":
        #show_english_words(questions)
        if input(f"{YELLOW}是否直接提交原英文单词？(y/n): ").strip().lower() == "y":
                batch_submit_raw_word(session, user_zuoye_id, raw_q_list)
        return

    is_audio_homework = input(f"{YELLOW}该作业是否为音频作业？(y=是/回车=否)：{END}").strip().lower()
    if is_audio_homework == "q":
        print(f"{PURPLE}退出提交流程{END}")
        return
    
    print(f"{BLUE}{'=' * 80}{END}")
    submit_count = 0
    skip_count = 0
    audio_submit_count = 0

    for idx, q in enumerate(questions, 1):
        if not q["qid"]:
            print(f"{YELLOW}第{idx}题：无ID，跳过{END}")
            skip_count += 1
            continue

        print(f"{YELLOW}【待提交】第{idx}题【{q['type']}】：{q['title'][:60]}...{END}")
        
        if is_audio_homework == "y":
            read_text = re.sub(r'![^!]+!', '', q["title"]).strip()
            if not read_text:
                print(f"{RED}  题目无有效文本，跳过{END}")
                skip_count += 1
                continue
            
            try:
                audio_path = text_to_speech_audio(read_text)
                res = submit_audio_answer(session, user_zuoye_id, q["qid"], audio_path)
                if res["success"]:
                    print(f"  ✅ 音频答案提交成功（朗读文本：{read_text[:30]}...）")
                    submit_count += 1
                    audio_submit_count += 1
                else:
                    skip_count += 1
            except Exception as e:
                skip_count += 1
            print(f"{BLUE}{'-' * 60}{END}")
            continue

        if q["type"] == "fill_blank":
            print(f"  {YELLOW}填空题，请直接输入答案{END}")
            ans = input(f"  {GREEN}第{idx}题答案：{END}").strip()
            if ans.lower() == "q":
                break
            if not ans:
                print("  跳过")
                skip_count += 1
                continue
            formatted_ans = format_fill_blank_answer(ans)
            res = save_user_answer(session, user_zuoye_id, q["qid"], formatted_ans)
            if res["success"]:
                print(f"  {GREEN} 提交成功{END}")
                submit_count += 1
            else:
                print(f"{RED} 失败：{res['msg']}{END}")
                skip_count += 1

        else:
            if not q["options"]:
                print("  无选项，跳过")
                skip_count += 1
                continue
            for i, opt in enumerate(q["options"]):
                print(f"  {chr(65+i)}. {opt[:50]}")
            ans = input(f"  {GREEN}请输入答案索引(0-{len(q['options'])-1}):{END}").strip()
            if ans.lower() == "q":
                break
            if not ans:
                print(f"  {YELLOW} 跳过{END}")
                skip_count += 1
                continue
            try:
                ans_idx = int(ans)
                answer_str = f"[{ans_idx}]"
                res = save_user_answer(session, user_zuoye_id, q["qid"], answer_str)
                if res["success"]:
                    print(f"  {GREEN} 提交成功{END}")
                    submit_count += 1
                else:
                    print(f"  {RED} 失败：{res['msg']}{END}")
                    skip_count += 1
            except:
                print(f"{RED} 输入无效，跳过{END}")
                skip_count += 1
        print(f"{BLUE}{'-' * 60}{END}")

    print(f"\n {GREEN}提交完成：成功 {submit_count} 题（其中音频 {audio_submit_count} 题）| 跳过 {skip_count} 题{END}")










#主程序
if __name__ == "__main__":
    # 设置控制台编码（Windows）
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
    # 颜色
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    PURPLE = "\033[95m"
    BOLD = "\033[1m"
    END = "\033[0m"

    os.system("cls" if os.name == "nt" else "clear")#清屏

    # 双层边框
    print(f"{BLUE}{BOLD}+" + "-" * 138 + "+")
    print(f"""
    {YELLOW}{BOLD}
                        上海市进才中学北校 · 作业极速通关工具
    {END}""")

    print(f"{BLUE}{BOLD}+" + "-" * 138 + "+")

    print()
    print(f"{GREEN} 这是上海市进才中学北校 JB 作业极速通关工具(简易版），支持自动提交答案和语音朗读！摆烂党直接起飞 !(✪ω✪)")
    print(f"{PURPLE}  天才同学:sxy,shy,sxy,cxm,zxy,亮鱼")
    print(f"{PURPLE}  对了沈皓阳和石绪源不怕被打出来(留下沈皓阳和石绪源NB (*^▽^*) ){END}")
    print()
    print(f"{BLUE}  不想写 JB 作业？恭喜你找对地方了，直接开摆！")
    for t in range (1,3):
        print(f"{GREEN}  我爱进北！{END}")
    print()
    print(f"{RED}     免责声明：仅供学习交流整活玩，别乱来嗷！{END}")
    print(f"{RED}     出问题自己扛，{YELLOW} 我们 {RED}概不负责~ ┗( ▔, ▔ )┛{END}")
    print(f"{BLUE}{BOLD}+" + "-" * 138 + "+")
    print(END)
    print('登录作业网站')
    print('复制JSESSIONID值(F12开发者工具-应用程序-Cookie里找),不会的就用gui版,这里就不教了(*^▽^*)')
    while True:
        choice = input("打开学校网站？(y/n): ").strip().lower()
        if choice in ("y", "n"):
            break
        print("❌ 输入错误！只能输入 y 或 n\n")
    if choice == "y":
        openwebsite()

    # 3. 无论 y/n，都必须输入 JSESSIONID（不能为空）为了开发时偷点懒(*^▽^*) (✪ω✪)
    while True:
        JSESSIONID = input("\n请输入复制的JSESSIONID值: ").strip()
        if JSESSIONID:
            break
        print("❌ JSESSIONID 不能为空，请重新输入！")
    # 固定currentrole
    CURRENT_ROLE = "%7B%22childId%22:0,%22roleId%22:3,%22schId%22:865%7D"
    HEADERS = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-US;q=0.7",
        "bschapirequest": "1",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded",
        "currentrole": CURRENT_ROLE,
        "Host": "base.bestsch.com",
        "Pragma": "no-cache",
        "Referer": "https://base.bestsch.com/BschZncp2/front/index.html",
        "Sec-Ch-Ua": '"Not:A-Brand";v="99", "Google Chrome";v="145", "Chromium";v="145"',
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": '"Windows"',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36"
    }
    
    # 创建会话，设置Cookie
    session = requests.Session()
    session.verify = False
    session.timeout = 30
    session.cookies.set("JSESSIONID", JSESSIONID, domain="base.bestsch.com", path="/BschZncp2")
    session.cookies.set("currentrole", CURRENT_ROLE, domain="base.bestsch.com", path="/BschZncp2")
    
    # 1. 获取作业列表
    zuoye_list = fetch_zuoye_list(session)
    if not zuoye_list:
        print(f"{RED} 未获取到任何作业，退出。{END}")
        exit()
    
    # 2. 显示作业列表，供用户选择
    print()
    print(f"{BLUE}  {"-" * 80}{END}")
    print(f"{YELLOW}{BOLD}【作业列表】{END}")
    
    status_map = {0: "未提交", 3: "已完成", 1: "进行中", 2: "未订正"}
    for idx, zuoye in enumerate(zuoye_list, 1):
        name = zuoye.get('name', '未知')
        teacher = zuoye.get('cname', '未知')
        start = zuoye.get('startDate', '未知')
        end = zuoye.get('endDate', '未知')
        status_code = zuoye.get('isComplete')
        status = status_map.get(status_code, '未知')
        total_score = zuoye.get('totalScore', 0)
        is_complete = zuoye.get('isComplete')
        #status = status_map.get(is_complete, '未知')
        if status_code == 0:
        # 红色：未提交
            #status = f"\033[91m{status}\033[0m"
            text_color = RED
        elif status_code == 1:
            # 黄色：进行中
            #status = f"\033[93m{status}\033[0m"
            text_color = YELLOW
        elif status_code == 2:
            # 紫色：未订正
            #status = f"\033[94m{status}\033[0m"
            text_color = PURPLE
        elif status_code == 3:
            # 绿色：已完成
            #status = f"\033[92m{status}\033[0m"
            text_color = GREEN
        print(f"{text_color}{idx:2d}. {name} | 老师：{teacher}{END}")
        print(f"{text_color}    起止：{start} → {end}{END}")
        print(f"{text_color}    状态：{status} | 总分：{total_score}{END}")
        print(f"{BLUE}  {"-" * 80}{END}")
    
    # 3. 用户选择
    while True:
        choice = input("请输入要查看的作业序号（直接回车退出）：").strip()
        if not choice:
            print("退出程序。")
            exit()
        try:
            idx = int(choice) - 1
            if 0 <= idx < len(zuoye_list):
                selected = zuoye_list[idx]
                break
            else:
                print(f"{RED} 序号超出范围,请输入1~{len(zuoye_list)}之间的数字。{END}")
        except ValueError:
            print(f"{RED} 请输入有效数字。{END}")
    
    # 4. 提取 zuoyeId 和 userZuoyeId
    zuoye_id = selected.get("id")
    user_zuoyes = selected.get("userZuoyes", [])
    if user_zuoyes and isinstance(user_zuoyes, list) and len(user_zuoyes) > 0:
        user_zuoye_id = user_zuoyes[0].get("id")
    else:
        print(f"{YELLOW} 未从作业数据中自动解析出 userZuoyeId,请手动输入。{END}")
        user_zuoye_id = input("请输入 userZuoyeId:").strip()
        if not user_zuoye_id:
            print(f"{RED} userZuoyeId 不能为空，退出。{END}")
            exit()
    
    if not zuoye_id or not user_zuoye_id:
        print(f"{RED} 无法获取 zuoyeId 或 userZuoyeId,退出。{END}")
        exit()
    
    print(f"\n{GREEN}已选择作业：{selected.get('name')}{END}")
    print(f"   zuoyeId = {zuoye_id}, userZuoyeId = {user_zuoye_id}")
    
    # 5. 请求作业详情并打印
    detail_questions = fetch_zuoye_detail(session, zuoye_id, user_zuoye_id)
    if detail_questions:
        print()
        print(f"{BLUE} 作业中共 {len(detail_questions)} 道题目：{END}")
        print(f"{YELLOW}{"=" * 80}{END}")
        for i, q in enumerate(detail_questions, 1):
            print_question(q, i)
    else:
        print(f"{RED} 未从作业详情中获取到题目。{END}")
    
    # 6. 请求答题记录并打印
    record_questions = fetch_answer_record(session, user_zuoye_id)
    if record_questions:
        print(f"\n{YELLOW} 答题记录中共 {len(record_questions)} 道题目（含用户答案）：{END}")
        print(f"{BLUE}{"=" * 80}{END}")
        for i, q in enumerate(record_questions, 1):
            print_question(q, i, show_user_info=True)
    else:
        print(f"{RED} 未从答题记录中获取到题目。{END}")
    
    # 7. 询问是否提交答案（增强版，支持音频）
    if detail_questions:
        if input(f"{YELLOW}是否要提交答案?(y/n):{END}").lower() == "y":
            batch_submit_answers(session, user_zuoye_id, detail_questions)
    else:
        print(f"{RED} 没有题目可提交。{END}")
    
    print(f"\n{GREEN}操作完成!快给star,都看到这里了,订阅走起!!!!!!!!{END}")
    print(f"{GREEN}作者写到找这里是彻底把这个写完了，大家有兴趣看一下gui版，有ai帮写，图片，音频预览，快点去看{END}")
    print(f"{GREEN}最后祝大家作业快快完成，成绩棒棒哒！(*^▽^*)(*^▽^*)(*^▽^*)(*^▽^*){END}")
    print(f"{GREEN}好了现在作者要去开发gui版本了，快给star,都看到这里了,订阅走起!!!!!!!!{END}")
