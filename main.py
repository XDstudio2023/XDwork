import os
from tkinter import messagebox
import tkinter as tk


root = tk.Tk()
root.title('XDwork1.0 office 特别版')
root.geometry('391x386')

def b1s():
    messagebox.showinfo('info','Excel启动成功')
    os.system('Excel.lnk')
def b2s():
    messagebox.showinfo('info','PowerPoint启动成功')
    os.system('PowerPoint.lnk')
def b3s():
    messagebox.showinfo('info','Word启动成功')
    os.system('Word.lnk')
def b4s():
    messagebox.showinfo('info','操作成功！')
    os.system('kms.exe')

b1 = tk.Button(root,command=b1s)
b2 = tk.Button(root,command=b2s)
b3 = tk.Button(root,command=b3s)
b4 = tk.Button(root,command=b4s)
b1['text'] = '打开 Excel'
b2['text'] = '打开 PowerPoint'
b3['text'] = '打开 Word'
b4['text'] = '激活office'
b1.pack()
b2.pack()
b3.pack()
b4.pack()

root.mainloop()
