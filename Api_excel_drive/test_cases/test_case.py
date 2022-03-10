# coding=utf8
import allure
import pytest
from conftest import api_infos  # conftest中的 api_info
from logic.logic1 import excel_logic

environment_variable = {}


@pytest.mark.parametrize('api_info', api_infos())
def test_1(api_info, globals_variable):
    allure.dynamic.title(api_info[14])
    allure.dynamic.feature(api_info[1])
    excel_logic(api_info, globals_variable, environment_variable)


if __name__ == '__main__':
    pytest.main(['-s'])
