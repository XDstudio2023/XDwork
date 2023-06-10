# -*- coding:utf-8 -*-0from tkinter import messagebo
from tkinter import messagebox 
import tkinter as tk
import time
import os
import webbrowser
import sys
# 调用Tk()创建主窗口
root_window =tk.Tk()
# 给主窗口起一个名字，也就是窗口的名字
root_window.title('宇孟OS')
root_window.geometry('391x386')
#开启主循环，让窗口处于显示状态
def b1():
    messagebox.showinfo('info','操作成功!')
    time.sleep(1)
    sys.exit (0)
def b2():
    messagebox.showinfo('info','操作成功!')
    os.system(r'main.py')

    
b1 = tk.Button(root_window,command=b1,text='关机')
b2 = tk.Button(root_window,command=b2,text='office管理工具')
b1.pack()
b2.pack()
root_window.mainloop()