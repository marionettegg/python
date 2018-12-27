#!/usr/bin/env python

from selenium import webdriver
from PIL import Image, ImageEnhance
from selenium.webdriver.chrome.options import Options
import time


def main(username='sa', password='1'):
    url = "http://192.168.103.211/ict5/"
    # website address

    chrome_options = Options()
    # chrome_options.add_argument('--headless')
    # chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(executable_path='/Users/wzq/Desktop/chromedriver', chrome_options=chrome_options)
    # Setting chrome as headless mode

    driver.implicitly_wait(30)
    driver.get(url)
    driver.maximize_window()

    userElement = driver.find_element_by_name("userName")

    passElement = driver.find_element_by_name("s_Pwd")

    codeElement = driver.find_element_by_name("s_Code")

    imgElement = driver.find_element_by_id("imgCode")

    userElement.clear()
    userElement.send_keys(username)
    passElement.clear()
    passElement.send_keys(password)
    codeElement.clear()
    time.sleep(10)

    driver.find_element_by_xpath("//span[text() = '登录']").click()
    time.sleep(5)
    cookies = driver.get_cookies()
    print (cookies)
    print(driver.title)
    title = driver.title  # 返回的title为unicode类型，下面比较时应该也应与unicode类型比较
    username = username.get_attribute("innerHTML")
    print(title)
    print(username)
    # 下面的代码是自己测试是否登录成功的
    driver.close()



if __name__ == "__main__":
    main()