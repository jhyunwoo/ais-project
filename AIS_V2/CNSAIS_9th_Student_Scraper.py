import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

# 크롬 드라이버 설정
s = Service('/Users/jhyunwoo/Documents/Programing/15_auto-selfcheck/chromedriver')
driver = webdriver.Chrome(service=s)

""" DEF AREA """

def get_webpage(page_link):  # 자가진단 웹페이지 띄우기
    driver.get(page_link)
    time.sleep(1)

def log_in(login_id, login_password):
    driver.find_element(By.XPATH, '//*[@id="loginId"]').send_keys(login_id)
    driver.find_element(By.XPATH, '//*[@id="loginPw"]').send_keys(login_password)
    driver.find_element(By.XPATH, '//*[@id="userLoginDto"]/section/div[1]/fieldset/div/input').click()
    time.sleep(1)
    html_source = driver.page_source
    if "다른" in html_source:
        driver.find_element(By.XPATH, '//*[@id="layerConfirmOk"]/span').click()

""" END DEF AREA """

get_webpage('https://student.cnsa.hs.kr/')

log_in('jhyunwoo', 'CNS*gksrnr42')

find = 0

progress = 2022010100000
    
for i in range(0, 99999, 1):    
    s = Service('/Users/jhyunwoo/Documents/Programing/15_auto-selfcheck/chromedriver')
    driver = webdriver.Chrome(service=s)
    url = "https://student.cnsa.hs.kr/common/file/imgView?id=AF" + str(progress)
    driver.get(url)
    progress = int(progress) + 300
    html = driver.page_source
    if "로그아웃 되었습니다." in html:
        driver.find_element(By.XPATH, '//*[@id="layerAlertOk"]/span').click()
        driver.find_element(By.XPATH, '//*[@id="loginPw"]').send_keys("CNS*gksrnr42")
        driver.find_element(By.XPATH, '//*[@id="userLoginDto"]/section/div[1]/fieldset/div/input').click()
        time.sleep(1)
    elif "style" in html:
        print(url)
    
