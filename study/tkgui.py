# -*- coding:UTF-8 -*-
from tkinter import *
import os
import datetime
#切换工作路径
os.chdir(r'F:\工作文档\常用文档\工作任务')
#strtime
now = datetime.datetime.now()
strtime = now.strftime("%Y-%m-%d.txt")
#button event
def updateButton():
    filewrite = open(path, 'a')
    var.set(var.get() + '\n' + e.get())
    filewrite.write('\n' + e.get())
    filewrite.close()
    e.set('')
#    print(entry.get())
def changeButton():
    rizhiread = open(path,'r')
    shuru = e2.get()
    shuru2 = e3.get()
    liebiao = rizhiread.readlines()
    liebiao[int(shuru)] = shuru2 + '\n'

    txt = ''
    for a in liebiao:
        txt = txt + a
    rizhiread.close()
    rizhiwrite = open(path,'w')
    rizhiwrite.write(txt)
    var.set(txt)
    e2.set('')
    e3.set('')
    rizhiwrite.close()
        
def updatanoteButton():
    os.system("note_write.py")
#main
path = "F:\\工作文档\\常用文档\\工作任务\\" + strtime

#file is exists?
if os.path.exists(path):
    fileopen = open(path,'r')
else:
    fileopen = open(path,'w+')
txt = fileopen.read()
root = Tk()
#label show work
var = StringVar()
w = Label(root, textvariable = var, justify='left').grid(row=0,columnspan=2)
var.set(txt)
fileopen.close()
#label show tianxie
label2 = Label(root,text='请填写日志：').grid(row=1)
#Entry
e = StringVar()
entry = Entry(root, textvariable = e)
entry.grid(row=1,column=1)
e.set('')
#button show work
Button(root, text='更新日志', command=updateButton).grid(row=1,column=2)

Label(root,text='修改行号：').grid(row=2,column=0)
e2 = StringVar()
entry2 = Entry(root, textvariable = e2)
entry2.grid(row=2,column=1)
e2.set('')

Label(root,text='修改内容：').grid(row=3,column=0)
e3 = StringVar()
entry3 = Entry(root, textvariable = e3)
entry3.grid(row=3,column=1)
e3.set('')
Button(root, text='修改日志',command=changeButton).grid(row=2,column=2,rowspan=2)
Button(root, text='刷新到内网',command=updatanoteButton).grid(row=4,column=0)
root.mainloop()