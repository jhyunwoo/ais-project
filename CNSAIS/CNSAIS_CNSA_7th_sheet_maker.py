from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import time
import clipboard
import urllib
import pyautogui
import csv
import gspread
from oauth2client.service_account import ServiceAccountCredentials

driver = webdriver.Chrome()
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


def relogin():
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


login()
time.sleep(5)

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    'cnsais-example-15b64aed76d8.json', scope)
gc = gspread.authorize(credentials)
gc1 = gc.open("gspread-test").worksheet('시트1')


for find in range(1, 380):

    find = find + 489
    find_url = 'https://student.cnsa.hs.kr/common/file/imgView?id=AF2020030384' + \
        str(find)
    driver.get(find_url)

    html = driver.page_source

    position = pyautogui.position()
    pyautogui.moveTo(929, 684)
    pyautogui.click(button='right')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('enter')
    time.sleep(5)
    result = clipboard.paste()
    gc1.update_acell('B1', result)

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
