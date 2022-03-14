# coding=utf-8

from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
import re
import os

options = webdriver.ChromeOptions()

# 处理SSL证书错误问题
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')

# 忽略无用的日志
options.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
driver = webdriver.Chrome(chrome_options=options)

size_Dict = driver.get_window_size()
driver.set_window_rect(x=1300, y=100, width=1250, height=1300)  # 设置浏览器的大小和位置
# driver.maximize_window()    # 最大化浏览器窗口
driver.implicitly_wait(20)  # 隐式等待。网页加载数据需要时间，智能化等待。

driver.get("https://www.amazon.co.jp")
time.sleep(3)
driver.close()

https://blog.csdn.net/feng542064/article/details/120073383

USB: usb_device_handle_win. cc:1049 Failed to read descriptor from node connection: 连到系统上的设备没有发挥作用。 (0x1F)

Registration URL fetching failed.