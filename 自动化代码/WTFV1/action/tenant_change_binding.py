"""
命名规定：
定位元素的要进行输入的内容名字为：元素名字_v (value)
定位元素的配置文件提取的内容名字：元素名字_a (attr)
定位元素去执行的find的名字为：元素名字_e  (element)
"""

from WTFV1.action.login import LoginAction
from WTFV1.tools.ui_util import UiUtil
from WTFV1.tools.comm_util import FileUtil
import time


class ChengeBinding:

    def __init__(self):
        self.driver = UiUtil.get_driver()
        LoginAction().do_login('抢租客0', '123', '0000')
        self.ui = UiUtil()
        self.ele = FileUtil.trans_ini_tuple_to_dict('..\\conf\\element_attr.ini', 'chenge_binding')

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

    def click_chenge_binding(self):
        time.sleep(0.5)
        chenge_binding_a = eval(self.ele['chenge_binding'])
        chenge_binding = self.ui.find_element(self.driver, chenge_binding_a)
        self.ui.click(chenge_binding)

    def input_account(self,binding):
        time.sleep(0.5)
        input_account_a = eval(self.ele['input_account'])
        input_account_e = self.ui.find_element(self.driver, input_account_a)
        self.ui.input(input_account_e,binding)

    def commit_changes(self):
        time.sleep(0.5)
        commit_changes_a = eval(self.ele['commit_changes'])
        commit_changes = self.ui.find_element(self.driver, commit_changes_a)
        self.ui.click(commit_changes)

    def get_text(self):
        time.sleep(5)
        get_text_a = eval(self.ele['text'])
        get_text_e = self.ui.find_element(self.driver, get_text_a)
        text = self.ui.get_text(get_text_e)
        return text

    def do_chenge_binding(self,data):
        self.examine_personal_information()
        self.skip_iframe()
        self.click_chenge_binding()
        self.input_account(data["account"])
        self.commit_changes()
        self.driver.refresh()
        self.examine_personal_information()
        self.skip_iframe()
        a = self.get_text()
        self.driver.refresh()
        if data["account"] in a:
            actual = "变更绑定成功"
        else:
            actual = "变更绑定失败"
        return actual

if __name__ == '__main__':
    binding = {'account': '112233'}
    a = ChengeBinding()
    print(a.do_chenge_binding(binding))
