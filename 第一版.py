import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os
import time

root = tk.Tk()

def set_face():
    time_set = [0,8,12,30,45,56,72,80,90]
    val = tk.StringVar()
    val.set('0%')

    root.destroy()
    window = tk.Tk()

    width = 500
    height = 150

    window.geometry(f"{width}x{height}+{int((window.winfo_screenwidth()-width)/2)}+{int((window.winfo_screenheight()-height)/2)}")
    window.title("永捷系統科技 - 印表機驅動程式安裝")
    window.iconbitmap("Autoinstall\\a1vuc-fgxyp-001.ico")
    window.resizable(False, False)

    ip = tk.Label(window, text='處理中...', font=('Helvetica', '20'))
    ip.place(x=200, y=90)

    bar = ttk.Progressbar(window, mode='determinate', length=350)
    bar.place(x=75, y=50)

    for i in time_set:
        bar['value'] = i            # 每次迴圈執行時改變進度條進度
        val.set(f'{i}%')            # 每次迴圈執行時改變顯示文字
        window.update()               # 更新視窗內容 ( 很重要！ )
        time.sleep(1)

    os.system("AutoInstall\Canon5170.bat")

    bar['value'] = 100
    exit_but = tk.Button(window, text='完成', width=15, font=('Helvetica', '20'), command=window.destroy)
    exit_but.place(x=125, y=75)
    window.update()

    window.focus_force()

    window.mainloop()

width = 500
height = 400

root.title("永捷系統科技 - 印表機驅動程式安裝")
root.iconbitmap("Autoinstall\\a1vuc-fgxyp-001.ico")
root.resizable(False, False)

img = Image.open('Autoinstall\\未命名.png')
ad_img = ImageTk.PhotoImage(img)
ad = tk.Canvas(root, width=350, height=198)
ad.create_image(0, 0, anchor='nw', image=ad_img)   # 在 Canvas 中放入圖片
ad.place(x=75, y=50)

set_but = tk.Button(root, text='開始設定', width=15, font=('Helvetica', '20'), command=set_face)
set_but.place(x=125, y=260)

mylabel = tk.Label(root, text='Copyright © 永捷系統科技公司 版權所有', fg="gray")
mylabel.place(x=135, y=375)

root.geometry(f"{width}x{height}+{int((root.winfo_screenwidth()-width)/2)}+{int((root.winfo_screenheight()-height)/2)}")
root.mainloop()
