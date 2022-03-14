# coding=utf8
import pytest
from logic.taobao_page import TBpages


@pytest.fixture
def set_up(browser):
    tb = TBpages(browser)
    return tb


class Test_TB():
    @classmethod
    def set_up1(cls, set_up):
        cls.tb = set_up

    def test_login(self):
        self.tb.login()

    def test_shop(self):
        # tb = TBpages(browser)
        self.tb.search()


if __name__ == '__main__':
    pytest.main(['-s', 'test_baidu.py', '-v'])
