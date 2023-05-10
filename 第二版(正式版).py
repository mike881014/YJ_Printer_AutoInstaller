import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os
import time
import zipfile
import shutil
import subprocess
import getpass

root = tk.Tk()
user_name = getpass.getuser()

def unzip():
    zip_file = zipfile.ZipFile(r'AutoInstall\AutoInstall.zip')  # 檔案的路徑與檔案名
    zip_list = zip_file.namelist()  # 得到壓縮包里所有檔案
    for f in zip_list:
        zip_file.extract(f, f'C:\\Users\\{user_name}\\Documents', pwd="123456".encode("utf-8"))  # 回圈解壓檔案到指定目錄
    zip_file.close()  # 關閉檔案，必須有，釋放記憶體

def delete():
    os.remove(f"C:\\Users\\{user_name}\\Documents\\Canon5170.bat")
    shutil.rmtree(f"C:\\Users\\{user_name}\\Documents\\Driver")

def set_face():
    time_set = [45,56,61,70]

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

    for i in range(31):
        bar['value'] = i            # 每次迴圈執行時改變進度條進度
        val.set(f'{i}%')            # 每次迴圈執行時改變顯示文字
        window.update()               # 更新視窗內容 ( 很重要！ )
        time.sleep(0.001)

    unzip()

    for i in time_set:
        bar['value'] = i            # 每次迴圈執行時改變進度條進度
        val.set(f'{i}%')            # 每次迴圈執行時改變顯示文字
        window.update()               # 更新視窗內容 ( 很重要！ )
        time.sleep(0.01)

    subprocess.run(f"C:\\Users\\{user_name}\\Documents\\Canon5170.bat", shell=True)

    for i in range(20):
        bar['value'] = bar['value'] + i            # 每次迴圈執行時改變進度條進度
        val.set(f'{i}%')            # 每次迴圈執行時改變顯示文字
        window.update()               # 更新視窗內容 ( 很重要！ )
        time.sleep(0.01)

    delete()

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
