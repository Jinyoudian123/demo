# coding=utf8
import os
from selenium import webdriver
import pytest


@pytest.fixture()
def browser():
    os.popen(r'C:\Users\EDZ\Desktop\demo-UI\demo-UI\chrome.bat', buffering=2)
    # os.popen(r'C:\Users\admin\Downloads\demo-UI\chrome.bat')
    # os.system('chrome.exe --remote-debugging-port=9222')
    # options = webdriver.ChromeOptions()
    options = webdriver.ChromeOptions()
    # 忽略无用的日志
    # options.add_experimental_option('excludeSwitches', ['enable-logging'])
    # options.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])

    # 处理SSL证书错误问题
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')

    options.debugger_address = '127.0.0.1:9222'
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    return driver


@pytest.fixture()
def aa():
    return 123

#
# aa = browser()
# aa.get('https://www.baidu.com')
