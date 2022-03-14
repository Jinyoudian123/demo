# coding=utf8
# import time
# from selenium import webdriver
# from basic.keyword import WebKey
# aa = ['id', 'kw']
# driver = webdriver.Chrome()
# wb = WebKey(driver)
# wb.url('https:www.baidu.com')
# wb.input_modify(aa, 123455)
# time.sleep(3)
# wb.input_modify(aa, 33333)
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep,ctime
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('https://www.baidu.com')
el = driver.find_element(By.ID, 'kw')
el.send_keys('seleniumm')
time.sleep(2)
el.send_keys(Keys.BACK_SPACE)
time.sleep(2)
el.send_keys(Keys.SPACE)
time.sleep(2)
el.send_keys('教程')
el.send_keys(Keys.CONTROL, 'a')
el.send_keys(Keys.CONTROL, 'x')
el.send_keys(Keys.CONTROL, 'v')
el.send_keys(Keys.ENTER)
driver.close()

