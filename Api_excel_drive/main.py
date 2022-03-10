# coding=utf8
import os
import pytest

from tool.read import send_email, read_excel

"""
    1、关键字类
    2、工具类
    3、测试数据
    4、测试用例类
    5、测试报告
    6、conftest.py
    7、main主入口
"""
# 测试用例文件
DATA_PATH = './test_data/test.xlsx'
# 发送邮件的信息
sender_user = '308759653@qq.com'
sender_pwd = 'dcvrrlkzxsesbhgd'
recevier = ['308759653@qq.com']
report_url = 'https://www.baidu.com'

if __name__ == '__main__':
    pytest.main(['--alluredir', './report/json', '--clean-alluredir'])
    # os.system('allure serve ./allure-results/json')
    # os.system('allure generate ./report/json -o ./report/report --clean')
    # send_email(sender_user, sender_pwd, recevier, report_url)
