from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import time
import urllib
import pyautogui
import csv

driver = webdriver.Chrome(
    '/Users/jhyunwoo/Documents/Programing/05_AIS/chromedriver')
url = 'https://student.cnsa.hs.kr/login/userLogin'
driver.get(url)
driver.maximize_window()
action = ActionChains(driver)


# 큰사넷 로그인
position = pyautogui.position()
pyautogui.write('jhyunwoo')
pyautogui.press('tab')
pyautogui.write('CNS*gksrnr42')
pyautogui.press('enter')
time.sleep(3)
# pyautogui.moveTo(901, 674)
# pyautogui.click()
