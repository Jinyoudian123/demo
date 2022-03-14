# coding=utf8
from selenium.webdriver import Keys

from basic.keyword import WebKey

# 登录页的信息
login_entrance = ['link text', '亲，请登录']
login_user = ['xpath', '//input[@name="fm-login-id"]']
login_pwd = ['xpath', '//input[@name="fm-login-password"]']
login_button = ['xpath', '//button[@type="submit"]']
# 首页搜索
home_page_search = ['id', 'q']
home_page_search_button = ['xpath', '//button[@type="submit"]']
select_goods = ['xpath', '//div[@class="items"][1]/div[5]//a']
# 商品页的选择
select_goods_type = ['xpath', '//div[@class="tb-sku"]//li[1]']
goods_page_num = ['xpath', '//input[@title="请输入购买量"]']
add_shopping_trolley = ['xpath', '//a[@id="J_LinkBasket"]']


class TBpages(WebKey):
    def login(self):
        # wb = WebKey()
        # wb.browser()
        self.url('https://www.taobao.com/')
        self.click(login_entrance)
        self.input(login_user, 15833077492)
        self.input(login_pwd, 'qq308759653')
        self.click(login_button)
        self.wait(2)

    def search(self):
        self.url('https://www.taobao.com/')
        self.input(home_page_search, '手机壳')
        self.click(home_page_search_button)
        self.click(select_goods)
        self.switch_handle(1)
        print('句柄切换完成')
        self.show_wait(select_goods_type)
        print('显示等待')
        self.click(select_goods_type)
        print('点击商品类型')
        self.input_modify(goods_page_num, Keys.BACK_SPACE)
        print('点击商品数量文本框')
        self.input(goods_page_num, 3)
        print('点击商品数量文本框，输入3')
        self.click(add_shopping_trolley)
        print('点击添加购物车按钮')
        try:
            self.input(login_user, 15833077492)
            self.input(login_pwd, 'qq308759653')
            self.click(login_button)
        except:
            pass
