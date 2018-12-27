[{'domain': '192.168.103.211', 'httpOnly': False, 'name': '__ssid', 'path': '/',
  'secure': False, 'value': '2018.12.26f131b8f9-c60d-4fc0-8598-b9d2c70ec59d'},
 {'domain': '192.168.103.211', 'httpOnly': False, 'name': 'JSESSIONID',
  'path': '/ict5', 'secure': False, 'value': 'B0395E8764E40EC46FBF9B79C6B80BA3'}]

from selenium import webdriver
import time
driver= webdriver.Chrome()
driver.get("https://pan.baidu.com/")
login=driver.find_element_by_css_selector("#u1 > a.lb")
print login.get_attribute("innerHTML")
login.click()
time.sleep(5)
userlogin=driver.find_element_by_css_selector("#TANGRAM__PSP_10__footerULoginBtn")
userlogin.click()
cookieslist=[] #把获取到的cookie复制过来就行了
for cookie in cookieslist:  #遍历添加cookie
    driver.add_cookie(cookie)
time.sleep(5)
driver.get("https://www.baidu.com")
time.sleep(5)
