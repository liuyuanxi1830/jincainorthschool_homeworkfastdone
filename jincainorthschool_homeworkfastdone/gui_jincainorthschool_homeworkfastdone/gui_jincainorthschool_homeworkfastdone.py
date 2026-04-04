import io                  # 内存流操作
import atexit              # 程序退出时执行清理函数
import urllib3             # 请求支持，禁用警告
import wave                # WAV音频文件处理
import struct              # 二进制数据打包/解包
import threading           # 多线程操作
import time                
import os                  
import re                  # 正则表达式（提取URL、分割图文文本、匹配LaTeX公式、清理文本）
import json                
import html                
import sys                 
import traceback           # 异常堆栈跟踪
import subprocess          # 子进程调用
import webbrowser          # 浏览器打开
from urllib.parse import urlparse  # URL解析（
import tempfile            # 临时文件创建
import shutil              # 文件夹/文件批量操作
import mimetypes           # MIME类型判断
import gc                  # 垃圾回收
from pathlib import Path   # 路径对象化操作
import pygame              
import pyttsx3             
import tkinter as tk       
import tkinter.font as tkfont  
from notifypy import Notify  
from PIL import Image, ImageTk, ImageDraw  
import requests            
from tkinter import ttk, filedialog, messagebox  
import cairosvg # SVG转PNG


VOICE_RATE = 180

def init_tts_engine_once():
    """全局只初始化一次 TTS 引擎"""
    global GLOBAL_TTS_ENGINE
    if GLOBAL_TTS_ENGINE is None:
        GLOBAL_TTS_ENGINE = pyttsx3.init()
        GLOBAL_TTS_ENGINE.setProperty('rate', VOICE_RATE)
        GLOBAL_TTS_ENGINE.setProperty('volume', 1.0)
init_tts_engine_once()

# 获取当前代码文件所在目录（绝对路径）
CURRENT_DIR = Path(__file__).parent  # 代码文件同级目录
photo_path = "gui_jincainorthschool_homeworkfastdone_photos"

# 3. 图片文件夹完整路径（自动拼接）
IMAGE_FOLDER = CURRENT_DIR / photo_path

IMAGE_FOLDER.mkdir(exist_ok=True)

name_IMAGE_leftimage_page1 = "mianma1.png"
path_DOWNLOAD_IMAGE_leftimage_page1 = str(IMAGE_FOLDER / name_IMAGE_leftimage_page1)

name_iconbitmap_name = "6408t-ng6lk-001.ico"
path_DOWNLOAD_IMAGE_iconbitmap = str(IMAGE_FOLDER / name_iconbitmap_name)

TARGET_FOLDER_NAME = "gui_jincainorthschool_homeworkfastdone_temporary_directory"       # 文件夹名称
name_right_animated_gif_name = "mianma2.gif"
path_DOWNLOAD_IMAGE_right_animated_gif = str(IMAGE_FOLDER / name_right_animated_gif_name)

name_page2_mader_photo_name ="20180122211724_HdtWZ.jpeg"
path_DOWNLOAD_IMAGE_page2_mader_photo = str(IMAGE_FOLDER / name_page2_mader_photo_name)

name_page2_gongchuangtupian1_name = "t1.png"
path_DOWNLOAD_IMAGE_page2_gongchuangtupian1 = str(IMAGE_FOLDER / name_page2_gongchuangtupian1_name)

name_page2_gongchuangtupian2_name = "t2.png"        
path_DOWNLOAD_IMAGE_page2_gongchuangtupian2 = str(IMAGE_FOLDER / name_page2_gongchuangtupian2_name)

name_page2_gongchuangtupian3_name = "t3.png"
path_DOWNLOAD_IMAGE_page2_gongchuangtupian3 = str(IMAGE_FOLDER / name_page2_gongchuangtupian3_name)

name_page2_gongchuangtupian4_name = "t4.png"
path_DOWNLOAD_IMAGE_page2_gongchuangtupian4 = str(IMAGE_FOLDER / name_page2_gongchuangtupian4_name)


name_page3_lindangsign_left = "jbxhai.png"
path_page3_lindangsign_left= str(IMAGE_FOLDER / name_page3_lindangsign_left)
show_page3_lindangsign_left = Image.open(path_page3_lindangsign_left)
show_page3_lindangsign_left = show_page3_lindangsign_left.resize((180, 180), Image.Resampling.LANCZOS)
show_page3_lindangsign_left = ImageTk.PhotoImage(show_page3_lindangsign_left)

name_page3_schoolsign_right = "jbxh.jpg"
path_page3_schoolsign_right= str(IMAGE_FOLDER / name_page3_schoolsign_right)
show_page3_schoolsign_right= Image.open(path_page3_schoolsign_right)
show_page3_schoolsign_right = show_page3_schoolsign_right.resize((180, 180), Image.Resampling.LANCZOS)
show_page3_schoolsign_right = ImageTk.PhotoImage(show_page3_schoolsign_right)

name_page4_liulanqisign_middle = "liulanqitupian.png"
path_page4_liulanqisign_middle= str(IMAGE_FOLDER / name_page4_liulanqisign_middle)
show_page4_liulanqisign_middle= Image.open(path_page4_liulanqisign_middle)
show_page4_liulanqisign_middle = show_page4_liulanqisign_middle.resize((180, 180), Image.Resampling.LANCZOS)
show_page4_liulanqisign_middle = ImageTk.PhotoImage(show_page4_liulanqisign_middle)
def shoe_page_temporary(page_number):
    pages=[page1]
    for page in pages:
        page.pack_forget()
    if page_number==1:
        page1.pack(fill=tk.BOTH, expand=True)
def show_page(page_num):
    pages = [page1, page2, page3, page4, page5, page6, page7, page8, page9, page10, page11, page12, page13, page14, page15,page16]
    
    for page in pages:
        page.pack_forget()
    
    if page_num == 1:
        page1.pack(fill=tk.BOTH, expand=True)
    elif page_num == 2:
        page2.pack(fill=tk.BOTH, expand=True)
    elif page_num == 3:
        page3.pack(fill=tk.BOTH, expand=True)
    elif page_num == 4:
        page4.pack(fill=tk.BOTH, expand=True)
    elif page_num == 5:
        page5.pack(fill=tk.BOTH, expand=True)
    elif page_num == 6:
        page6.pack(fill=tk.BOTH, expand=True)
    elif page_num == 7:
        page7.pack(fill=tk.BOTH, expand=True)
    elif page_num == 8:
        page8.pack(fill=tk.BOTH, expand=True)
    elif page_num == 9:
        page9.pack(fill=tk.BOTH, expand=True)
    elif page_num == 10:
        page10.pack(fill=tk.BOTH, expand=True)
    elif page_num == 11:
        page11.pack(fill=tk.BOTH, expand=True)
    elif page_num == 12:
        page12.pack(fill=tk.BOTH, expand=True)
        # 进入page12时：取消置顶 + 放大窗口
        root.attributes('-topmost', False)
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        new_width = int(screen_width * 0.8)
        new_height = int(screen_height * 0.8)
        x = (screen_width - new_width) // 2
        root.geometry(f"{new_width}x{new_height}+{x}+50")
    elif page_num == 13:
        page13.pack(fill=tk.BOTH, expand=True)
    elif page_num == 14:
        page14.pack(fill=tk.BOTH, expand=True)
    elif page_num == 15:
        page15.pack(fill=tk.BOTH, expand=True)
    elif page_num == 16:
        page16.pack(fill=tk.BOTH, expand=True)
        update_statistics()







def openliulanqi():
    TARGET_URL = "https://base.bestsch.com/BschZncp2/front/index.html"
    try:
        subprocess.Popen(f'start msedge {TARGET_URL}', shell=True)
    except Exception as e:
        print(f" 启动Edge失败：{str(e)}")



class RoundedButton(tk.Canvas):
    def __init__(self, parent, text, command=None, radius=20, color="#B03DC5", active_color="#D98CE7", **kwargs):
        super().__init__(parent, **kwargs)
        self.radius = radius
        self.color = color
        self.active_color = active_color
        self.command = command
        self.text = text

        self.bind("<ButtonPress-1>", self._on_press)
        self.bind("<ButtonRelease-1>", self._on_release)
        self.bind("<Enter>", self._on_enter)
        self.bind("<Leave>", self._on_leave)
        self.bind("<Configure>", self._on_configure)
        self.after(10, self._draw_button, self.color)

    def _on_configure(self, event):
        self._draw_button(self.color)

    def _draw_button(self, color):
        self.delete("all")
        w = self.winfo_reqwidth()
        h = self.winfo_reqheight()
        self.create_rounded_rectangle(0, 0, w, h, radius=self.radius, fill=color, outline="")
        self.create_text(w//2, h//2, text=self.text, fill="white", font=("Arial", 16))

    def create_rounded_rectangle(self, x1, y1, x2, y2, radius=25, **kwargs):
        points = [
            x1+radius, y1, x2-radius, y1, x2, y1, x2, y1+radius,
            x2, y2-radius, x2, y2, x2-radius, y2, x1+radius, y2,
            x1, y2, x1, y2-radius, x1, y1+radius, x1, y1
        ]
        return self.create_polygon(points, **kwargs, smooth=True)

    def _on_press(self, event):
        self._draw_button(self.active_color)

    def _on_release(self, event):
        self._draw_button(self.color)
        if self.command:
            self.command()

    def _on_enter(self, event):
        self.config(cursor="hand2")

    def _on_leave(self, event):
        self._draw_button(self.color)
        self.config(cursor="arrow")


root = tk.Tk()
root.title("loving AI学伴")

def center_window():
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width - 1000) // 2
    y = (screen_height - 600) // 2
    root.geometry(f"1000x600+{x}+{y}")

center_window()
root.withdraw()
try:
    root.iconbitmap(path_DOWNLOAD_IMAGE_iconbitmap)
except Exception as e:
    print(f"图标加载失败：{e}")

root.resizable(False, False)
root.configure(bg="#ED85C9")
TRANSPARENT_COLOR = '#123456'
root.wm_attributes('-transparentcolor', TRANSPARENT_COLOR)







class AnimatedGIF(tk.Label):
    def __init__(self, parent, gif_path, **kwargs):
        if not os.path.exists(gif_path):
            print(f"错误：GIF不存在于路径 {gif_path}")
            super().__init__(parent, text="GIF缺失", bg="#ED94CE", fg="red", font=("Arial", 12))
            return

        self.gif = Image.open(gif_path)
        self.frames = []
        try:
            while True:
                frame = self.gif.copy()
                frame = frame.resize((180, 180), Image.Resampling.LANCZOS)
                self.frames.append(ImageTk.PhotoImage(frame))
                self.gif.seek(len(self.frames))
        except EOFError:
            pass

        print(f"GIF加载完成，共{len(self.frames)}帧")
        self.current_frame = 0
        try:
            self.delay = self.gif.info.get('duration', 100)
        except:
            self.delay = 100

        super().__init__(parent, image=self.frames[0], **kwargs)
        if len(self.frames) > 1:
            self.after(self.delay, self.animate)

    def animate(self):
        self.current_frame = (self.current_frame + 1) % len(self.frames)
        self.config(image=self.frames[self.current_frame])
        self.after(self.delay, self.animate)








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
DOWNLOAD_FOLDER = str(CURRENT_DIR / TARGET_FOLDER_NAME)
# 自动创建文件夹（不存在则创建）
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)
print(f"{GREEN}所有资源将下载到: {DOWNLOAD_FOLDER}{END}")
print(f"{BLUE}正在加载图片...{END}")
show_leftimage_page1 = Image.open(path_DOWNLOAD_IMAGE_leftimage_page1)
show_leftimage_page1 = show_leftimage_page1.resize((180, 180), Image.Resampling.LANCZOS)
show_leftimage_page1= ImageTk.PhotoImage(show_leftimage_page1)

show_page2_mader_photo_name=Image.open(path_DOWNLOAD_IMAGE_page2_mader_photo)
show_page2_mader_photo_name=show_page2_mader_photo_name.resize((180, 180), Image.Resampling.LANCZOS)
show_page2_mader_photo_name= ImageTk.PhotoImage(show_page2_mader_photo_name)

show_page2_gongchuangtupian1 = Image.open(name_page2_gongchuangtupian1_name).resize((60, 60), Image.Resampling.LANCZOS)
show_page2_gongchuangtupian2 = Image.open(name_page2_gongchuangtupian2_name).resize((60, 60), Image.Resampling.LANCZOS)
show_page2_gongchuangtupian3 = Image.open(name_page2_gongchuangtupian3_name).resize((60, 60), Image.Resampling.LANCZOS)
show_page2_gongchuangtupian4 = Image.open(name_page2_gongchuangtupian4_name).resize((60, 60), Image.Resampling.LANCZOS)

show_page2_gongchuangtupian1 = ImageTk.PhotoImage(show_page2_gongchuangtupian1)
show_page2_gongchuangtupian2 = ImageTk.PhotoImage(show_page2_gongchuangtupian2)
show_page2_gongchuangtupian3 = ImageTk.PhotoImage(show_page2_gongchuangtupian3)
show_page2_gongchuangtupian4 = ImageTk.PhotoImage(show_page2_gongchuangtupian4)
print(f"{GREEN}第一张图片加载完成{END}")




print("开始构建页面...")

# 页面1
page1 = tk.Frame(root, bg="#ED94CE")
title_canvas = tk.Canvas(page1, bg="#ED94CE", height=200, highlightthickness=0)
title_canvas.pack(side=tk.TOP, fill=tk.X)
title_font = tkfont.Font(family="Segoe Print", size=80, weight="bold")
title_text_id = title_canvas.create_text(500, 100, text="loving AI学伴", font=title_font, fill="#F11477", anchor="center")
middle_frame = tk.Frame(page1, bg="#ED94CE")
middle_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=50)
label2 = tk.Label(middle_frame, text="这个应用可以帮你完成金杯学伴机的作业", font=("Segoe Print", 24), bg="#ED94CE", fg="#79098D", justify=tk.CENTER, wraplength=800)
label2.pack(side=tk.BOTTOM, pady=(0, 30))
button_frame = tk.Frame(page1, bg="#ED94CE")
button_frame.pack(side=tk.BOTTOM, pady=20)
left_img_label = tk.Label(button_frame, image=show_leftimage_page1, bg="#ED94CE")
left_img_label.image = show_leftimage_page1
left_img_label.pack(side=tk.LEFT, padx=(0, 20))
btn_next1 = RoundedButton(button_frame, text="开始", command=lambda: show_page(2), radius=66, width=200, height=66, bg="#ED94CE", highlightthickness=0)
btn_next1.pack(side=tk.LEFT)
right_animated_gif = AnimatedGIF(button_frame, path_DOWNLOAD_IMAGE_right_animated_gif, bg="#ED94CE")
right_animated_gif.pack(side=tk.LEFT, padx=(20, 0))

min_size, max_size, step, current_size, direction = 70, 90, 0.5, 80, 1
def animate_title():
    global current_size, direction
    try:
        # 检查画布是否还存在
        if not title_canvas.winfo_exists():
            return
        new_size = current_size + direction * step
        if new_size > max_size or new_size < min_size:
            direction *= -1
            new_size = current_size + direction * step
        current_size = new_size
        title_font.config(size=int(current_size))
        title_canvas.itemconfig(title_text_id, font=title_font)
        root.after(30, animate_title)
    except (tk.TclError, AttributeError):
        # 对象已不存在，停止动画
        pass
root.after(200, animate_title)








page2 = tk.Frame(root, bg="#ED94CE")
page2.grid_columnconfigure(0, weight=1)
page2.grid_columnconfigure(1, weight=1)
page2.grid_rowconfigure(0, weight=0)
page2.grid_rowconfigure(1, weight=1)
page2.grid_rowconfigure(2, weight=0)
page2.grid_rowconfigure(3, weight=0)
title_label = tk.Label(page2, text="loving AI学伴", font=("Segoe Print", 50, "bold"), bg="#ED94CE", fg="#F11477")
title_label.grid(row=0, column=0, columnspan=2, pady=(30, 10), sticky="n")
author_label = tk.Label(page2, text="作者:lyx", font=("Segoe Print", 50, "bold"), bg="#ED94CE", fg="#821DDA")
author_label.grid(row=1, column=0, padx=(10, 5), pady=(20, 0), sticky="ne")
left_img_label1 = tk.Label(page2, image=show_page2_mader_photo_name, bg="#ED94CE")
left_img_label1.image = show_page2_mader_photo_name
left_img_label1.grid(row=1, column=1, padx=(5, 10), pady=(20, 0), sticky="nw")
bottom_content_frame = tk.Frame(page2, bg="#ED94CE")
bottom_content_frame.grid(row=2, column=0, columnspan=2, pady=(20, 10))
gongchuang_label = tk.Label(bottom_content_frame, text="共创: ", font=("Segoe Print", 30, "bold"), bg="#ED94CE", fg="#F11477")
gongchuang_label.pack(side=tk.LEFT, padx=(0, 20))
small_images_frame = tk.Frame(bottom_content_frame, bg="#ED94CE")
small_images_frame.pack(side=tk.LEFT)
small_img_labels = []
for i, small_img in enumerate([show_page2_gongchuangtupian1,show_page2_gongchuangtupian2 ,show_page2_gongchuangtupian3 ,show_page2_gongchuangtupian4 ]):
    img_label = tk.Label(small_images_frame, image=small_img, bg="#ED94CE")
    img_label.image = small_img
    img_label.pack(side=tk.LEFT, padx=5)
    small_img_labels.append(img_label)
btn_next2 = RoundedButton(page2, text="继续", command=lambda: show_page(3), radius=66, width=200, height=66, bg="#ED94CE", highlightthickness=0)
btn_next2.grid(row=3, column=0, columnspan=2, pady=30, sticky="s")






page3 = tk.Frame(root, bg="#ED94CE")
label3_page3 = tk.Label(page3, text="loving AI学伴", font=("Segoe Print", 50, "bold"), bg="#ED94CE", fg="#F11477")
label3_page3.pack(pady=(20, 10))
image_frame = tk.Frame(page3, bg="#ED94CE")
image_frame.pack(expand=True)
left_canvas = tk.Canvas(image_frame, width=180, height=180, bg='#ED94CE', highlightthickness=0)
left_canvas.pack(side=tk.LEFT, padx=20)
left_canvas.create_image(90, 90, image=show_page3_lindangsign_left)
left_canvas.image = show_page3_lindangsign_left
right_canvas = tk.Canvas(image_frame, width=180, height=180, bg='#ED94CE', highlightthickness=0)
right_canvas.pack(side=tk.LEFT, padx=20)
right_canvas.create_image(90, 90, image=show_page3_schoolsign_right)
right_canvas.image = show_page3_schoolsign_right
btn_next4 = RoundedButton(page3, text="开始", command=lambda: show_page(4), radius=66, width=200, height=66, bg="#ED94CE", highlightthickness=0)
btn_next4.pack(pady=20)

line_step, line_delay, line_width, line_color = 5, 30, 3, "red"
stage, progress = 1, 0
left_line1 = left_line2 = right_line1 = right_line2 = None

def draw_x_animation():
    global stage, progress, left_line1, left_line2, right_line1, right_line2
    try:
        # 检查画布是否还存在
        if not left_canvas.winfo_exists() or not right_canvas.winfo_exists():
            return
            
        if stage == 1:
            x1, y1, x2, y2 = 0, 0, 180, 180
            if progress == 0:
                # 先检查画布是否存在再删除
                try:
                    if left_canvas.winfo_exists():
                        left_canvas.delete("line")
                    if right_canvas.winfo_exists():
                        right_canvas.delete("line")
                except:
                    pass
                left_line1 = left_line2 = right_line1 = right_line2 = None
            
            end_x = x1 + (x2 - x1) * progress / 100
            end_y = y1 + (y2 - y1) * progress / 100
            
            try:
                if left_line1 is None and left_canvas.winfo_exists():
                    left_line1 = left_canvas.create_line(x1, y1, end_x, end_y, fill=line_color, width=line_width, capstyle=tk.ROUND, tags="line")
                elif left_canvas.winfo_exists():
                    left_canvas.coords(left_line1, x1, y1, end_x, end_y)
                    
                if right_line1 is None and right_canvas.winfo_exists():
                    right_line1 = right_canvas.create_line(x1, y1, end_x, end_y, fill=line_color, width=line_width, capstyle=tk.ROUND, tags="line")
                elif right_canvas.winfo_exists():
                    right_canvas.coords(right_line1, x1, y1, end_x, end_y)
            except:
                pass
            
            progress += line_step
            if progress >= 100:
                progress = 100
                try:
                    if left_canvas.winfo_exists():
                        left_canvas.coords(left_line1, x1, y1, x2, y2)
                    if right_canvas.winfo_exists():
                        right_canvas.coords(right_line1, x1, y1, x2, y2)
                except:
                    pass
                stage, progress = 2, 0
                root.after(line_delay, draw_x_animation)
            else:
                root.after(line_delay, draw_x_animation)
                
        elif stage == 2:
            x1, y1, x2, y2 = 180, 0, 0, 180
            end_x = x1 + (x2 - x1) * progress / 100
            end_y = y1 + (y2 - y1) * progress / 100
            
            try:
                if left_line2 is None and left_canvas.winfo_exists():
                    left_line2 = left_canvas.create_line(x1, y1, end_x, end_y, fill=line_color, width=line_width, capstyle=tk.ROUND, tags="line")
                elif left_canvas.winfo_exists():
                    left_canvas.coords(left_line2, x1, y1, end_x, end_y)
                    
                if right_line2 is None and right_canvas.winfo_exists():
                    right_line2 = right_canvas.create_line(x1, y1, end_x, end_y, fill=line_color, width=line_width, capstyle=tk.ROUND, tags="line")
                elif right_canvas.winfo_exists():
                    right_canvas.coords(right_line2, x1, y1, end_x, end_y)
            except:
                pass
            
            progress += line_step
            if progress >= 100:
                progress = 100
                try:
                    if left_canvas.winfo_exists():
                        left_canvas.coords(left_line2, x1, y1, x2, y2)
                    if right_canvas.winfo_exists():
                        right_canvas.coords(right_line2, x1, y1, x2, y2)
                except:
                    pass
                root.after(200, clear_lines)
            else:
                root.after(line_delay, draw_x_animation)
                
    except (tk.TclError, AttributeError, TypeError) as e:
        print(f"动画已停止: {e}")
        return

def clear_lines():
    global stage, progress
    try:
        if left_canvas.winfo_exists():
            left_canvas.delete("line")
        if right_canvas.winfo_exists():
            right_canvas.delete("line")
    except:
        pass
    stage, progress = 1, 0
    # 检查画布是否还存在再继续动画
    try:
        if left_canvas.winfo_exists() and right_canvas.winfo_exists():
            draw_x_animation()
    except:
        pass




page4 = tk.Frame(root, bg="#ED94CE")
label_page4 = tk.Label(page4, text="loving AI学伴", font=("Segoe Print", 50, "bold"), bg="#ED94CE", fg="#F11477")
label_page4.pack(pady=(20, 10))
middle_frame4 = tk.Frame(page4, bg="#ED94CE")
middle_frame4.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=50)
left_img_label11 = tk.Label(middle_frame4, image=show_page4_liulanqisign_middle, bg="#ED94CE")
left_img_label11.image = show_page4_liulanqisign_middle
left_img_label11.pack()
button_frame4 = tk.Frame(page4, bg="#ED94CE")
button_frame4.pack(side=tk.BOTTOM, pady=20)
left_img_label4 = tk.Label(button_frame4, image=show_leftimage_page1, bg="#ED94CE")
left_img_label4.image = show_leftimage_page1
left_img_label4.pack(side=tk.LEFT, padx=(0, 20))
btn_open_google = RoundedButton(button_frame4, text="打开浏览器", command=openliulanqi, radius=66, width=200, height=66, bg="#ED94CE", highlightthickness=0)
btn_open_google.pack(side=tk.LEFT)
right_animated_gif4 = AnimatedGIF(button_frame4, path_DOWNLOAD_IMAGE_right_animated_gif, bg="#ED94CE")
right_animated_gif4.pack(side=tk.LEFT, padx=(20, 0))



page5 = tk.Frame(root, bg="#ED94CE")
label_page5 = tk.Label(page5, text="请完成登录", font=("Segoe Print", 50, "bold"), bg="#ED94CE", fg="#F11477")
label_page5.pack(expand=True)
btn_open_google1 = RoundedButton(page5, text="下一步", command=lambda: show_page(6), radius=66, width=200, height=66, bg="#ED94CE", highlightthickness=0)
btn_open_google1.pack(pady=(0,20))



page6 = tk.Frame(root, bg="#ED94CE")
label_page6 = tk.Label(page6, text="右击浏览器空白处，点击检查，打开开发者工具", wraplength=350, font=("Segoe Print", 29, "bold"), bg="#ED94CE", fg="#F11477")
label_page6.pack(expand=True)
btn_open_google1 = RoundedButton(page6, text="下一步", command=lambda: show_page(7), radius=66, width=200, height=66, bg="#ED94CE", highlightthickness=0)
btn_open_google1.pack(pady=(0,20))



page7 = tk.Frame(root, bg="#ED94CE")
label_page7 = tk.Label(page7, text="点击应用，找到cookie，点击cookie下的https://base.bestsch.com", wraplength=250, font=("Segoe Print", 23, "bold"), bg="#ED94CE", fg="#F11477")
label_page7.pack(expand=True)
btn_open_google1 = RoundedButton(page7, text="下一步", command=lambda: show_page(8), radius=66, width=200, height=66, bg="#ED94CE", highlightthickness=0)
btn_open_google1.pack(pady=(0,20))


page8 = tk.Frame(root, bg="#ED94CE")
label_page8 = tk.Label(page8, text="找到path下的/BschZncp2", wraplength=250, font=("Segoe Print", 35, "bold"), bg="#ED94CE", fg="#F11477")
label_page8.pack(expand=True)
btn_open_google1 = RoundedButton(page8, text="下一步", command=lambda: show_page(9), radius=66, width=200, height=66, bg="#ED94CE", highlightthickness=0)
btn_open_google1.pack(pady=(0,20))


page9 = tk.Frame(root, bg="#ED94CE")
label_page9 = tk.Label(page9, text="复制JSESSIONID对应的值", wraplength=250, font=("Segoe Print", 35, "bold"), bg="#ED94CE", fg="#F11477")
label_page9.pack(expand=True)
btn_open_google1 = RoundedButton(page9, text="下一步", command=lambda: show_page(10), radius=66, width=200, height=66, bg="#ED94CE", highlightthickness=0)
btn_open_google1.pack(pady=(0,20))


page10 = tk.Frame(root, bg="#ED94CE")
entry_var = tk.StringVar(value="点击输入粘贴的JSESSIONID")

def on_entry_focus_in(event):
    if entry_var.get() == "点击输入粘贴的JSESSIONID":
        entry_var.set("")
        entry.config(fg="black")

def on_entry_focus_out(event):
    if entry_var.get().strip() == "":
        entry_var.set("点击输入粘贴的JSESSIONID")
        entry.config(fg="gray")

def try_go_to_page11():
    content = entry_var.get().strip()
    if content and content != "点击输入粘贴的JSESSIONID":
        print(f"输入的JSESSIONID: {content}")
        show_page(11)
    else:
        pass

entry_frame = tk.Frame(page10, bg="#ED94CE")
entry_frame.pack(expand=True, padx=20, pady=20)
entry_frame.pack_propagate(False)
entry_frame.configure(width=400, height=60)
entry = tk.Entry(entry_frame, textvariable=entry_var, font=("微软雅黑", 16), bg="#FE71A0", fg="gray", bd=0, highlightthickness=0, justify=tk.CENTER)
entry.place(relx=0.5, rely=0.5, anchor=tk.CENTER, width=380, height=50)
entry.bind("<FocusIn>", on_entry_focus_in)
entry.bind("<FocusOut>", on_entry_focus_out)

btn_next10 = RoundedButton(page10, text="开始爬取", command=try_go_to_page11, radius=66, width=200, height=66, bg="#ED94CE", highlightthickness=0)
btn_next10.pack(pady=20)



page11 = tk.Frame(root, bg="#ED94CE")
style = ttk.Style()
style.theme_use('clam')
style.configure("custom.Horizontal.TProgressbar", background="#B03DC5", troughcolor="#ED94CE", bordercolor="#B03DC5", lightcolor="#B03DC5", darkcolor="#B03DC5")
progress_var = tk.IntVar()
percent_text = tk.StringVar(value="0%")
label_crawling = tk.Label(page11, text="爬取中,请稍后", font=("微软雅黑", 24, "bold"), bg="#ED94CE", fg="#B03DC5")
label_crawling.pack(pady=(50, 20))
progress_frame = tk.Frame(page11, bg="#ED94CE")
progress_frame.pack(pady=10)
progress_bar = ttk.Progressbar(progress_frame, style="custom.Horizontal.TProgressbar", variable=progress_var, maximum=100, length=300, mode='determinate')
progress_bar.pack(side=tk.LEFT, padx=(0, 10))
percent_label = tk.Label(progress_frame, textvariable=percent_text, font=("Arial", 16, "bold"), bg="#ED94CE", fg="#F11477")
percent_label.pack(side=tk.LEFT)

def background_task(jsessionid):
    global zuoye_list_data, pygame_initialized
    try:
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
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        }
        ZUOYE_LIST_URL = "https://base.bestsch.com/BschZncp2/api/FindMyZuoye"

        session = requests.Session()
        session.verify = False
        session.timeout = 30
        session.cookies.set("JSESSIONID", jsessionid, domain="base.bestsch.com", path="/BschZncp2")
        session.cookies.set("currentrole", CURRENT_ROLE, domain="base.bestsch.com", path="/BschZncp2")

        all_zuoye = []
        page = 1
        page_size = 10
        total = 0
        print("后台线程：开始获取作业列表...")
        while True:
            params = {"page": page, "count": page_size}
            resp = session.get(ZUOYE_LIST_URL, params=params, headers=HEADERS, timeout=15, verify=False)
            result = resp.json()
            if result.get("code") != 0:
                print(f"后台线程：第{page}页获取失败：{result.get('msg')}")
                break
            data = result.get("data", {})
            total = data.get("total", 0)
            zuoye_list = data.get("content", [])
            if not zuoye_list:
                break
            all_zuoye.extend(zuoye_list)
            print(f"后台线程：第{page}页获取成功，累计 {len(all_zuoye)}/{total} 条")
            if len(all_zuoye) >= total:
                break
            page += 1
        zuoye_list_data = all_zuoye
        print(f"后台线程：作业列表获取完成，共 {len(zuoye_list_data)} 条")
        
        # ========== 在作业列表获取完成后初始化pygame ==========
        global pygame_initialized
        if not pygame_initialized:
            try:
                pygame.mixer.quit()
                pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)
                pygame_initialized = True
                print(" Pygame音频初始化成功（作业列表获取后）")
            except Exception as e:
                print(f" Pygame音频初始化失败: {e}")
        # ====================================================
        
    except Exception as e:
        print(f"后台线程异常：{str(e)}")
        zuoye_list_data = []
def start_progress():
    jsessionid = entry_var.get().strip()
    if not jsessionid or jsessionid == "点击输入粘贴的JSESSIONID":
        print("错误：未输入有效的JSESSIONID")
        return
    progress_var.set(0)
    percent_text.set("0%")
    update_progress(0)
    thread = threading.Thread(target=background_task, args=(jsessionid,), daemon=True)
    thread.start()

def update_progress(value):
    progress_var.set(value)
    percent_text.set(f"{value}%")
    if value < 100:
        root.after(50, update_progress, value + 1)
    else:
        show_page(12)

page11.bind("<Map>", lambda e: start_progress())


def clean_text(text, base_url="https://base.bestsch.com"):
    """
    清理文本：将整个<img>标签和包含图片的<span>标签替换为 '!' + 图片绝对URL + '!'，
    去除其他HTML标签，转换实体，合并空白。
    """
    if not text:
        return ""
    text = str(text)
    # 1. 处理直接的 <img> 标签
    def img_replacer(match):
        src = match.group(1)
        if src.startswith("http"):
            full_url = src
        else:
            if not src.startswith("/"):
                src = "/" + src
            full_url = base_url + src
        return f"!{full_url}!"

    text = re.sub(r'<img\s+[^>]*src="([^">]+)"[^>]*>', img_replacer, text)

    # 2. 处理 <span class="qml-an"> 里面包含的 <img>
    def span_img_replacer(match):
        span_content = match.group(1)
        # 从 span_content 中提取 img 的 src
        src_match = re.search(r'<img\s+[^>]*src="([^">]+)"', span_content)
        if src_match:
            src = src_match.group(1)
            if src.startswith("http"):
                full_url = src
            else:
                if not src.startswith("/"):
                    src = "/" + src
                full_url = base_url + src
            return f"!{full_url}!"
        return ""  # 没找到图片就返回空

    text = re.sub(r'<span[^>]*class="[^"]*qml-an[^"]*"[^>]*>(.*?)</span>', span_img_replacer, text, flags=re.DOTALL)

    # 3. 移除所有剩余的HTML标签
    text = re.sub(r"<[^>]+>", "", text)

    # 4. 转换HTML实体
    text = html.unescape(text)

    # 5. 移除控制字符
    text = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f\x7f-\x9f]', '', text)

    # 6. 合并连续空白为一个空格，并去除首尾空格
    text = re.sub(r'\s+', ' ', text).strip()

    return text



def clean_text_with_formula(raw_text):
    """改造后的文本清理函数（保留公式语法）"""
    # 调用你原来的clean_text函数
    clean_html = clean_text(raw_text)
    # 清理多余转义符，保留公式语法
    clean_html = clean_html.replace("\\{", "{").replace("\\}", "}")
    return clean_html


def fix_json_text(raw_text):
    """
    修复不标准的JSON文本：去除可能的前缀/后缀，删除多余的逗号。
    """
    if not raw_text:
        return "{}"
    raw_text = raw_text.strip()
    # 提取花括号内容（去除可能的BOM或前缀）
    match = re.search(r'(\{.*\})', raw_text, re.DOTALL)
    if match:
        raw_text = match.group(1)
    # 移除多余的逗号（尾随逗号）
    raw_text = re.sub(r',\s*}', '}', raw_text)
    raw_text = re.sub(r',\s*]', ']', raw_text)
    return raw_text



def extract_question_info(question_dict):
    """
    从单个题目对象中提取结构化信息，图片已嵌入到文本中。
    返回包含 id, title, options, correct_answer, explanation, media_urls 的字典。
    """
    info = {
        "id": question_dict.get("id"),          # 保留id字段用于匹配
        "title": "",
        "options": [],
        "correct_answer": "",
        "explanation": "",
        "media_urls": []
    }

    # 标题（含内联图片）
    title_html = question_dict.get("name", "")
    info["title"] = clean_text_with_formula(title_html)

    # 选项提取：从config字段解析
    config_str = question_dict.get("config", "{}")
    if config_str and config_str != "{}":
        try:
            fixed_config = fix_json_text(config_str)
            config = json.loads(fixed_config)
            opt_list = config.get("options", [])
            for opt_html in opt_list:
                info["options"].append(clean_text(opt_html))
        except Exception as e:
            print(f" 从config解析选项失败: {e}")
            # 备选方案：直接从question_dict获取options字段
            alt_opts = question_dict.get("options") or question_dict.get("optionList")
            if alt_opts:
                for opt_html in alt_opts:
                    info["options"].append(clean_text(opt_html))

    # 答案处理逻辑
    raw_answer = question_dict.get("answer", "")

    # 防护：如果raw_answer是整数，先转为字符串
    if isinstance(raw_answer, int):
        raw_answer = str(raw_answer)
        print(f" 检测到答案为整数，已转换为字符串: {raw_answer}")

    # 如果raw_answer是字符串且符合JSON数组格式，解析
    if isinstance(raw_answer, str) and raw_answer.strip().startswith('[') and raw_answer.strip().endswith(']'):
        try:
            answer_list = json.loads(raw_answer)
            if answer_list and len(answer_list) > 0:
                raw_answer = str(answer_list[0]) if not isinstance(answer_list[0], str) else answer_list[0]
                print(f" 解析答案数组成功: {raw_answer[:50]}...")
        except json.JSONDecodeError as e:
            print(f"答案JSON解析失败: {e}, 保持原样: {raw_answer[:50]}")
        except Exception as e:
            print(f" 答案处理异常: {e}")

    # 清理答案文本
    answer_clean = clean_text(raw_answer).strip("[]")

    # 转换为选项索引（A、B、C...）
    try:
        answer_clean_digit = ''.join(filter(str.isdigit, answer_clean))
        if answer_clean_digit:
            answer_idx = int(answer_clean_digit)
            option_labels = ["A", "B", "C", "D", "E", "F", "G", "H"]
            if 0 <= answer_idx < len(option_labels):
                info["correct_answer"] = option_labels[answer_idx]
            else:
                info["correct_answer"] = answer_clean
        else:
            info["correct_answer"] = answer_clean
    except (ValueError, TypeError, IndexError) as e:
        print(f" 答案转换为选项索引失败: {e}，使用原始清理文本")
        info["correct_answer"] = answer_clean

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





def fetch_zuoye_detail_thread(zuoye_id, user_zuoye_id, jsessionid):
    global current_zuoye_detail, current_zuoye_name
    try:
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
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        }
        ZUOYE_DETAIL_URL = "https://base.bestsch.com/BschZncp2/api/FindUserZuoye2"
        ANSWER_RECORD_URL = "https://base.bestsch.com/BschZncp2/api/findUserAnswerRecordAll"
        session = requests.Session()
        session.verify = False
        session.timeout = 30
        session.cookies.set("JSESSIONID", jsessionid, domain="base.bestsch.com", path="/BschZncp2")
        session.cookies.set("currentrole", CURRENT_ROLE, domain="base.bestsch.com", path="/BschZncp2")
        # 获取详情
        detail_params = {"zuoyeId": zuoye_id, "userZuoyeId": user_zuoye_id}
        detail_resp = session.get(ZUOYE_DETAIL_URL, params=detail_params, headers=HEADERS, timeout=15)
        detail_data = detail_resp.json()
        questions = []
        if detail_data.get("code") == 0:
            q_list = detail_data.get("data", {}).get("zuoyeQestionList", [])
            for q in q_list:
                questions.append(extract_question_info(q))
        # 获取答题记录
        record_params = {"userZuoyeId": user_zuoye_id}
        record_resp = session.get(ANSWER_RECORD_URL, params=record_params, headers=HEADERS, timeout=15)
        record_data = record_resp.json()
        if record_data.get("code") == 0:
            record_list = record_data.get("data", [])
            for item in record_list:
                q_dict = item.get("userAnswer", {}).get("zuoyeQestion", {})
                q_id = q_dict.get("id")
                for q in questions:
                    if q.get("id") == q_id:
                        q["user_answer"] = item.get("userAnswer", {}).get("answer", "")
                        q["score"] = item.get("userAnswer", {}).get("fenshu", "")
                        break
        current_zuoye_detail = questions
        root.after(0, lambda: show_page(14))
    except Exception as e:
        print(f"获取详情异常：{str(e)}")
        root.after(0, lambda: messagebox.showerror("错误", f"获取详情失败：{str(e)}"))





page12 = tk.Frame(root, bg="#ED94CE")
tip_label = tk.Label(page12, text="双击作业即可跳转  made by lyx", font=("微软雅黑", 14), bg="#ED94CE", fg="#666666")
tip_label.pack(pady=(10, 0))
label_page12 = tk.Label(page12, text="作业列表", font=("Segoe Print", 40, "bold"), bg="#ED94CE", fg="#F11477")
label_page12.pack(pady=(5, 10))

# ----- 工具栏（搜索、过滤器、刷新）-----
toolbar = tk.Frame(page12, bg="#ED94CE")
toolbar.pack(fill=tk.X, padx=20, pady=5)
stats_btn = RoundedButton(toolbar, text=" 统计面板", command=lambda: show_page(15), 
                          radius=20, width=120, height=30, bg="#ED94CE", highlightthickness=0)
stats_btn.pack(side=tk.LEFT, padx=(20,0))

tk.Label(toolbar, text=" 搜索:", font=("微软雅黑", 12), bg="#ED94CE", fg="#333").pack(side=tk.LEFT)
search_var = tk.StringVar()
search_entry = tk.Entry(toolbar, textvariable=search_var, font=("微软雅黑", 12), bg="white", fg="black", width=20)
search_entry.pack(side=tk.LEFT, padx=5)

tk.Label(toolbar, text="状态:", font=("微软雅黑", 12), bg="#ED94CE", fg="#333").pack(side=tk.LEFT, padx=(10,5))
status_filter_var = tk.StringVar(value="全部")
status_combo = ttk.Combobox(toolbar, textvariable=status_filter_var, values=["全部", "已完成", "未完成"], state="readonly", width=8, font=("微软雅黑", 12))
status_combo.pack(side=tk.LEFT, padx=5)

refresh_btn = RoundedButton(toolbar, text="刷新", command=lambda: refresh_zuoye_list(), radius=20, width=80, height=30, bg="#ED94CE", highlightthickness=0)
refresh_btn.pack(side=tk.LEFT, padx=(20,0))

search_entry.bind("<KeyRelease>", lambda e: filter_current_tab())
status_combo.bind("<<ComboboxSelected>>", lambda e: filter_current_tab())

# ----- 标签页 -----
notebook = ttk.Notebook(page12)
notebook.pack(expand=True, fill=tk.BOTH, padx=20, pady=5)

frame_all = tk.Frame(notebook, bg="#ED94CE")
frame_chinese = tk.Frame(notebook, bg="#ED94CE")
frame_math = tk.Frame(notebook, bg="#ED94CE")
frame_english = tk.Frame(notebook, bg="#ED94CE")
notebook.add(frame_all, text="全部")
notebook.add(frame_chinese, text="语文 ")
notebook.add(frame_math, text="数学 ")
notebook.add(frame_english, text="英语 ")

# ----- 定义创建Treeview的辅助函数 -----
def create_treeview_with_scroll(parent):
    f = tk.Frame(parent, bg="#ED94CE")
    f.pack(expand=True, fill=tk.BOTH, padx=5, pady=5)
    
    vsb = tk.Scrollbar(f, orient="vertical")
    vsb.pack(side=tk.RIGHT, fill=tk.Y)
    hsb = tk.Scrollbar(f, orient="horizontal")
    hsb.pack(side=tk.BOTTOM, fill=tk.X)
    
    columns = ("name", "teacher", "time", "status")
    tree = ttk.Treeview(f, columns=columns, show="headings", yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
    
    vsb.config(command=tree.yview)
    hsb.config(command=tree.xview)
    
    tree.heading("name", text="作业名称")
    tree.heading("teacher", text="老师")
    tree.heading("time", text="时间")
    tree.heading("status", text="状态")
    tree.column("name", width=300, minwidth=200)
    tree.column("teacher", width=100, minwidth=80)
    tree.column("time", width=150, minwidth=100)
    tree.column("status", width=80, minwidth=60)
    
    tree.item_data = {}
    return tree

# 为每个标签页创建Treeview
tree_all = create_treeview_with_scroll(frame_all)
tree_chinese = create_treeview_with_scroll(frame_chinese)
tree_math = create_treeview_with_scroll(frame_math)
tree_english = create_treeview_with_scroll(frame_english)

# 映射：每个Treeview对应的作业列表（原始数据，由更新列表时填充）
all_items_map = []
chinese_items_map = []
math_items_map = []
english_items_map = []



def get_subject_by_teacherid(teacher_id):
    #网页给的就是cid，要更多老师的话，自己找
    #说实话你也找不到，因为网页根本就没有按学科排序φ(>ω<*) 
    if teacher_id == "153299": return "英语"
    elif teacher_id == "253449": return "语文"
    elif teacher_id == "435534": return "数学"
    else: return "其他"


def Sort_zuoyelist(lst):
    def sort_key(zuoye):
        status = zuoye.get('isComplete')
        status_group = 0 if status in [0, 1] else 1
        start_date = zuoye.get('startDate', '')
        return (status_group, start_date)
    return sorted(lst, key=sort_key)

def claer_all_list():
    for tree in [tree_all, tree_chinese, tree_math, tree_english]:
        tree.delete(*tree.get_children())
        tree.item_data.clear()
    all_items_map.clear()
    chinese_items_map.clear()
    math_items_map.clear()
    english_items_map.clear()

def add_color_list(tree, item_map, zuoye):
    name = zuoye.get('name', '无名称')
    teacher = zuoye.get('cname', '未知老师')
    status = zuoye.get('isComplete')
    status_map = {0: "未提交", 1: "进行中", 3: "已完成"}
    status_text = status_map.get(status, "未知")
    start = zuoye.get('startDate', '')
    time_str = start[:16] if start else ""
    
    values = (name, teacher, time_str, status_text)
    item_id = tree.insert('', tk.END, values=values)
    tree.item_data[item_id] = zuoye
    
    if status == 3:
        tree.tag_configure('completed', foreground='green')
        tree.item(item_id, tags=('completed',))
    elif status in [0, 1]:
        tree.tag_configure('uncompleted', foreground='red')
        tree.item(item_id, tags=('uncompleted',))
    
    item_map.append(zuoye)

def filter_current_tab():
    search_text = search_var.get().strip().lower()
    status_filter = status_filter_var.get()
    
    current_tab = notebook.index(notebook.select())
    if current_tab == 0:
        tree = tree_all
        data_list = all_items_map
    elif current_tab == 1:
        tree = tree_chinese
        data_list = chinese_items_map
    elif current_tab == 2:
        tree = tree_math
        data_list = math_items_map
    elif current_tab == 3:
        tree = tree_english
        data_list = english_items_map
    else:
        return
    
    tree.delete(*tree.get_children())
    tree.item_data.clear()
    
    for zuoye in data_list:
        status = zuoye.get('isComplete')
        if status_filter == "已完成" and status != 3:
            continue
        if status_filter == "未完成" and status not in [0, 1]:
            continue
        
        if search_text:
            name = zuoye.get('name', '').lower()
            teacher = zuoye.get('cname', '').lower()
            time_str = zuoye.get('startDate', '').lower()
            if search_text not in name and search_text not in teacher and search_text not in time_str:
                continue
        
        name_disp = zuoye.get('name', '无名称')
        teacher_disp = zuoye.get('cname', '未知老师')
        status_map = {0: "未提交", 1: "进行中", 3: "已完成"}
        status_text = status_map.get(status, "未知")
        time_disp = zuoye.get('startDate', '')[:16]
        values = (name_disp, teacher_disp, time_disp, status_text)
        item_id = tree.insert('', tk.END, values=values)
        tree.item_data[item_id] = zuoye
        if status == 3:
            tree.item(item_id, tags=('completed',))
        else:
            tree.item(item_id, tags=('uncompleted',))

def reshow_list():
    global zuoye_list_data
    claer_all_list()
    if not zuoye_list_data:
        tree_all.insert('', tk.END, values=("暂无作业数据", "", "", ""))
        return
    
    sorted_all = Sort_zuoyelist(zuoye_list_data)
    for zuoye in sorted_all:
        add_color_list(tree_all, all_items_map, zuoye)
        teacher_id = zuoye.get('cid', '')
        subject = get_subject_by_teacherid(teacher_id)
        if subject == "语文":
            add_color_list(tree_chinese, chinese_items_map, zuoye)
        elif subject == "数学":
            add_color_list(tree_math, math_items_map, zuoye)
        elif subject == "英语":
            add_color_list(tree_english, english_items_map, zuoye)
    
    for tree in [tree_all, tree_chinese, tree_math, tree_english]:
        tree.tag_configure('completed', foreground='green')
        tree.tag_configure('uncompleted', foreground='red')
    
    search_var.set("")
    status_filter_var.set("全部")
    filter_current_tab()

def refresh_zuoye_list():
    jsessionid = entry_var.get().strip()
    if not jsessionid or jsessionid == "点击输入粘贴的JSESSIONID":
        messagebox.showwarning("提示", "请先在页面10输入有效的JSESSIONID")
        show_page(10)
        return
    loading = tk.Toplevel(root)
    loading.title("刷新中")
    loading.geometry("300x100+{}+{}".format(root.winfo_x()+350, root.winfo_y()+250))
    tk.Label(loading, text="正在刷新作业列表...", font=("微软雅黑", 14)).pack(expand=True)
    loading.update()
    
    def task():
        global zuoye_list_data
        try:
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
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
            }
            ZUOYE_LIST_URL = "https://base.bestsch.com/BschZncp2/api/FindMyZuoye"
            session = requests.Session()
            session.verify = False
            session.timeout = 30
            session.cookies.set("JSESSIONID", jsessionid, domain="base.bestsch.com", path="/BschZncp2")
            session.cookies.set("currentrole", CURRENT_ROLE, domain="base.bestsch.com", path="/BschZncp2")
            
            all_zuoye = []
            page = 1
            page_size = 10
            while True:
                params = {"page": page, "count": page_size}
                resp = session.get(ZUOYE_LIST_URL, params=params, headers=HEADERS, timeout=15, verify=False)
                result = resp.json()
                if result.get("code") != 0:
                    break
                data = result.get("data", {})
                total = data.get("total", 0)
                zuoye_list = data.get("content", [])
                if not zuoye_list:
                    break
                all_zuoye.extend(zuoye_list)
                if len(all_zuoye) >= total:
                    break
                page += 1
            zuoye_list_data = all_zuoye
        except Exception as e:
            print(f"刷新异常：{str(e)}")
            zuoye_list_data = []
        finally:
            root.after(0, loading.destroy)
            root.after(0, lambda: reshow_list())
    
    thread = threading.Thread(target=task, daemon=True)
    thread.start()

# ----- 双击事件处理 -----
def on_tree_double_click(event, tree):
    selection = tree.selection()
    if not selection:
        return
    item_id = selection[0]
    zuoye = tree.item_data.get(item_id)
    if not zuoye:
        return
    
    status = zuoye.get('isComplete')
    if status == 3:
        jsessionid = entry_var.get().strip()
        if not jsessionid or jsessionid == "点击输入粘贴的JSESSIONID":
            messagebox.showwarning("提示", "请先在页面10输入有效的JSESSIONID")
            return
        zuoye_id = zuoye.get("id")
        user_zuoyes = zuoye.get("userZuoyes", [])
        if not user_zuoyes:
            messagebox.showerror("错误", "无法获取userZuoyeId")
            return
        user_zuoye_id = user_zuoyes[0].get("id")
        global current_zuoye_name
        current_zuoye_name = zuoye.get("name", "未知作业")
        loading = tk.Toplevel(root)
        loading.title("加载中")
        loading.geometry("300x100+{}+{}".format(root.winfo_x()+350, root.winfo_y()+250))
        tk.Label(loading, text="正在加载作业详情...", font=("微软雅黑", 14)).pack(expand=True)
        loading.update()
        def task():
            fetch_zuoye_detail_thread(zuoye_id, user_zuoye_id, jsessionid)
            loading.destroy()
        thread = threading.Thread(target=task, daemon=True)
        thread.start()
    elif status in [0, 1]:  # 未完成作业
        jsessionid = entry_var.get().strip()
        if not jsessionid or jsessionid == "点击输入粘贴的JSESSIONID":
            messagebox.showwarning("提示", "请先在页面10输入有效的JSESSIONID")
            return
        zuoye_id = zuoye.get("id")
        user_zuoyes = zuoye.get("userZuoyes", [])
        if not user_zuoyes:
            messagebox.showerror("错误", "无法获取userZuoyeId")
            return
        user_zuoye_id = user_zuoyes[0].get("id")
        
        # 保存作业ID，供AI使用
        global current_zuoye_id_for_ai, current_user_zuoye_id_for_ai
        current_zuoye_id_for_ai = zuoye_id
        current_user_zuoye_id_for_ai = user_zuoye_id
        
        show_page(13)  # 跳转到AI选择页

tree_all.bind("<Double-1>", lambda e: on_tree_double_click(e, tree_all))
tree_chinese.bind("<Double-1>", lambda e: on_tree_double_click(e, tree_chinese))
tree_math.bind("<Double-1>", lambda e: on_tree_double_click(e, tree_math))
tree_english.bind("<Double-1>", lambda e: on_tree_double_click(e, tree_english))



def cleanup_previous_pages():
    """销毁 page1~page11，释放 GIF 动画、图片等资源"""
    global previous_pages_cleaned, page1, page2, page3, page4, page5, page6, page7, page8, page9, page10, page11
    global show_leftimage_page1,show_page2_gongchuangtupian1,show_page2_gongchuangtupian2,show_page2_gongchuangtupian3,show_page2_gongchuangtupian4,show_page2_gongchuangtupian4,show_page2_gongchuangtupian4,show_page2_mader_photo_name,show_page3_lindangsign_left,show_page3_schoolsign_right,show_page4_liulanqisign_middle
    if previous_pages_cleaned:
        return

    # 销毁页面 Frame
    pages_to_destroy = [page1, page2, page3, page4, page5, page6, page7, page8, page9, page10, page11]
    for p in pages_to_destroy:
        try:
            if p.winfo_exists():
                p.destroy()
        except:
            pass

    # 置空全局图片变量，帮助垃圾回收
    show_leftimage_page1 = show_page2_gongchuangtupian1 = show_page2_gongchuangtupian2 = show_page2_gongchuangtupian3 = show_page2_gongchuangtupian4 = show_page2_gongchuangtupian4 = show_page2_gongchuangtupian4 = show_page2_mader_photo_name = show_page3_lindangsign_left = show_page3_schoolsign_right = show_page4_liulanqisign_middle = None

    # 强制垃圾回收
    gc.collect()
    previous_pages_cleaned = True
    print(" 已清理前面页面资源")



def on_page12_map(event):
    cleanup_previous_pages()   # 首次显示时清理前面页面
    reshow_list()

page12.bind("<Map>", on_page12_map)

# ----- 配置Treeview的紫色主题 -----
style = ttk.Style()
style.theme_use('clam')
style.configure("Treeview.Heading", background="#B03DC5", foreground="white", font=("微软雅黑", 11, "bold"))
style.map("Treeview.Heading", background=[("active", "#D98CE7")])
style.configure("Treeview", background="white", foreground="black", rowheight=25, fieldbackground="white", font=("微软雅黑", 10))
style.map("Treeview", background=[("selected", "#B03DC5")], foreground=[("selected", "white")])
style.configure("Vertical.TScrollbar", background="#ED94CE", arrowcolor="white")
style.configure("Horizontal.TScrollbar", background="#ED94CE", arrowcolor="white")




DOUBAO_API_KEY = ""
DEEPSEEK_API_KEY = ""

# ====================== page13 选择AI页面 ======================
page13 = tk.Frame(root, bg="#ED94CE")

label_title = tk.Label(
    page13,
    text="请选择你想使用的AI",
    font=("微软雅黑", 24, "bold"),
    bg="#ED94CE",
    fg="#F11477"
)
label_title.pack(pady=50)

#豆包AI
def open_doubao_api():
    api_win = tk.Toplevel(page13)
    api_win.title("")
    api_win.geometry("500x220")
    api_win.config(bg="#ED94CE")
    api_win.overrideredirect(True)

    api_win.update_idletasks()
    x = (api_win.winfo_screenwidth() - 500) // 2
    y = (api_win.winfo_screenheight() - 220) // 2
    api_win.geometry(f"500x220+{x}+{y}")

    tk.Label(api_win, text="请输入豆包AI API密钥", font=("微软雅黑", 14), bg="#ED94CE", fg="white").pack(pady=20)

    entry = tk.Entry(api_win, font=("微软雅黑", 12), width=32)
    placeholder = "请输入你的API密钥"
    entry.insert(0, placeholder)
    entry.config(fg="grey")
    entry.pack(pady=5)

    def on_focus_in(event):
        if entry.get() == placeholder:
            entry.delete(0, tk.END)
            entry.config(fg="black")
    entry.bind("<FocusIn>", on_focus_in)

    def save_doubao_api():
        global DOUBAO_API_KEY
        user_input = entry.get().strip()
        if user_input == "" or user_input == placeholder:
            messagebox.showwarning("提示", "请输入有效的API密钥！")
            return
        DOUBAO_API_KEY = user_input
        api_win.destroy()
        # 直接调用 AI 处理（不再跳转 page16）
        threading.Thread(target=fetch_first_question_and_call_ai, args=(DOUBAO_API_KEY, "doubao"), daemon=True).start()
        # 显示一个加载提示
        loading = tk.Toplevel(root)
        loading.title("处理中")
        loading.geometry("300x100")
        tk.Label(loading, text="正在调用 AI 并提交答案...", font=("微软雅黑", 14)).pack(expand=True)
        # 5 秒后自动关闭
        root.after(5000, loading.destroy)

    tk.Button(api_win, text="确定", font=("微软雅黑", 12),
              bg="#F11477", fg="white", width=10,
              command=save_doubao_api).pack(pady=18)
btn_doubao = RoundedButton(
    page13, text="豆包AI(图文)", radius=66, width=260, height=66,
    bg="#ED94CE", highlightthickness=0, command=open_doubao_api
)
btn_doubao.pack(pady=10)

# DeepSeekAI
def open_deepseek_api():
    api_win = tk.Toplevel(page13)
    api_win.title("")
    api_win.geometry("500x220")
    api_win.config(bg="#ED94CE")
    api_win.overrideredirect(True)

    # 居中窗口
    api_win.update_idletasks()
    x = (api_win.winfo_screenwidth() - 500) // 2
    y = (api_win.winfo_screenheight() - 220) // 2
    api_win.geometry(f"500x220+{x}+{y}")

    tk.Label(api_win, text="请输入DeepSeekAI API密钥", font=("微软雅黑", 14), bg="#ED94CE", fg="white").pack(pady=20)

    entry = tk.Entry(api_win, font=("微软雅黑", 12), width=32)
    placeholder = "请输入你的API密钥"
    entry.insert(0, placeholder)
    entry.config(fg="grey")
    entry.pack(pady=5)

    def on_focus_in(event):
        if entry.get() == placeholder:
            entry.delete(0, tk.END)
            entry.config(fg="black")
    entry.bind("<FocusIn>", on_focus_in)

    def save_deepseek_api():
        global DEEPSEEK_API_KEY
        user_input = entry.get().strip()
        if user_input == "" or user_input == placeholder:
            messagebox.showwarning("提示", "请输入有效的API密钥！")
            return
        DEEPSEEK_API_KEY = user_input
        api_win.destroy()

        # 显示加载提示
        loading = tk.Toplevel(root)
        loading.title("处理中")
        loading.geometry("300x100")
        tk.Label(loading, text="正在调用 AI 并提交答案...", font=("微软雅黑", 14)).pack(expand=True)
        root.after(5000, loading.destroy)  # 5秒后自动关闭

        # 启动AI处理线程
        threading.Thread(target=fetch_first_question_and_call_ai, args=(DEEPSEEK_API_KEY, "deepseek"), daemon=True).start()

    tk.Button(api_win, text="确定", font=("微软雅黑", 12),
              bg="#F11477", fg="white", width=10,
              command=save_deepseek_api).pack(pady=18)
btn_deepseek = RoundedButton(
    page13, text="DeepSeekAI(文字)", radius=66, width=260, height=66,
    bg="#ED94CE", highlightthickness=0, command=open_deepseek_api
)
btn_deepseek.pack(pady=10)
def call_doubao_api(api_key, content_parts):
    """调用豆包 API，content_parts 是符合 OpenAI 格式的列表"""
    url = "https://ark.cn-beijing.volces.com/api/v3/chat/completions"  
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "doubao-vision-pro",  
        "messages": [{"role": "user", "content": content_parts}],
        "max_tokens": 50
    }
    try:
        resp = requests.post(url, headers=headers, json=payload, timeout=60)
        resp.raise_for_status()
        result = resp.json()
        return result["choices"][0]["message"]["content"].strip()
    except Exception as e:
        print(f"豆包调用失败: {e}")
        return None

def call_deepseek_api(api_key, content_parts):
    """调用 DeepSeek API，同上"""
    url = "https://api.deepseek.com/v1/chat/completions"  
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "deepseek-chat",
        "messages": [{"role": "user", "content": content_parts}],
        "max_tokens": 50
    }
    try:
        resp = requests.post(url, headers=headers, json=payload, timeout=60)
        resp.raise_for_status()
        result = resp.json()
        return result["choices"][0]["message"]["content"].strip()
    except Exception as e:
        print(f"DeepSeek调用失败: {e}")
        return None


def is_image_url(url):
    """判断是否为图片链接，支持简书公式链接"""
    if not url or not url.startswith("http"):
        return False
    # 检查常见图片扩展名
    ext = os.path.splitext(urlparse(url).path)[1].lower()
    if ext in [".svg", ".png", ".jpg", ".jpeg", ".gif", ".bmp", ".tiff"]:
        return True
    # 检查简书公式链接
    if "math.jianshu.com" in url and "/math?formula=" in url:
        return True
    return False


def split_text_and_images(text):
    """
    将一段混合文本（如 "选项A https://xx.svg 继续"）拆分为列表：
    [("text", "选项A "), ("img", "https://xx.svg"), ("text", " 继续")]
    """
    # 简单的正则匹配URL
    url_pattern = r'(https?://[^\s]+)'
    parts = re.split(url_pattern, text)
    
    result = []
    for part in parts:
        if not part: continue
        if re.match(url_pattern, part) and is_image_url(part):
            result.append(("img", part))
        else:
            # 如果前面也是text，合并它（可选优化）
            if result and result[-1][0] == "text":
                result[-1] = ("text", result[-1][1] + part)
            else:
                result.append(("text", part))
    return result



def download_jianshu_formula(url, svg_data=None):
    """
    下载简书数学公式（SVG格式）并转换为 PIL Image 对象
    如果传入 svg_data 则直接使用该数据，否则从 url 下载
    """
    try:
        if svg_data is None:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
            response = requests.get(url, timeout=10, headers=headers)
            response.raise_for_status()
            svg_data = response.content

        # 使用 cairosvg 将 SVG 转换为 PNG 数据
        import cairosvg
        from io import BytesIO
        png_data = cairosvg.svg2png(
            bytestring=svg_data,
            output_width=200,   # 可根据需要调整输出宽度
            output_height=60     # 高度会自动按比例调整，但指定一个基础值有助于控制大小
        )
        img = Image.open(BytesIO(png_data))
        return img
    except ImportError:
        print(" 请安装 cairosvg 以显示数学公式：pip install cairosvg")
        return None
    except Exception as e:
        print(f"下载简书公式失败：{url} → {e}")
        return None



def download_image(url):
    """
    下载图片，支持普通图片（PNG、JPG等）和简书公式（SVG）
    如果 URL 是简书公式或返回的内容为 SVG，则自动转换为 PNG 后返回 PIL Image 对象
    """
    try:
        # 1. 特殊处理简书公式链接
        if "math.jianshu.com" in url and "/math?formula=" in url:
            return download_jianshu_formula(url)

        # 2. 普通图片下载
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get(url, timeout=10, headers=headers)
        response.raise_for_status()

        # 检查返回的内容类型，可能是 image/svg+xml
        content_type = response.headers.get('content-type', '').lower()
        if 'image/svg+xml' in content_type or response.text.strip().startswith('<svg'):
            # 如果返回的是 SVG 内容，调用简书处理函数（复用逻辑）
            return download_jianshu_formula(url, response.content)

        # 否则作为普通图片打开
        from io import BytesIO
        img = Image.open(BytesIO(response.content))
        return img

    except Exception as e:
        print(f"下载图片失败：{url} → {e}")
        return None

def extract_json_from_response(text):
    """
    从可能包含非JSON内容的响应中提取并解析JSON对象。
    """
    if not text:
        return None
    text = text.strip()
    try:
        # 第一次尝试：直接按标准JSON解析
        return json.loads(text)
    except json.JSONDecodeError:
        pass
    # 智能提取：用正则表达式查找 { ... } 格式的内容（强行找JSON）
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
            print(f" JSON二次解析失败: {e}")
            error_pos = e.pos
            start = max(0, error_pos - 50)
            end = min(len(json_str), error_pos + 50)
            print(f"   错误位置附近: ...{json_str[start:end]}...")
    return None




def save_user_answer(jsessionid, user_zuoye_id, zuoye_qest_id, answer_content):
    """提交文本答案（用于 AI 答案）"""
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
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }

    session = requests.Session()
    session.verify = False
    session.cookies.set("JSESSIONID", jsessionid, domain="base.bestsch.com", path="/BschZncp2")
    session.cookies.set("currentrole", CURRENT_ROLE, domain="base.bestsch.com", path="/BschZncp2")

    data = {
        "userZuoyeId": user_zuoye_id,
        "zuoyeQestId": zuoye_qest_id,
        "answer": answer_content
    }
    try:
        resp = session.post(
            "https://base.bestsch.com/BschZncp2/api/saveUserAnswerRecordNew",
            data=data, headers=HEADERS, timeout=20, verify=False
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


def fetch_first_question_and_call_ai(api_key, ai_type):
    """获取第一题详情，调用 AI，提交答案，然后返回列表"""
    global current_ai_answer, current_zuoye_detail

    jsessionid = entry_var.get().strip()
    if not jsessionid or jsessionid == "点击输入粘贴的JSESSIONID":
        root.after(0, lambda: messagebox.showwarning("提示", "请先输入有效的JSESSIONID"))
        root.after(0, lambda: show_page(12))
        return

    try:
        # 1. 获取第一题详情（复用之前保存的作业ID）
        session = requests.Session()
        session.verify = False
        session.cookies.set("JSESSIONID", jsessionid, domain="base.bestsch.com", path="/BschZncp2")
        CURRENT_ROLE = "%7B%22childId%22:0,%22roleId%22:3,%22schId%22:865%7D"
        session.cookies.set("currentrole", CURRENT_ROLE, domain="base.bestsch.com", path="/BschZncp2")

        headers = {
            "Accept": "application/json, text/plain, */*",
            "currentrole": CURRENT_ROLE,
            "User-Agent": "Mozilla/5.0"
        }

        detail_url = "https://base.bestsch.com/BschZncp2/api/FindUserZuoye2"
        params = {"zuoyeId": current_zuoye_id_for_ai, "userZuoyeId": current_user_zuoye_id_for_ai}
        resp = session.get(detail_url, params=params, headers=headers, timeout=15)
        data = resp.json()
        if data.get("code") != 0:
            raise Exception("获取详情失败")

        q_list = data.get("data", {}).get("zuoyeQestionList", [])
        if not q_list:
            raise Exception("该作业无题目")

        # 2. 解析第一题（包含图片URL）
        first_q = extract_question_info(q_list[0])  
        current_zuoye_detail = [first_q]

        # 3. 构建带图片的 prompt（按 OpenAI Vision 格式）
        content_parts = []

        # 处理题干中的文本和图片
        title = first_q.get('title', '')
        parts = split_text_and_images(title)  
        for typ, text_or_url in parts:
            if typ == "text":
                content_parts.append({"type": "text", "text": text_or_url})
            else:  # 图片
                img = download_image(text_or_url)
                if img:
                    import io, base64
                    buf = io.BytesIO()
                    img.save(buf, format="PNG")
                    img_b64 = base64.b64encode(buf.getvalue()).decode("utf-8")
                    content_parts.append({
                        "type": "image_url",
                        "image_url": {"url": f"data:image/png;base64,{img_b64}"}
                    })
                else:
                    content_parts.append({"type": "text", "text": "[图片加载失败]"})

        # 处理选项
        options = first_q.get('options', [])
        for opt in options:
            opt_parts = split_text_and_images(opt)
            for typ, text_or_url in opt_parts:
                if typ == "text":
                    content_parts.append({"type": "text", "text": text_or_url})
                else:
                    img = download_image(text_or_url)
                    if img:
                        buf = io.BytesIO()
                        img.save(buf, format="PNG")
                        img_b64 = base64.b64encode(buf.getvalue()).decode("utf-8")
                        content_parts.append({
                            "type": "image_url",
                            "image_url": {"url": f"data:image/png;base64,{img_b64}"}
                        })
                    else:
                        content_parts.append({"type": "text", "text": "[图片加载失败]"})

        # 4. 调用对应的 AI API
        if ai_type == "doubao":
            answer = call_doubao_api(api_key, content_parts)
        else:
            answer = call_deepseek_api(api_key, content_parts)

        if answer:
            current_ai_answer = answer
            # 5. 提交答案
            
            answer_to_submit = answer
            # 尝试转换为选项索引
            if first_q.get('options') and answer in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                idx = ord(answer) - ord('A')
                answer_to_submit = f"[{idx}]"
                answer_to_submit =format_fill_blank_answer()
            res = save_user_answer(jsessionid, current_user_zuoye_id_for_ai, first_q['id'], answer_to_submit)
            if res["success"]:
                root.after(0, lambda ans=answer: messagebox.showinfo("提示", f"AI 答案已提交：{ans}"))
            else:
                root.after(0, lambda msg=res["msg"]: messagebox.showerror("错误", f"提交失败：{msg}"))
        else:
            root.after(0, lambda: messagebox.showerror("错误", "AI 调用失败，未获得答案"))

    except Exception as e:
        print(f"AI处理异常: {e}")
        err_msg = str(e)
        root.after(0, lambda msg=err_msg: messagebox.showerror("错误", f"处理失败：{msg}"))
    finally:
        root.after(0, lambda: show_page(16))  # 返回列表




# ---------------------- 英语录音 ----------------------
def english_voice():
    """英语录音快速完成：获取第一题，生成音频并提交"""
    jsessionid = entry_var.get().strip()
    if not jsessionid or jsessionid == "点击输入粘贴的JSESSIONID":
        messagebox.showwarning("提示", "请先输入有效的JSESSIONID")
        show_page(12)
        return

    # 确保有当前作业ID
    if current_zuoye_id_for_ai is None or current_user_zuoye_id_for_ai is None:
        messagebox.showwarning("提示", "请先双击一个未完成作业进入本页面")
        show_page(12)
        return
    VOICE_LANG = "en"
    def text_to_speech_audio(text, lang=VOICE_LANG):
        """将文本转为音频文件（使用 pyttsx3 离线引擎）"""
        if not text:
            raise ValueError("朗读文本不能为空")
        # 使用全局临时文件夹
        temp_folder = DOWNLOAD_FOLDER
        os.makedirs(temp_folder, exist_ok=True)
        unique_name = f"tts_{os.urandom(4).hex()}.wav"
        temp_path = os.path.join(temp_folder, unique_name)

        def generate():
            engine = GLOBAL_TTS_ENGINE
            engine.save_to_file(text, temp_path)
            engine.runAndWait()

        t = threading.Thread(target=generate, daemon=True)
        t.start()
        t.join()  # 等待生成完成
        print(f"音频生成完成：{temp_path}")
        return temp_path


    def submit_audio_answer(jsessionid, user_zuoye_id, zuoye_qest_id, audio_path):
        """提交音频答案（WAV 格式）"""
        if not os.path.exists(audio_path):
            return {"success": False, "msg": "音频文件不存在"}

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
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        }

        session = requests.Session()
        session.verify = False
        session.cookies.set("JSESSIONID", jsessionid, domain="base.bestsch.com", path="/BschZncp2")
        session.cookies.set("currentrole", CURRENT_ROLE, domain="base.bestsch.com", path="/BschZncp2")

        try:
            with open(audio_path, 'rb') as f:
                files = {"file": (os.path.basename(audio_path), f, "audio/wav")}
                data = {
                    "userZuoyeId": user_zuoye_id,
                    "zuoyeQestId": zuoye_qest_id,
                    "answerType": "2",
                    "answer": ""
                }
                resp = session.post(
                    "https://base.bestsch.com/BschZncp2/api/saveUserAnswerRecordNew",
                    data=data, files=files, timeout=30, verify=False
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
            # 提交后删除临时音频文件
            try:
                os.remove(audio_path)
            except:
                pass

    # 在后台线程中处理
    def task():
        try:
            # 1. 获取第一题详情
            session = requests.Session()
            session.verify = False
            session.cookies.set("JSESSIONID", jsessionid, domain="base.bestsch.com", path="/BschZncp2")
            CURRENT_ROLE = "%7B%22childId%22:0,%22roleId%22:3,%22schId%22:865%7D"
            session.cookies.set("currentrole", CURRENT_ROLE, domain="base.bestsch.com", path="/BschZncp2")

            headers = {
                "Accept": "application/json, text/plain, */*",
                "currentrole": CURRENT_ROLE,
                "User-Agent": "Mozilla/5.0"
            }

            detail_url = "https://base.bestsch.com/BschZncp2/api/FindUserZuoye2"
            params = {"zuoyeId": current_zuoye_id_for_ai, "userZuoyeId": current_user_zuoye_id_for_ai}
            resp = session.get(detail_url, params=params, headers=headers, timeout=15)
            data = resp.json()
            if data.get("code") != 0:
                raise Exception("获取详情失败")

            q_list = data.get("data", {}).get("zuoyeQestionList", [])
            if not q_list:
                raise Exception("该作业无题目")

            first_q = extract_question_info(q_list[0])

            # 2. 提取纯文本（去除图片标记）
            read_text = re.sub(r'![^!]+!', '', first_q['title']).strip()
            if not read_text:
                raise Exception("题目中没有可朗读的文本")

            # 3. 生成音频
            audio_path = text_to_speech_audio(read_text)

            # 4. 提交音频
            res = submit_audio_answer(jsessionid, current_user_zuoye_id_for_ai, first_q['id'], audio_path)
            if res["success"]:
                root.after(0, lambda: messagebox.showinfo("提示", f"音频答案已提交：{read_text}"))
            else:
                root.after(0, lambda: messagebox.showerror("错误", f"提交失败：{res['msg']}"))
        except Exception as e:
            root.after(0, lambda: messagebox.showerror("错误", f"处理失败：{str(e)}"))
        finally:
            root.after(0, lambda: show_page(16))

    threading.Thread(target=task, daemon=True).start()
btn_english = RoundedButton(
    page13, text="英语录音快速完成", radius=66, width=260, height=66,
    bg="#ED94CE", highlightthickness=0, command=english_voice
)
btn_english.pack(pady=10)

# ---------------------- 返回 ----------------------
btn_back_to_page12 = RoundedButton(
    page13, text="返回作业列表", command=lambda: show_page(12),
    radius=66, width=200, height=66, bg="#ED94CE", highlightthickness=0
)
btn_back_to_page12.pack(pady=30)



page16 = tk.Frame(root, bg="#ED94CE")
label_page16 = tk.Label(
    page16,
    text="恭喜你把这个垃圾作业做完了",
    font=("微软雅黑", 26, "bold"),
    bg="#ED94CE",
    fg="#F11477",
    justify=tk.CENTER
)
label_page16.pack(expand=True)

btn_back_to_page13 = RoundedButton(
    page16, text="返回作业列表", command=lambda: show_page(12),
    radius=66, width=200, height=66, bg="#ED94CE", highlightthickness=0
)
btn_back_to_page13.pack(pady=20)





page15 = tk.Frame(root, bg="#ED94CE")
title_label15 = tk.Label(page15, text="作业统计看板", font=("Segoe Print", 40, "bold"), bg="#ED94CE", fg="#F11477")
title_label15.pack(pady=(20, 10))

toolbar15 = tk.Frame(page15, bg="#ED94CE")
toolbar15.pack(fill=tk.X, padx=20)

back_btn15 = RoundedButton(toolbar15, text="← 返回列表", command=lambda: show_page(12), 
                           radius=30, width=150, height=40, bg="#ED94CE", highlightthickness=0)
back_btn15.pack(side=tk.LEFT)

refresh_btn15 = RoundedButton(toolbar15, text="刷新", command=lambda: update_statistics(), 
                              radius=30, width=100, height=40, bg="#ED94CE", highlightthickness=0)
refresh_btn15.pack(side=tk.RIGHT)

canvas_frame = tk.Frame(page15, bg="#ED94CE")
canvas_frame.pack(expand=True, fill=tk.BOTH, padx=40, pady=20)

stats_canvas = tk.Canvas(canvas_frame, bg="white", highlightthickness=0)
stats_canvas.pack(expand=True, fill=tk.BOTH)

summary_label = tk.Label(page15, text="", font=("微软雅黑", 14), bg="#ED94CE", fg="#333333")
summary_label.pack(pady=10)

def update_statistics():
    stats_canvas.delete("all")
    
    if not zuoye_list_data:
        stats_canvas.create_text(400, 200, text="暂无作业数据", font=("微软雅黑", 20), fill="gray")
        summary_label.config(text="")
        return
    
    subjects = {"语文": {"total": 0, "completed": 0},
                "数学": {"total": 0, "completed": 0},
                "英语": {"total": 0, "completed": 0}}
    
    for zuoye in zuoye_list_data:
        teacher = zuoye.get('cid', '')
        status = zuoye.get('isComplete')
        if teacher == "253449":
            subject = "语文"
        elif teacher == "435534":
            subject = "数学"
        elif teacher == "153299":
            subject = "英语"
        else:
            continue
        subjects[subject]["total"] += 1
        if status == 3:
            subjects[subject]["completed"] += 1
    
    total_zuoye = sum(s["total"] for s in subjects.values())
    total_completed = sum(s["completed"] for s in subjects.values())
    completion_rate = (total_completed / total_zuoye * 100) if total_zuoye > 0 else 0
    
    summary_label.config(text=f"总作业数：{total_zuoye}  已完成：{total_completed}  未完成：{total_zuoye - total_completed}  完成率：{completion_rate:.1f}%")
    
    canvas_width = stats_canvas.winfo_width()
    canvas_height = stats_canvas.winfo_height()
    if canvas_width <= 1:
        canvas_width, canvas_height = 800, 400
    
    margin_left, margin_right = 100, 130
    margin_top, margin_bottom = 60, 90
    chart_width = canvas_width - margin_left - margin_right
    chart_height = canvas_height - margin_top - margin_bottom
    
    if chart_width < 200 or chart_height < 100:
        stats_canvas.create_text(canvas_width//2, canvas_height//2, 
                                 text="窗口太小，无法显示图表", font=("微软雅黑", 14), fill="gray")
        return
    
    max_count = max(max(s["total"], s["completed"]) for s in subjects.values()) or 1
    
    colors = {"total": "#B03DC5", "completed": "#4CAF50", "axis": "#333", "text": "#333"}
    
    stats_canvas.create_line(margin_left, canvas_height - margin_bottom,
                             canvas_width - margin_right, canvas_height - margin_bottom,
                             width=2, fill=colors["axis"])
    stats_canvas.create_line(margin_left, margin_top, margin_left, canvas_height - margin_bottom,
                             width=2, fill=colors["axis"])
    
    for i in range(max_count + 1):
        y = canvas_height - margin_bottom - (i / max_count) * chart_height
        stats_canvas.create_line(margin_left - 5, y, margin_left, y, width=1, fill=colors["axis"])
        stats_canvas.create_text(margin_left - 15, y, text=str(i), anchor="e",
                                 font=("Arial", 9), fill=colors["text"])
    
    n = len(subjects)
    bar_width = chart_width // (n * 2 + (n - 1))
    group_gap = bar_width // 2
    start_x = margin_left
    
    for i, (subject, data) in enumerate(subjects.items()):
        x_center = start_x + i * (2 * bar_width + group_gap) + bar_width
        
        total_height = (data["total"] / max_count) * chart_height
        x1_total = x_center - bar_width
        y1_total = canvas_height - margin_bottom - total_height
        x2_total = x_center
        y2_total = canvas_height - margin_bottom
        stats_canvas.create_rectangle(x1_total, y1_total, x2_total, y2_total,
                                      fill=colors["total"], outline="", tags="bar")
        stats_canvas.create_text((x1_total + x2_total)//2, y1_total - 10,
                                 text=str(data["total"]), font=("Arial", 10, "bold"), fill=colors["total"])
        
        completed_height = (data["completed"] / max_count) * chart_height
        x1_comp = x_center
        y1_comp = canvas_height - margin_bottom - completed_height
        x2_comp = x_center + bar_width
        y2_comp = canvas_height - margin_bottom
        stats_canvas.create_rectangle(x1_comp, y1_comp, x2_comp, y2_comp,
                                      fill=colors["completed"], outline="", tags="bar")
        stats_canvas.create_text((x1_comp + x2_comp)//2, y1_comp - 10,
                                 text=str(data["completed"]), font=("Arial", 10, "bold"), fill=colors["completed"])
        
        stats_canvas.create_text(x_center + bar_width//2, canvas_height - margin_bottom + 20,
                                 text=subject, font=("微软雅黑", 12, "bold"), fill="#333")
        
        if data["total"] > 0:
            rate = data["completed"] / data["total"] * 100
            stats_canvas.create_text(x_center + bar_width//2, canvas_height - margin_bottom + 40,
                                     text=f"{rate:.0f}%", font=("Arial", 10), fill="#666")
    
    legend_x = canvas_width - margin_right + 20
    legend_y = margin_top + 20
    stats_canvas.create_rectangle(legend_x, legend_y, legend_x+20, legend_y+15,
                                  fill=colors["total"], outline="")
    stats_canvas.create_text(legend_x+30, legend_y+7, text="总数", anchor="w",
                             font=("Arial", 10), fill=colors["text"])
    stats_canvas.create_rectangle(legend_x, legend_y+25, legend_x+20, legend_y+40,
                                  fill=colors["completed"], outline="")
    stats_canvas.create_text(legend_x+30, legend_y+32, text="已完成", anchor="w",
                             font=("Arial", 10), fill=colors["text"])
    
    stats_canvas.create_text(margin_left - 40, margin_top - 10, text="作业数量",
                             angle=90, font=("Arial", 10), fill=colors["text"])

def on_canvas_configure(event):
    update_statistics()

stats_canvas.bind("<Configure>", on_canvas_configure)
page15.bind("<Map>", lambda e: update_statistics())


cache_lock = threading.Lock()

def stop_current_audio():
    global audio_playing
    if pygame_initialized and pygame.mixer.music.get_busy():
        pygame.mixer.music.stop()
    audio_playing = False



def clear_temp_folder():
    if os.path.exists(DOWNLOAD_FOLDER):
        for f in os.listdir(DOWNLOAD_FOLDER):
            fp = os.path.join(DOWNLOAD_FOLDER, f)
            try:
                if os.path.isfile(fp):
                    os.remove(fp)
                elif os.path.isdir(fp):
                    shutil.rmtree(fp)
            except Exception as e:
                print(f"清理失败: {fp} → {e}")
        print(f" 已清空临时文件夹: {DOWNLOAD_FOLDER}")



def cleanup_zuoye_detail_memory():
    """清理作业详情页占用的内存：清空图片缓存、停止音频、清理临时文件、强制垃圾回收"""
    global image_cache, audio_playing, current_audio_path
    # 清空图片缓存
    with cache_lock:
        image_cache.clear()
    # 停止当前音频
    stop_current_audio()
    # 清理临时文件夹中的文件
    clear_temp_folder()
    # 强制垃圾回收
    gc.collect()
    print(" 作业详情内存已清理")






page14 = tk.Frame(root, bg="#ED94CE")
back_frame = tk.Frame(page14, bg="#ED94CE")
back_frame.pack(fill=tk.X, pady=10)
def back_to_list_and_clean():
    cleanup_zuoye_detail_memory()
    show_page(12)

btn_back_to_page12 = RoundedButton(back_frame, text=" 返回列表", command=back_to_list_and_clean, radius=30, width=150, height=40, bg="#ED94CE", highlightthickness=0)
btn_back_to_page12.pack(side=tk.LEFT, padx=20)
zuoye_title_label = tk.Label(page14, text="", font=("微软雅黑", 24, "bold"), bg="#ED94CE", fg="#F11477", wraplength=900)
zuoye_title_label.pack(pady=(0, 20))

# 主容器（使用Canvas+Frame实现可滚动的富文本区域）
main_container = tk.Frame(page14, bg="#ED94CE")
main_container.pack(expand=True, fill=tk.BOTH, padx=20, pady=10)

# 滚动区域设置
canvas = tk.Canvas(main_container, bg="white", highlightthickness=0)
scrollbar = tk.Scrollbar(main_container, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas, bg="white")

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# 修复鼠标滚轮
def _on_mousewheel(event):
    canvas.yview_scroll(int(-1*(event.delta/120)), "units")

canvas.bind("<MouseWheel>", _on_mousewheel)
scrollable_frame.bind("<MouseWheel>", _on_mousewheel)
def get_file_extension(url):
    """从 URL 中提取文件扩展名（忽略查询参数）"""
    if not url:
        return ""
    try:
        # 解析URL，获取路径部分
        parsed = urlparse(url)
        path = parsed.path
        # 获取扩展名
        ext = os.path.splitext(path)[1].lower()
        return ext
    except Exception as e:
        print(f"获取文件扩展名失败: {e}")
        return ""
#修改：show_zuoye_detail函数




def download_and_convert_svg(url):
    """下载SVG并转换为PNG（需安装cairosvg）"""
    try:
        import cairosvg
        import requests
        from io import BytesIO
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        png_data = cairosvg.svg2png(bytestring=response.content, output_height=120)
        img = Image.open(BytesIO(png_data))
        return img
    except ImportError:
        print("缺少cairosvg库，请安装：pip install cairosvg")
        return None
    except Exception as e:
        print(f"下载SVG失败：{url} → {e}")
        return None



def latex_to_image(latex_text, font_size=16, color="black", bg_color="white"):
    """
    将LaTeX公式转换为图片（使用在线API，无需本地安装LaTeX环境）
    :param latex_text: 原始LaTeX公式文本（如 r'\frac{x+4}{x^2-4}'）
    :return: PIL Image对象（失败返回None）
    """
    # 清理原始文本中的多余符号（如\{ \} 转义符）
    clean_latex = latex_text.replace("\\{", "{").replace("\\}", "}").replace("\\frac", "\\frac")
    
    # 在线公式渲染API（稳定且免费）
    api_url = f"https://latex.codecogs.com/png.latex?\\dpi{{150}}\\Large {clean_latex}"
    
    try:
        # 请求公式图片（忽略证书验证）
        response = requests.get(api_url, timeout=10, verify=False)
        response.raise_for_status()
        
        # 读取图片数据并返回PIL对象
        img_data = io.BytesIO(response.content)
        img = Image.open(img_data).convert("RGBA")
        return img
    except Exception as e:
        print(f" 公式渲染失败: {e}")
        return None





def render_formula_in_tkinter_custom(parent, latex_text, font=("微软雅黑", 11), bg="white", fg="#333"):
    """
    自定义样式的公式渲染函数（适配原render_rich_text的字体/背景/颜色）
    """
    # 转换公式为图片
    formula_img = latex_to_image(latex_text)
    if formula_img is None:
        # 渲染失败时显示原始文本（保留原样式）
        lbl = tk.Label(parent, text=latex_text, font=font, bg=bg, fg=fg, wraplength=750, justify="left")
        return lbl
    
    # 调整图片大小（适配行内显示）
    formula_img = formula_img.resize((int(formula_img.width*0.8), int(formula_img.height*0.8)), Image.Resampling.LANCZOS)
    tk_img = ImageTk.PhotoImage(formula_img)
    
    # 创建Label显示图片（保留原背景色）
    lbl = tk.Label(parent, image=tk_img, bg=bg)
    lbl.image = tk_img  # 保留引用，防止GC回收
    return lbl


def render_rich_content(parent, text, font=("微软雅黑", 11), bg="white", fg="#333"):
    """
    渲染混合内容：图片（!URL!）和 LaTeX 公式（\(...\) 或 \[...\]）
    """
    # 第一步：按图片标记分割（!URL!）
    segments = re.split(r'!([^!]+)!', text)
    for seg in segments:
        if not seg:
            continue
        if is_image_url(seg.strip()):
            # 处理图片
            img_label = tk.Label(parent, bg=bg)
            img_label.pack(side="left", anchor="w", pady=2, padx=1)

            def load_img(lbl, url):
                try:
                    if url.endswith(".svg"):
                        img = download_and_convert_svg(url)
                    else:
                        img = download_image(url)
                    if img:
                        # 缩放图片，保持行内高度
                        orig_w, orig_h = img.size
                        target_h = 25
                        ratio = target_h / orig_h
                        new_w = int(orig_w * ratio)
                        img = img.resize((new_w, target_h), Image.Resampling.LANCZOS)
                        photo = ImageTk.PhotoImage(img)
                        lbl.config(image=photo)
                        lbl.image = photo
                    else:
                        lbl.config(text="[图]", fg="red")
                except Exception:
                    lbl.config(text="[图]", fg="red")

            threading.Thread(target=load_img, args=(img_label, seg.strip()), daemon=True).start()
        else:
            # 第二步：对文本段按 LaTeX 标记分割
            latex_parts = re.split(r'(\\\(.*?\\\)|\\\[.*?\\\])', seg)
            for part in latex_parts:
                if not part:
                    continue
                if part.startswith(r'\(') and part.endswith(r'\)'):
                    # 内联公式
                    latex = part[2:-2]
                    render_formula_in_tkinter_custom(parent, latex, font, bg, fg).pack(side="left", anchor="w")
                elif part.startswith(r'\[') and part.endswith(r'\]'):
                    # 块公式
                    latex = part[2:-2]
                    render_formula_in_tkinter_custom(parent, latex, font, bg, fg).pack(side="left", anchor="w")
                else:
                    # 普通文本
                    tk.Label(parent, text=part, font=font, bg=bg, fg=fg,
                             wraplength=750, justify="left").pack(side="left", anchor="w")





def download_file(url, target_folder=DOWNLOAD_FOLDER):
    """下载文件到默认临时文件夹，返回本地路径"""
    try:
        resp = requests.get(url, stream=True, timeout=10)
        resp.raise_for_status()

        parsed = urlparse(url)
        filename = os.path.basename(parsed.path)
        if not filename:
            ext = mimetypes.guess_extension(resp.headers.get("content-type", "")) or ".bin"
            filename = f"temp_{int(time.time())}{ext}"

        local_path = os.path.join(target_folder, filename)
        with open(local_path, "wb") as f:
            for chunk in resp.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f" 已下载: {local_path}")
        return local_path
    except Exception as e:
        print(f" 下载失败: {e}")
        return None

def play_audio_directly(audio_path):
    """直接播放本地音频文件（只处理非PCM格式）"""
    global audio_playing, current_audio_path, pygame_initialized
    
    # 检查是否是PCM文件，如果是则返回
    ext = os.path.splitext(audio_path)[1].lower()
    if ext in ['.pcm', '.p']:
        print(f" 检测到PCM文件，应由download_and_play_audio处理")
        return
    
    try:
        if not pygame_initialized:
            try:
                pygame.mixer.quit()
                pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)
                pygame_initialized = True
                print(" Pygame音频初始化成功")
            except Exception as e:
                print(f" Pygame初始化失败: {e}")
                return
        
        stop_current_audio()
        
        if not os.path.exists(audio_path):
            print(f" 音频文件不存在: {audio_path}")
            return
        
        pygame.mixer.music.load(audio_path)
        pygame.mixer.music.play()
        audio_playing = True
        current_audio_path = audio_path
        print(f" 正在播放音频: {audio_path}")
        
        def monitor_audio():
            global audio_playing
            while pygame.mixer.music.get_busy():
                time.sleep(0.1)
            audio_playing = False
            current_audio_path = ""
            print(" 音频播放结束")
            # 播放完后删除临时文件
            try:
                if os.path.exists(audio_path) and audio_path.startswith(DOWNLOAD_FOLDER):
                    os.remove(audio_path)
                    print(f" 已删除临时文件: {audio_path}")
            except:
                pass
        
        threading.Thread(target=monitor_audio, daemon=True).start()
        
    except pygame.error as e:
        print(f" Pygame音频错误: {e}")
        audio_playing = False
    except Exception as e:
        print(f" 音频播放失败: {e}")
        audio_playing = False



def play_pcm_file(file_path):
    """使用 Pygame 播放 PCM 文件，自动适配参数"""
    global pygame_initialized
    if not pygame_initialized:
        print(" 无法播放：Pygame 音频未初始化")
        return

    # 读取 PCM 原始数据
    try:
        with open(file_path, 'rb') as f:
            pcm_data = f.read()
        file_size = len(pcm_data)
        print(f" PCM数据大小: {file_size} 字节")

        # 尝试多组 PCM 参数（覆盖常见场景）
        params_list = [
            (1, 2, 16000),   # 单声道 16位 16000Hz（最常用）
            (1, 2, 44100),   # 单声道 16位 44100Hz
            (1, 1, 8000),    # 单声道 8位 8000Hz
            (2, 2, 44100),   # 双声道 16位 44100Hz
        ]

        played = False
        for channels, sampwidth, framerate in params_list:
            try:
                print(f" 尝试: {channels}声道, {sampwidth*8}位, {framerate}Hz")
                
                # 计算有效时长，过滤无效参数
                frame_size = channels * sampwidth
                if frame_size == 0:
                    continue
                expected_frames = file_size // frame_size
                duration = expected_frames / framerate
                if duration <= 0.1 or duration > 30:
                    print(f" 无效时长({duration:.1f}秒)，跳过")
                    continue
                print(f"⏱ 预估时长: {duration:.1f}秒")

                # 生成临时 WAV 文件（Pygame 需容器格式）
                temp_wav = os.path.join(DOWNLOAD_FOLDER, f"temp_{int(time.time())}.wav")
                with wave.open(temp_wav, 'wb') as wav_f:
                    wav_f.setnchannels(channels)
                    wav_f.setsampwidth(sampwidth)
                    wav_f.setframerate(framerate)
                    wav_f.writeframes(pcm_data)

                # 停止当前播放，加载并播放新音频
                pygame.mixer.music.stop()
                pygame.mixer.music.load(temp_wav)
                pygame.mixer.music.play()
                print(f" Pygame 开始播放 PCM (WAV 临时文件: {temp_wav})")

                # 监控播放状态 + 延迟清理临时文件
                def monitor_and_cleanup():
                    start = time.time()
                    # 等待播放结束或超时
                    while pygame.mixer.music.get_busy():
                        time.sleep(0.1)
                        if time.time() - start > duration + 5:  # 超时保护
                            pygame.mixer.music.stop()
                            break
                    # 延迟删除临时文件（避免播放中删除）
                    time.sleep(2)
                    try:
                        os.remove(temp_wav)
                        print(f" 清理临时 WAV 文件: {temp_wav}")
                    except:
                        pass

                threading.Thread(target=monitor_and_cleanup, daemon=True).start()
                played = True
                break

            except Exception as e:
                print(f" 参数尝试失败: {e}")
                continue

        if not played:
            print(" 所有参数尝试失败，无法播放 PCM 文件")

    except Exception as e:
        print(f" PCM 文件播放异常: {e}")
        traceback.print_exc()


def download_and_play_audio(url, folder):
    """下载音频并播放 - 统一入口函数"""
    try:
        # 下载文件（同步）
        local_path = download_file(url, folder)
        if not local_path:
            print(f" 音频下载失败: {url}")
            return
        
        # 获取文件信息
        ext = os.path.splitext(local_path)[1].lower()
        
        # 判断是否为PCM文件
        is_pcm = ext in ['.pcm', '.p'] or 'pcm' in url.lower()
        
        if is_pcm:
            print(f" PCM文件，启动播放线程...")
            # PCM文件在新线程中播放
            thread = threading.Thread(target=play_pcm_file, args=(local_path,), daemon=True)
            thread.start()
        else:
            # 非PCM文件，用pygame播放
            print(f" 普通音频: {local_path}")
            def play_audio_thread():
                root.after(0, lambda: play_audio_directly(local_path))
            threading.Thread(target=play_audio_thread, daemon=True).start()
            
    except Exception as e:
        print(f" 音频处理失败: {e}")


def create_audio_play_button(parent, url):
    """创建音频播放按钮（无弹窗）- 统一使用 download_and_play_audio"""
    def play_audio():
        # 直接调用 download_and_play_audio，它会自动判断格式
        threading.Thread(target=download_and_play_audio, args=(url, DOWNLOAD_FOLDER), daemon=True).start()
    
    btn = RoundedButton(parent, text=" 播放音频", command=play_audio, 
                       radius=15, width=100, height=30, bg="#ED94CE", highlightthickness=0)
    return btn


def show_zuoye_detail():
    global current_zuoye_detail, current_zuoye_name
    # 清空可滚动区域
    for widget in scrollable_frame.winfo_children():
        widget.destroy()
    
    zuoye_title_label.config(text=current_zuoye_name)
    
    if not current_zuoye_detail:
        tk.Label(scrollable_frame, text="暂无题目数据", font=("微软雅黑", 14), bg="white").pack(pady=20)
        return
    
    # 遍历题目渲染
    for idx, q in enumerate(current_zuoye_detail, 1):
        # 题目大容器
        q_frame = tk.Frame(scrollable_frame, bg="white", padx=15, pady=15)
        q_frame.pack(fill="x", padx=10, pady=5, ipady=5)
        
        # 题号
        tk.Label(q_frame, text=f"【第{idx}题】", font=("微软雅黑", 12, "bold"), 
                 fg="#B03DC5", bg="white").pack(anchor="w")
        
        # 题干（富文本）
        title_container = tk.Frame(q_frame, bg="white")
        title_container.pack(fill="x", pady=5, padx=10)
        render_rich_content(title_container, q.get('title', ''), bg="white")
        
        # 选项（富文本）
        if q.get('options'):
            opt_frame = tk.Frame(q_frame, bg="white")
            opt_frame.pack(fill="x", pady=5, padx=10)
            tk.Label(opt_frame, text="选项：", font=("微软雅黑", 11, "bold"), bg="white").pack(anchor="w")
            
            for opt_idx, opt_text in enumerate(q['options']):
                opt_label = chr(ord('A') + opt_idx)
                #  修复：将选项字母和内容合并为一个字符串，整体渲染
                full_opt_text = f"{opt_label}. {opt_text}"
                
                # 创建一个容器来容纳这个选项
                opt_line_container = tk.Frame(opt_frame, bg="white")
                opt_line_container.pack(anchor="w", fill="x", pady=1)
                
                # 使用 smart_render 渲染完整的选项文本（包含字母和内容）
                render_rich_content(opt_line_container, full_opt_text, bg="white")
        
        # 答案区域
        ans_frame = tk.Frame(q_frame, bg="white")
        ans_frame.pack(fill="x", pady=5, padx=10)
        if q.get('correct_answer'):
            tk.Label(ans_frame, text=f" 正确答案：{q['correct_answer']}", 
                     font=("微软雅黑", 11, "bold"), fg="green", bg="white").pack(anchor="w")
        
        # 解析（富文本）
        if q.get('explanation'):
            expl_frame = tk.Frame(q_frame, bg="white")
            expl_frame.pack(fill="x", pady=5, padx=10)
            tk.Label(expl_frame, text="【解析】", font=("微软雅黑", 11, "bold"), bg="white").pack(anchor="w")
            render_rich_content(expl_frame, q['explanation'], bg="white")
        
        # 媒体文件
        if q.get('media_urls'):
            media_frame = tk.Frame(q_frame, bg="white")
            media_frame.pack(fill="x", pady=5, padx=10)
            tk.Label(media_frame, text="【媒体文件】", font=("微软雅黑", 11, "bold"), bg="white").pack(anchor="w")
            
            btn_frame = tk.Frame(media_frame, bg="white")
            btn_frame.pack(anchor="w", pady=2)
            
            for media_url in q['media_urls']:
                ext = get_file_extension(media_url)
                
                if ext in ['.mp3', '.wav', '.ogg', '.m4a', '.pcm']:
                    btn = create_audio_play_button(btn_frame, media_url)
                    btn.pack(side="left", padx=5, pady=2)
                else:
                    btn = tk.Button(btn_frame, text="打开文件", font=("微软雅黑", 10),
                                    command=lambda u=media_url: webbrowser.open(u))
                    btn.pack(side="left", padx=5, pady=2)
        
        # 分隔线
        tk.Frame(q_frame, height=2, bg="#ED94CE").pack(fill="x", pady=15)
page14.bind("<Map>", lambda e: show_zuoye_detail())



show_page(1)
root.deiconify()
root.attributes('-topmost', True)
if __name__ == "__main__":
    try:
        root.mainloop()  
    except Exception as e:
        print(f" 程序异常退出: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)