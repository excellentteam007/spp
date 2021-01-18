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


class PersonalInformation:

    def __init__(self):
        self.driver = UiUtil.get_driver()
        LoginAction().do_login('抢租客0', '123', '0000')
        self.ui = UiUtil()
        self.ele = FileUtil.trans_ini_tuple_to_dict('..\\conf\\element_attr.ini', 'personal_information')

    def examine_personal_information(self):
        time.sleep(0.5)
        order_history_a = eval(self.ele['personal_information'])
        order_history = self.ui.find_element(self.driver, order_history_a)
        self.ui.click(order_history)

    # 跳转ifream
    def skip_iframe(self):
        time.sleep(1)
        iframe_a = eval(self.ele['iframe'])
        iframe_e = self.ui.find_element(self.driver, iframe_a)
        self.ui.skip_iframe(self.driver, iframe_e)

    def change_information(self):
        time.sleep(0.5)
        order_history_a = eval(self.ele['change_information'])
        order_history_e = self.ui.find_element(self.driver, order_history_a)
        self.ui.click(order_history_e)

    def amend_uname(self):
        time.sleep(0.5)
        uname_a = eval(self.ele['amend_uname'])
        uname_e = self.ui.find_element(self.driver, uname_a)
        self.ui.input(uname_e,"抢租客1")

    def amend_uphone_number(self):
        time.sleep(0.5)
        uname_a = eval(self.ele['amend_uphone_number'])
        uname_e = self.ui.find_element(self.driver, uname_a)
        self.ui.input(uname_e, "17296313549")

    def affirm_change(self):
        time.sleep(0.5)
        order_history_a = eval(self.ele['affirm_change'])
        order_history_e = self.ui.find_element(self.driver, order_history_a)
        self.ui.click(order_history_e)

    def get_text(self):
        time.sleep(5)
        order_history_a = eval(self.ele['text'])
        order_history_e = self.ui.find_element(self.driver, order_history_a)
        text = self.ui.get_text(order_history_e)
        return text

    def do_change_information(self):
        self.examine_personal_information()
        self.skip_iframe()
        self.change_information()
        self.amend_uname()
        self.amend_uphone_number()
        self.affirm_change()
        a = self.get_text()
        if "抢租客1" and "17296313549" in a:
            print("修改成功")
        else:
            print("修改失败")

if __name__ == '__main__':
    a = PersonalInformation()
    a.do_change_information()
