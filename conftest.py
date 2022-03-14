# coding=utf8
import os
from selenium import webdriver
import pytest


@pytest.fixture()
def browser():
    os.popen(r'C:\Users\EDZ\Desktop\demo-UI\demo-UI\chrome.bat', buffering=2)
    options = webdriver.ChromeOptions()

    # 处理SSL证书错误问题
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')

    options.debugger_address = '127.0.0.1:9222'
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    return driver

#
# aa = browser()
# aa.get('https://www.baidu.com')
