# coding=utf8
from time import sleep as sleep_

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.wait import WebDriverWait


class WebKey:
    # 打开浏览器
    def __init__(self, driver):
        # self.driver = webdriver.Chrome()
        self.driver = driver

    # 打开URL网址
    def url(self, url):
        self.driver.get(url)

    # 元素定位
    def location(self, key, value):
        return self.driver.find_element(key, value)

    # 定位到指定元素，并使用红色的框圈住定位到的元素
    def location_list(self, element_list):
        self.scroll_to(element_list[0], element_list[1])
        self._locator_station(self.location(element_list[0], element_list[1]))
        return self.location(element_list[0], element_list[1])

    # 点击
    def click(self, element_list):
        self.location_list(element_list).click()

    # 输入
    def input(self, element_list, value):
        self.location_list(element_list).send_keys(value)

    # 修改文本框数据
    def input_modify(self, element_list, value):
        el = self.location_list(element_list)
        el.clear()
        el.send_keys(value)

    # 鼠标悬浮
    def hover(self, element_list):
        ActionChains(self.driver).move_to_element(self.location_list(element_list)).perform()

    # 圈住指定的元素
    def _locator_station(self, element):
        self.driver.execute_script(
            "arguments[0].setAttribute('style', arguments[1]);",
            element,
            "border: 3px solid blue;"  # 边框border:2px; red红色
        )

    # 强制等待
    def wait(self, value):
        sleep_(value)

    # 切换句柄
    def switch_handle(self, value):
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[value])

    # 切换iframe
    def iframe(self, element_list):
        self.driver.switch_to.frame(self.location_list(element_list))

    # 返回默认iframe
    def default_iframe(self):
        self.driver.switch_to.default_content()

    # 关闭句柄页
    def close(self):
        self.driver.close()

    # 关闭浏览器
    def quit(self):
        self.driver.quit()

    # 使浏览器页面到达指定元素
    def scroll_to(self, key, value):
        js = 'arguments[0].scrollIntoView()'
        self.driver.execute_script(js, self.location(key, value))

    # 显示等待
    def show_wait(self, element_list):
        WebDriverWait(self.driver, 10, 0.5).until(
            lambda el: self.location_list(element_list), "元素未找到")

    # 截图
    def screenshot(self, filename):
        self.driver.save_screenshot(filename)

    # 通过获取文本内容进行断言
    def assert_text(self, element_list, text):
        if self.location_list(element_list).text == text:
            return True
        else:
            return False

    # 通过判断元素是否存在进行断言
    def assert_exist(self, element_list):
        if self.location_list(element_list):
            return True
        else:
            return False
