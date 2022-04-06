from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import time
import urllib
import pyautogui
import csv

driver = webdriver.Chrome()
url = 'https://student.cnsa.hs.kr/login/userLogin'
driver.get(url)
driver.maximize_window()
action = ActionChains(driver)


time.sleep(2)
# 큰사넷 로그인
position = pyautogui.position()
pyautogui.write('jhyunwoo')
pyautogui.press('tab')
pyautogui.write('CNS*gksrnr42')
pyautogui.press('enter')
time.sleep(3)
pyautogui.moveTo(901, 674)
pyautogui.click()

for row in range(1, 999):

    a = str(int(row)+872)
    driver.get(
        'https://student.cnsa.hs.kr/common/file/imgView?id=AF2019030319' + a)
    time.sleep(1)

    html = driver.page_source

    if html.find('viewport') == 46:
        position = pyautogui.position()
        pyautogui.moveTo(929, 684)
        pyautogui.click(button='right')
        pyautogui.press('down')
        pyautogui.press('down')
        pyautogui.press('enter')
        time.sleep(1)
        row = str(row)
        row = row.zfill(3)
        pyautogui.write(str(row))
        pyautogui.press('enter')
        print('Download complete:', row)

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
