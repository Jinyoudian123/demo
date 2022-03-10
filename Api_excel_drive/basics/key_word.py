# coding=utf8
import json
import re

import allure
import requests
from jsonpath import jsonpath as jsonpath_


class ApiKey():
    # post 请求
    @allure.step('发送post请求')
    def post(self, url, data=None, json=None, **kwargs):
        return requests.post(url, data=data, json=json, **kwargs)

    # get 请求
    @allure.step('发送get请求')
    def get(self, url, params=None, **kwargs):
        return requests.get(url=url, params=params, **kwargs)

    # 通过jsonpath 提取响应中的变量
    @allure.step('通过jsonpath提取响应中的变量')
    def get_json_text(self, response, rule):
        json_data = jsonpath_(response, rule)
        if json_data:
            return json_data[0]
        return json_data

    # 通过jsonpath进行断言
    @allure.step('通过jsonpath进行断言')
    def jsonpath(self, response, expect, case_id, rule):
        if expect is None:
            raise KeyError(f'用例{case_id}断言失败，预期结果为空')
        json_data = jsonpath_(response, rule)
        # print(json_data)
        if json_data:
            if len(json_data) == 1:
                result = json_data[0]
            else:
                expect = eval(expect)
                result = tuple(json_data)
        else:
            result = json_data
        if result == expect:
            return True
        else:
            return False

    # 通过全等进行断言
    @allure.step('通过全等进行断言')
    def equal(self, response, expect, case_id, rule=None):
        if expect is None:
            raise KeyError(f'用例{case_id}断言失败，预期结果为空')
        if response == eval(expect):
            return True
        else:
            return False

    # 通过字符串包含进行断言
    allure.step('通过字符串包含进行断言')

    def include(self, response, expect, case_id, rule=None):
        if expect is None:
            raise KeyError(f'用例{case_id}断言失败，预期结果为空')
        sun_response = str(response).replace("'", '"')
        if expect in sun_response:
            return True
        else:
            return False

    # 将全局变量替换成相应的值
    def _sub_global_variable(self, str_value, global_variable):
        """
        :param str_value: 整个字符串内容 （str）
        :param global_variable: 全局变量 （dict）
        :return: 返回替换后的的字符串内容 （str）
        """
        key = re.findall(r'get_global\${(.+?)}', str_value)
        after_sub_key = str_value
        for i in key:
            # 将所有匹配到的变量进行替换
            after_sub_key = re.sub(r"get_global\${(.+?)}", global_variable[i], after_sub_key, count=1)
        return after_sub_key

    def _sub_environment_variable(self, str_value, environment_variable):
        """
        :param str_value: 整个字符串内容 （str）
        :param environment_variable: 环境变量 （dict）
        :return: 返回替换后的的字符串内容 （str）
        """
        key = re.findall(r'get_variable\${(.+?)}', str_value)
        after_sub_key = str_value
        for i in key:
            # 将所有匹配到的变量进行替换
            after_sub_key = re.sub(r"get_variable\${(.+?)}", environment_variable[i], after_sub_key, count=1)
        return after_sub_key

    @allure.step('替换所有变量')
    def sub_all_variable(self, str_value, global_variable, environment_variable):
        """
        替换所有变量，包括环境变量和全局变量
        :rtype: object
        :param str_value: 整个字符串内容 （str）
        :param global_variable: 全局变量 （dict）
        :param environment_variable: 环境变量 （dict）
        :return:
        """
        after_value = self._sub_global_variable(str_value, global_variable)
        return self._sub_environment_variable(after_value, environment_variable)


if __name__ == '__main__':
    ak = ApiKey()
