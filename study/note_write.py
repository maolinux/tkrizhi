# -*- conding:UTF-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import datetime
#读取日志和路径
now = datetime.datetime.now()
strtime = now.strftime("%Y-%m-%d.txt")
path = "F:\\工作文档\\常用文档\\工作任务\\" + strtime
try:
    rizhi = open(path,'r')
except:
    print('file is not exsist')
durizhi = rizhi.read()[1:]
rizhi.seek(0,0)
lines = len(rizhi.readlines())
rizhi.close()
#打开主页
browser = webdriver.Firefox()
browser.get('http://172.10.10.32/jspweb/login.jsp?system=diary')
assert '用户登录' in browser.title
browser.maximize_window()
#登录日志系统
loginName = browser.find_element_by_name('loginName')  # Find the login box
loginName.send_keys('mao_yaoguang')
#loginName.send_keys('mao_yaoguang' + Keys.RETURN)
password = browser.find_element_by_name('password')  #Find the password box
password.send_keys('275807981mao!')
#password.send_keys('275807981mao!' + Keys.RETURN)
iptb = browser.find_element_by_class_name('ipt-b')
iptb.click()

#点击我的日志和周报
assert '工作日志系统' in browser.title
browser.implicitly_wait(30)
#time.sleep(2)
browser.switch_to_frame('leftFrame')
textline = browser.find_element_by_link_text('我的日志和周报')
textline.click()

#点击填写日志
browser.switch_to_default_content()
browser.implicitly_wait(30)
#time.sleep(2)
browser.switch_to_frame('mainFrame')
tianxierizhi = browser.find_element_by_xpath(".//*[@id='normaltable']/tbody/tr/td[3]/input")
tianxierizhi.click()

#填写日志
browser.switch_to_default_content()
browser.implicitly_wait(30)
#time.sleep(2)
browser.switch_to_frame('lhgfrm_lhgdgId')
worktype2 = browser.find_element_by_id('worktype2')
worktype2.send_keys('日常工作')
usetime = browser.find_element_by_id('usetime')
usetime.send_keys('8')
noiframe = browser.find_element_by_xpath("html/body/div[2]/form/table[5]/tbody/tr[1]/td[2]/div/div[2]/iframe")
browser.switch_to_frame(noiframe)
tianx = browser.find_element_by_xpath('html/body')
wanc = [str(x) + ".完成" for x in range(lines) if x != 0 ]
b = ''
for a in wanc:
    b = b + a + '\n'
tianx.send_keys(Keys.DOWN + durizhi + (Keys.DOWN * 3) + b[:-1])
#提交
browser.switch_to_default_content()
browser.switch_to_frame('lhgfrm_lhgdgId')
tijiao = browser.find_element_by_xpath("html/body/div[2]/form/table[5]/tbody/tr[3]/td/input[1]")
tijiao.click()
browser.quit()