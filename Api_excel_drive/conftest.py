# coding=utf8
import pytest
from main import DATA_PATH
from tool.read import read_excel

excel_data = read_excel(DATA_PATH)
Api_Infos = excel_data['ApiInfo']
print(Api_Infos)
globals_variable_datas = excel_data['globals_variable']


@pytest.fixture()
def globals_variable():
    globals_variable = {}
    for i in globals_variable_datas:
        globals_variable[i[0]] = i[1]
    return globals_variable


@pytest.fixture()
def environment_variable():
    globals_variable = {}
    return globals_variable


# @pytest.fixture()
def api_infos():
    Api_Infos.pop(0)
    return Api_Infos

