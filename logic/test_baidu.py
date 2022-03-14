# coding=utf8
import pytest
from logic.taobao_page import TBpages


# @pytest.fixture(scope='class')
# def set_up(browser):
#     tb = TBpages(browser)
#     return tb


class Test_TB():
    def test_login(self, browser):
        tb = TBpages(browser)
        tb.search()


if __name__ == '__main__':
    pytest.main(['-s', 'test_baidu.py', '-v'])
