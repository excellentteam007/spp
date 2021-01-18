"""
命名规定：
定位元素的要进行输入的内容名字为：元素名字_v (value)
定位元素的配置文件提取的内容名字：元素名字_a (attr)
定位元素去执行的find的名字为：元素名字_e  (element)
"""

from WTFV1_test.action.login import LoginAction
from WTFV1_test.tools.ui_util import UiUtil
from WTFV1_test.tools.comm_util import FileUtil
import time


class Comment:

    def __init__(self):
        self.driver = UiUtil.get_driver()
        LoginAction().do_login('抢租客0', '123', '0000')
        self.ui = UiUtil()
        self.ele = FileUtil.trans_ini_tuple_to_dict('..\\conf\\element_attr.ini', 'comment')

    #点击进入历史订单页面
    def examine_order_history (self):
        time.sleep(0.5)
        order_history_a = eval(self.ele['order_history'])
        order_history = self.ui.find_element(self.driver, order_history_a)
        self.ui.click(order_history)

    def skip_iframe(self):
        time.sleep(1)
        iframe_a = eval(self.ele['iframe'])
        iframe_e = self.ui.find_element(self.driver, iframe_a)
        self.ui.skip_iframe(self.driver, iframe_e)

    def query_method(self):
        time.sleep(5)
        query_method_a = eval(self.ele['query_method'])
        query_method = self.ui.find_element(self.driver, query_method_a)
        self.ui.select_drop_down_box(query_method,"按状态查询")

    def select_status(self):
        time.sleep(0.5)
        select_status_a = eval(self.ele['select_status'])
        select_status= self.ui.find_element(self.driver, select_status_a)
        self.ui.select_drop_down_box(select_status, "已完成")

    def click_seek(self):
        time.sleep(0.5)
        click_seek_a = eval(self.ele['click_seek'])
        click_seek = self.ui.find_element(self.driver, click_seek_a)
        self.ui.click(click_seek)

    def click_comment(self):
        time.sleep(0.5)
        click_comment_a = eval(self.ele['comment'])
        click_comment = self.ui.find_element(self.driver, click_comment_a)
        self.ui.click(click_comment)

    def input_comment(self,comment):
        time.sleep(0.5)
        input_comment_a = eval(self.ele['input_comment'])
        input_comment_e = self.ui.find_element(self.driver, input_comment_a)
        self.ui.input(input_comment_e,"车位干净整洁,挺不错的")

    def send_comment(self):
        time.sleep(0.5)
        send_comment_a = eval(self.ele['send_comment'])
        send_comment = self.ui.find_element(self.driver, send_comment_a)
        self.ui.click(send_comment)

    def get_text(self):
        time.sleep(5)
        order_history_a = eval(self.ele['text'])
        order_history_e = self.ui.find_element(self.driver, order_history_a)
        text = self.ui.get_text(order_history_e)
        return text

    def do_comment(self,comment):
        self.examine_order_history()
        self.skip_iframe()
        self.query_method()
        self.select_status()
        self.click_seek()
        self.click_comment()
        self.input_comment(comment)
        self.send_comment()
        text = self.get_text()



if __name__ == '__main__':
    a = Comment()
    a.do_comment()
