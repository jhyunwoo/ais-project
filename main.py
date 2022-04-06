# 패키지 불러오기

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import pyautogui

# 크롬 드라이버 설정
s = Service('/Users/jhyunwoo/Documents/Programing/05_AIS/chromedriver')
driver = webdriver.Chrome(service=s)


def cnsa_net_log_in():
    # 큰사넷 진입
    driver.get('https://student.cnsa.hs.kr/login/userLogin')
    time.sleep(0.5)

    # 아이디 입력
    driver.find_element(
        By.XPATH, '//*[@id="loginId"]').click()
    driver.find_element(
        By.XPATH, '//*[@id="loginId"]').send_keys('jhyunwoo')

    # 비밀번호 입력
    driver.find_element(
        By.XPATH, '//*[@id="loginPw"]').click()
    driver.find_element(
        By.XPATH, '//*[@id="loginPw"]').send_keys('CNS*gksrnr42')

    # 로그인 버튼 클릭
    driver.find_element(
        By.XPATH, '//*[@id="userLoginDto"]/section/div[1]/fieldset/div/input').click()
    time.sleep(0.5)

    # 중복 로그인 페이지 해결
    html_source = driver.page_source
    if '다른 PC 또는 테블릿에 동일한 ID로 로그인되어 있습니다.' in html_source:
        driver.find_element(By.XPATH, '//*[@id="layerConfirmOk"]').click()


def image_finder():
    for i in range(380, 739, 1):
        i = str(i)
        driver.get(
            'https://student.cnsa.hs.kr/common/file/imgView?id=AF2021030957' + i)
        time.sleep(0.5)
        pyautogui.moveTo(600, 1200)
        time.sleep(0.5)
        pyautogui.click(button='right')
        pyautogui.press('down')
        pyautogui.press('down')
        pyautogui.press('enter')
        time.sleep(0.5)
        i = int(i)
        file_name = str(i - 379)
        pyautogui.write(file_name)
        time.sleep(0.5)
        pyautogui.press('enter')
        time.sleep(3)


cnsa_net_log_in()

image_finder()
