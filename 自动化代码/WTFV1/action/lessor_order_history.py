"""
命名规定：
定位元素的要进行输入的内容名字为：元素名字_v (value)
定位元素的配置文件提取的内容名字：元素名字_a (attr)
定位元素去执行的find的名字为：元素名字_e  (element)
"""

from WTFV1.action.login import LoginAction
from WTFV1.tools.ui_util import UiUtil, GetDesignatedPageElement
import time


class LessorOrderHistory:
    """
    出租方历史订单
    """

    def __init__(self):
        self.driver = UiUtil.get_driver()
        LoginAction().do_login('222', '123', '0000')
        self.ui = UiUtil()
        self.e = GetDesignatedPageElement(self.driver, '..\\conf\\element_attr.ini', 'lessor_order_history')
        self.click_order_history()
        time.sleep(5)
        self.skip_iframe()

    # 点击历史订单
    def click_order_history(self):
        order_history_e = self.e.get_element('order_history')
        self.ui.click(order_history_e)

    # 跳转iframe
    def skip_iframe(self):
        iframe_e = self.e.get_element('iframe')
        self.ui.skip_iframe(self.driver, iframe_e)

    # 选择订单查询类型
    def select_search_type(self, type_v):
        search_type_e = self.e.get_element('search_type')
        self.ui.select_drop_down_box(search_type_e, type_v)

    # 选择类型对应的状态值
    def select_order_status(self, status_v):
        status_e = self.e.get_element('status')
        self.ui.select_drop_down_box(status_e, status_v)

    # 点击搜索按钮
    def click_search_button(self):
        search_button_e = self.e.get_element('search_button')
        self.ui.click(search_button_e)

    # 按状态去执行搜索
    def do_status_order_search(self, type_v, status_v):
        self.select_search_type(type_v)
        self.select_order_status(status_v)
        self.click_search_button()

    # 获取按状态去执行搜索，返回"搜索成功"或者"搜索失败"
    def get_status_order_search_result(self, type_v, status_v):
        self.do_status_order_search(type_v, status_v)
        time.sleep(2)
        status_search_result_e = self.e.get_element('status_search_result')
        result = self.ui.get_text(status_search_result_e)
        time.sleep(5)
        if result == status_v:
            actual = "搜索成功"
        else:
            actual = "搜索失败"
        return actual

    # 选择账单时间
    def select_order_time(self, time1):
        js_code = f'''document.querySelector('input[id="time"]').value='{time1}';'''
        self.ui.execute_js(self.driver, js_code)

    # 按账单时间去执行搜索
    def do_time_order_search(self, type_v, time1):
        self.select_search_type(type_v)
        self.select_order_time(time1)
        self.click_search_button()

    # 按账单时间去执行搜索，返回"搜索成功"或者"搜索失败"
    def get_time_order_search_result(self, type_v, time1):
        self.do_time_order_search(type_v, time1)
        time.sleep(2)
        time_search_result_e = self.e.get_element('time_search_result')
        result = self.ui.get_text(time_search_result_e)
        if result[0:4] in time1:
            actual = "搜索成功"
        else:
            actual = "搜索失败"
        return actual










if __name__ == '__main__':
    run = LessorOrderHistory()
    # print(run.get_status_order_search_result('按状态查询', '已完成'))
    print(run.get_time_order_search_result('按时间查询', '2019-06-26'))
