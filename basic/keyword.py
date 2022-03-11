# coding=utf8
from time import sleep as sleep_

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait


class WebKey:
    # 打开浏览器
    def browser(self, driver):
        self.driver = webdriver.Chrome()
        # self.driver = driver

    # 打开URL网址
    def url(self, url):
        self.driver.get(url)

    # 元素定位
    def location(self, key, value):
        return self.driver.find_element(key, value)

    # 定位到指定元素，并使用红色的框圈住定位到的元素
    def location_list(self, element_list):
        self._locator_station(self.location(element_list[0], element_list[1]))
        return self.location(element_list[0], element_list[1])

    # 点击
    def click(self, element_list):
        self.location_list(element_list).click()

    # 输入
    def input(self, element_list, value):
        self.location_list(element_list).send_keys(value)

    # 鼠标悬浮
    def hover(self, element_list):
        ActionChains(self.driver).move_to_element(self.location_list(element_list)).perform()

    # 圈住指定的元素
    def _locator_station(self, element):
        self.driver.execute_script(
            "arguments[0].setAttribute('style', arguments[1]);",
            element,
            "border: 3px solid red;"  # 边框border:2px; red红色
        )

    # 强制等待
    def wait(self, value):
        sleep_(value)

    # 切换句柄
    def switch_handle(self, value):
        self.driver.switch_to.window(value)

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

    # 显示等待
    def show_wait(self, element_list):
        WebDriverWait(self.driver, 10, 0.5).until(
            lambda el: self.location_list(element_list), "元素未找到")

    def A(self,filename):
        # self.driver.save_screenshot(filename)
        self.driver.get_screenshot_as_file(filename)
