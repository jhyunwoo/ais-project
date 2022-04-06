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

f = open('2021_CNSA_8기_명단.csv')
data = csv.reader(f)


for row in data:
    a = str(int(row[0])+379)
    name = str(row[1])
    driver.get(
        'https://student.cnsa.hs.kr/common/file/imgView?id=AF2021030957' + a)
    time.sleep(1)
    position = pyautogui.position()
    pyautogui.moveTo(929, 684)
    pyautogui.click(button='right')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.write(name)
    pyautogui.press('enter')
    print('Download complete:', name)
    if row[1] == '210701':
        driver.get('https://student.cnsa.hs.kr/')
        time.sleep(2)
        pyautogui.press('f5')
        print('relode is complete')
