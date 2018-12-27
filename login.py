
from selenium import webdriver
from PIL import Image, ImageEnhance
from selenium.webdriver.chrome.options import Options
import pytesseract
import sys


def main(username='sa', password='1', path='/Users/wzq/Desktop/chromedriver',
         screen='/Users/wzq/Desktop/printscreen.png'):
    url = "http://192.168.103.211/ict5/"
    # website address

    chrome_options = Options()
    # chrome_options.add_argument('--headless')                     set as headless or not
    # chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(executable_path=path, chrome_options=chrome_options)
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

    driver.save_screenshot(screen)

    location = imgElement.location                                  # Get security code position
    size = imgElement.size                                          # get the size of code
    pos = (int(location['x']), int(location['y']),
            int(location['x'] + size['width']),
              int(location['y'] + size['height']))                  # get the position as left, top, right, down

    i = Image.open(screen)            # open image
    frame4 = i.crop(pos)                                            # use crop get the code image
    frame4.save(screen)

    imageCode = Image.open(screen)
    sharp_img = ImageEnhance.Contrast(imageCode).enhance(2.0)
    sharp_img = ImageEnhance.Sharpness(sharp_img).enhance(3.0)
    # enhance contrast and sharpness for easy recognize

    sharp_img.load()
    sharp_img.save(screen)

    code = pytesseract.image_to_string(sharp_img).strip()

    codeElement.send_keys(code)

    driver.find_element_by_xpath("//span[text() = '登录']").click()
    driver.save_screenshot(screen)
    driver.close()


if __name__ == '__main__':
    if len(sys.argv) == 1:
        main()
    else:
        main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
