"""
命名规定：
定位元素的要进行输入的内容名字为：元素名字_v (value)
定位元素的配置文件提取的内容名字：元素名字_a (attr)
定位元素去执行的find的名字为：元素名字_e  (element)
"""

from WTFV1.action.login import LoginAction
from WTFV1.tools.ui_util import UiUtil, GetDesignatedPageElement
import time


class LessorHomepage:

    def __init__(self):
        self.driver = UiUtil.get_driver()
        LoginAction().do_login('抢租客0', '123', '0000')
        self.ui = UiUtil()
        self.e = GetDesignatedPageElement(self.driver, '..\\conf\\element_attr.ini', 'tenants_order')

    # 通过页面元素无法定位到，采用图像识别，点击红色表示点，
    def click_red_dot(self):
        time.sleep(2.5)
        self.ui.click_image('..\\image\\test01.png')

    # 跳转ifream
    def skip_iframe(self):
        time.sleep(1)
        iframe_e = self.e.get_element('iframe')
        self.ui.skip_iframe(self.driver, iframe_e)

    # 获取车位信息列表以供后面断言
    def get_text(self):
        time.sleep(1)
        text_e = self.e.get_element('text')
        return text_e.text

    # 点击抢购按钮
    def rush_purchase(self):
        time.sleep(1)
        purchase_e = self.e.get_element('rush_purchase')
        self.ui.click(purchase_e)

    # 点击下单按钮
    def do_confirm(self):
        time.sleep(1)
        self.ui.click_image('..\\image\\test02.png')

    def do_rush_purchase(self):
        self.click_red_dot()
        self.skip_iframe()
        a = self.get_text()
        self.rush_purchase()
        self.do_confirm()
        self.click_red_dot()
        b = self.get_text()
        if a != b:
            actual = "下单成功"
        else:
            actual = "下单失败"
        return actual


if __name__ == '__main__':
    a = LessorHomepage()
    a.do_rush_purchase()
    # print(LessorHomepage().get_add_stall_actual('2345', '1', '4200', '第五国际'))
