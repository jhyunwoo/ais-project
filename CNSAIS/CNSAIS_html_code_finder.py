from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import time
import urllib
import pyautogui
import csv


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


driver = webdriver.Chrome()
url = 'https://student.cnsa.hs.kr/common/file/imgView?id=AF2021030957379'
driver.get(url)
driver.maximize_window()
action = ActionChains(driver)


driver.get("https://student.cnsa.hs.kr/common/file/imgView?id=AF2021030957379")
html = driver.page_source
time.sleep(2)
print(html.find('확인'))

if html.find('확인') == 718:
    driver.find_element_by_xpath('//*[@id="layerAlertOk"]/span').click()
    time.sleep(2)
    pyautogui.write('jhyunwoo')
    pyautogui.press('tab')
    pyautogui.write('CNS*gksrnr42')
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.moveTo(901, 674)
    pyautogui.click()
    time.sleep(3)
