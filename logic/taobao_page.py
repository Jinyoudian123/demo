# coding=utf8
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from basic.keyword import WebKey

# 登录页的信息
login_entrance = ['link text', '亲，请登录']
login_user = ['xpath', '//input[@name="fm-login-id"]']
login_pwd = ['xpath', '//input[@name="fm-login-password"]']
login_button = ['xpath', '//button[@type="submit"]']
# 首页搜索
home_page_search = ['id', 'q']
home_page_search_button = ['xpath', '//button[@type="submit"]']
select_goods = ['xpath', '//div[@class="items"][1]/div[7]//a']
# 商品页的选择
goods_title = ['xpath', '//div[@id="detail"]//h1']
select_goods_type = ['xpath', '//div[@class="tb-sku"]//dl[1]//li[1]']
select_goods_type1 = ['xpath', '//div[@class="tb-sku"]//dl[2]//li[5]']
goods_page_num = ['xpath', '//input[@title="请输入购买量"]']
add_shopping_trolley = ['xpath', '//a[@id="J_LinkBasket"]']
shopping_trolley = ['link text', '购物车']
shopping_trolley_in_goods_title = ['xpath', '//div[@id="J_OrderList"]/div[1]//div[@class="order-content"]'
                                            '//div[@class="item-basic-info"]/a']
delete_button = '//div[@id="J_OrderList"]/div[1]//div[@class="order-content"]//a[text()="删除"]'
yes_delete_button = ['xpath', '//div[@id="ks-component471"]//div[@id="ks-content-ks-component471"]'
                              '//a[contains(text(),"定")]']
air_view = ['xpath', '//div[@class="J_detail_cart_layer"]'], 'display'


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
        self.input(home_page_search, '水杯')
        self.click(home_page_search_button)
        self.click(select_goods)
        self.switch_handle(1)
        print('句柄切换完成')
        # self.wait(3)
        goods_name = self.location_list(goods_title).text
        self.show_wait(select_goods_type)
        print('显示等待')
        self.click(select_goods_type)
        print('点击商品类型')
        try:
            self.click(select_goods_type1)
        except:
            pass
        self.input(goods_page_num, Keys.BACK_SPACE)
        print('点击商品数量文本框')
        self.input(goods_page_num, 3)
        print('点击商品数量文本框，输入3')
        self.wait(1)
        self.screenshot('../num.png')
        self.wait(1)
        self.click(add_shopping_trolley)
        print('点击添加购物车按钮')
        try:
            self.input(login_user, 15833077492)
            self.input(login_pwd, 'qq308759653')
            self.click(login_button)
            print('点击添加购物车按钮')
            self.click(add_shopping_trolley)
        except:
            pass
        # goods_name1 = self.location_list(shopping_trolley_in_goods_title).title
        # if self.assert_text(shopping_trolley_in_goods_title, goods_name):
        #     print('添加购物车成功')
        # else:
        #     raise Exception('添加购物车失败')
        assert self.getAttribute(*air_view) is None, '添加购物车失败'
        self.click(shopping_trolley)
        self.click(delete_button)
        self.click(yes_delete_button)
        print('流程运行结束')
