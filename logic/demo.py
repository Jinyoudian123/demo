from basic.keyword import WebKey
from selenium import webdriver

d = webdriver.Chrome()
wb = WebKey(d)
wb.url('https://www.baidu.com')
print(wb.getAttribute(['id', 'su'], 'value'))
