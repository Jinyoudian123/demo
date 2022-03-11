# coding=utf8
import json

from basic.keyword import WebKey
from selenium import webdriver


def aa():
    driver = webdriver.Chrome()
    wb = WebKey()
    wb.browser(driver)
    wb.url('https://www.baidu.com')
    wb.input(['id', 'kw'], '你好')
    wb.click(['id', 'su'])
    wb.wait(2)
    wb.A('../1.png')

if __name__ == '__main__':
    aa()