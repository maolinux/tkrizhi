# -*- coding:UTF-8 -*-
from tkinter import *
from urllib import request
from selenium import webdriver
import io
from PIL import Image, ImageTk
win = Tk()
chaxun = input("请输入名字：")
driver = webdriver.PhantomJS(executable_path=r'C:\phantomjs-2.1.1-windows\bin\phantomjs.exe')
strcode = request.quote(chaxun.encode(encoding='gbk', errors='strict'))
path = "http://172.10.10.32/jspweb/contacts/index.do?realName=" + strcode + "&phone=&type=search"
driver.get(path)
driver.implicitly_wait(10)
i=1
photos = []
ximings = []
youxiangs = []
bumens = []
fenjis = []
while True:
    try:
        xpath = ".//*[@id='row']/tbody/tr[" + str(i) + "]/td[5]/img"
        xpath_ximing = ".//*[@id='row']/tbody/tr[" + str(i) + "]/td[1]"
        xpath_youxiang = ".//*[@id='row']/tbody/tr[" + str(i) + "]/td[2]"
        xpath_bumen = ".//*[@id='row']/tbody/tr[" + str(i) + "]/td[3]"
        xpath_fenji = ".//*[@id='row']/tbody/tr[" + str(i) + "]/td[4]"
        data = driver.find_element_by_xpath(xpath)
        data_ximing = driver.find_element_by_xpath(xpath_ximing)
        data_youxiang = driver.find_element_by_xpath(xpath_youxiang)
        data_bumen = driver.find_element_by_xpath(xpath_bumen)
        data_fenji = driver.find_element_by_xpath(xpath_fenji)
        ximing = data_ximing.text
        youxiang = data_youxiang.text
        bumen = data_bumen.text
        fenji = data_fenji.text
        ximings.append(ximing)
        youxiangs.append(youxiang)
        bumens.append(bumen)
        fenjis.append(fenji)
        photo = data.get_attribute('src')
        i = i + 1
        image_bytes = request.urlopen(photo).read()
        data_stream = io.BytesIO(image_bytes)
        pil_image = Image.open(data_stream)
        pil_image.thumbnail((50,100),Image.ANTIALIAS)
        #pil_image.show()        
        #pil_image = pil_image.resize((50,100),Image.ANTIALIAS)
        tk_image = ImageTk.PhotoImage(pil_image)
        photos.append(tk_image) 
    except:
        break
row = 0
Label(win,text="姓名").grid(row = row,column=0)
Label(win,text="邮箱").grid(row = row,column=1)
Label(win,text="部门").grid(row = row,column=2)
Label(win,text="分机").grid(row = row,column=3)
Label(win,text="图片").grid(row = row,column=4)
for e in fenjis:
    row = row + 1
    Label(win,text = e).grid(row=row,column=3)
row = 0
for d in bumens:
    row = row + 1
    Label(win,text = d).grid(row=row,column=2)
row = 0
for c in youxiangs:
    row = row + 1
    Label(win,text = c).grid(row=row,column=1)
row = 0
for b in ximings:
    row = row + 1
    Label(win,text = b).grid(row=row,column=0)
row = 0
for a in photos:
    row = row + 1
    Label(win, image = a).grid(row=row,column=4)
    #Label(win, image=i).pack()
win.mainloop()

'''
image_bytes = request.urlopen(image).read()
data_stream = io.BytesIO(image_bytes)
pil_image = Image.open(data_stream)
#pil_image.show()
tk_image = ImageTk.PhotoImage(pil_image)
Label(win, image=tk_image).pack()
win.mainloop()
'''