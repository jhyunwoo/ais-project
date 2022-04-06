from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import time
import urllib
import pyautogui
import csv

driver = webdriver.Chrome("/Users/jhyunwoo/Documents/Programing/05_AIS/chromedriver")
url = 'https://student.cnsa.hs.kr/login/userLogin'
driver.get(url)
driver.maximize_window()
action = ActionChains(driver)


time.sleep(2)

# 큰사넷 로그인


def login():
    driver.get(url)
    position = pyautogui.position()
    pyautogui.write('jhyunwoo')
    pyautogui.press('tab')
    pyautogui.write('CNS*gksrnr42')
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.moveTo(901, 674)
    pyautogui.click()


login()
time.sleep(5)


progress = 30387406


for find in range(1 + progress, 999999999, 100):
    try:
        find = str(find)
        find = find.zfill(9)
        find_url = 'https://student.cnsa.hs.kr/common/file/imgView?id=AF2020' + find
        driver.get(find_url)

        html = driver.page_source
        if html.find('확인') == 718:
            driver.find_element_by_xpath(
                '//*[@id="layerAlertOk"]/span').click()
            time.sleep(10)
            pyautogui.write('CNS*gksrnr42')
            time.sleep(10)
            pyautogui.press('enter')
            time.sleep(10)
            pyautogui.moveTo(901, 674)
            pyautogui.click()
            time.sleep(10)
            print('complete task')

        if html.find('viewport') == 46:
            print(find_url)

    except:
        print(find)
        break
