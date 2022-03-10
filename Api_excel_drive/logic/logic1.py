# coding=utf8
import re
from basics.key_word import ApiKey
from tool.read import sql_select
import allure

ak = ApiKey()


def excel_logic(api_info, globals_variable, environment_variable):
    # for api_info in api_infos:
    # if type(api_info[0]) is int:
    case_id = api_info[0]  # 用例编号
    case_name = api_info[1]  # 用例名称
    case_url = api_info[2]  # Url(接口地址)
    case_headers = api_info[3]  # Headers(请求头内容)
    case_method = api_info[4]  # 请求方式
    case_data = api_info[5]  # 请求参数
    assert_type = api_info[6]  # 断言方式
    rule = api_info[7]  # jsonpath语法
    expect = api_info[8]  # 预期结果
    set_variable = api_info[9]  # 响应中设置变量
    pre_db = api_info[10]  # 数据库前置判断
    pre_db_verify = api_info[11]  # 数据库前置结果确认
    after_db = api_info[12]  # 数据库后置判断
    after_db_verify = api_info[13]  # 数据库后置结果确认
    case_title = api_info[14]  # 用例标题

    # 1、所有变量的替换
    with allure.step('开始所有变量的替换'):
        # 1.1替换ulr中的变量
        with allure.step('开始替换ulr中的变量'):
            case_url = ak.sub_all_variable(case_url, globals_variable, environment_variable)
        # 1.2替换headers中的变量
        if case_headers:
            with allure.step('开始替换headers中的变量'):
                case_headers = ak.sub_all_variable(case_headers, globals_variable, environment_variable)
        # 1.3替换请求参数中的变量
        if case_data:
            with allure.step('开始替换请求参数中的变量'):
                case_data = ak.sub_all_variable(case_data, globals_variable, environment_variable)

    # 2、执行数据库前置内容
    if pre_db:
        try:
            if len(eval(pre_db)) == len(eval(pre_db_verify)):
                with allure.step('开始执行数据库前置内容'):
                    pre_db = eval(pre_db)
                    # 3、数据库前置内容校验
                    for i in pre_db:
                        for y in eval(pre_db_verify):
                            if i['no'] == y['no']:
                                with allure.step(f'执行no.{i["no"]}条前置数据库校验'):
                                    assert sql_select(i['sql']) == y['sql'], f'用例{case_id}前置数据库校验失败'
            else:
                with allure.step('前置数据库查询内容与校验内容数量不符,执行失败'):
                    raise KeyError(f'用例{case_id}前置数据库查询内容与校验内容数量不符,执行失败')
        except SyntaxError as e:
            with allure.step('前置数据库校验执行失败，查询内容或校验内容填写格式错误'):
                raise SyntaxError('查询内容或校验内容填写格式错误')
    # 4、发送接口请求
    with allure.step('发送接口请求'):
        if case_headers:
            case_headers = eval(case_headers)
            if case_data:
                case_data = eval(case_data)
                try:
                    response = getattr(ak, case_method)(url=case_url, headers=case_headers, json=case_data)
                except:
                    response = getattr(ak, case_method)(url=case_url, headers=case_headers, data=case_data)
            else:
                response = getattr(ak, case_method)(url=case_url, headers=case_headers)
        else:
            response = getattr(ak, case_method)(url=case_url)
    # 5、响应断言
    with allure.step('执行接口响应断言'):
        response_json = response.json()
        result = getattr(ak, assert_type)(response_json, expect, case_id, rule)
        print(f'接口{case_id}的响应为：', response_json)
        assert result == True, f'接口{case_id}响应断言失败'
    # 6、执行数据库后置内容
    if after_db:
        try:
            if len(eval(after_db)) == len(eval(after_db_verify)):
                with allure.step('开始执行数据库后置内容'):
                    after_db = eval(after_db)
                    # 3、数据库后置内容校验
                    for i in after_db:
                        for y in eval(after_db_verify):
                            if i['no'] == y['no']:
                                with allure.step(f'执行no.{i["no"]}条后置数据库校验'):
                                    assert sql_select(i['sql']) == y['sql'], f'用例{case_id}后置数据库校验失败'
            else:
                with allure.step('前置数据库查询内容与校验内容数量不符,执行失败'):
                    raise KeyError(f'用例{case_id}后置数据库查询内容与校验内容数量不符,执行失败')
        except SyntaxError as e:
            with allure.step('后置数据库校验执行失败，查询内容或校验内容填写格式错误'):
                raise SyntaxError('查询内容或校验内容填写格式错误')
    # 8、从响应中获取变量
    if set_variable:
        with allure.step('开始从响应中获取变量'):
            try:
                key_values = re.findall(r'set_variable\("(.+?)","(.+?)"\)', set_variable)
                for i in key_values:
                    environment_variable[i[0]] = ak.get_json_text(response_json, i[1])
            except Exception as e:
                print(f'接口{case_id}变量获取失败，错误信息为', e)
