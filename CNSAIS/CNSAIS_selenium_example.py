from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import time

driver = webdriver.Chrome()
url = 'https://google.com'
driver.get(url)
driver.maximize_window()
action = ActionChains(driver)


driver.find_element_by_css_selector('#gb_70').click()

action.send_keys('jhyunwoo0228').perform()

driver.find_element_by_css_selector('.CwaK9').click()

time.sleep(5)
driver.find_element_by_css_selector('.whsOnd zHQkBf').send_keys('apple')
driver.find_element_by_css_selector('.CwaK9').click()

driver.get('https://mail.google.com/mail/u/0/?ogb1#inbox')
time.sleep(2)

action.send_keys('jhyunwoo0228@gmail.com').key_down(Keys.TAB).perform()
