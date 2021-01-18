"""
命名规定：
定位元素的要进行输入的内容名字为：元素名字_v (value)
定位元素的配置文件提取的内容名字：元素名字_a (attr)
定位元素去执行的find的名字为：元素名字_e  (element)
"""

from WTFV1.action.login import LoginAction
from WTFV1.tools.ui_util import UiUtil
from WTFV1.tools.comm_util import FileUtil


class LessorHomepage:

    def __init__(self):
        self.driver = UiUtil.get_driver()
        LoginAction().do_login('出租方1', '123', '0000')
        self.ui = UiUtil()
        self.ele = FileUtil.trans_ini_tuple_to_dict('..\\conf\\element_attr.ini', 'lessor_homepage')

    def skip_iframe(self):
        iframe_a = eval(self.ele['iframe'])
        iframe_e = self.ui.find_element(self.driver, iframe_a)
        self.ui.skip_iframe(self.driver, iframe_e)

    def click_add_stall_button(self):
        add_stall_a = eval(self.ele['add_stall'])
        add_stall_e = self.ui.find_element(self.driver, add_stall_a)
        self.ui.select_by_js(self.driver, add_stall_e)


    def input_size_id(self, size_id_v):
        size_id_a = eval(self.ele['size_id'])
        stall_number_e = self.ui.find_element(self.driver, size_id_a)
        self.ui.input(stall_number_e, size_id_v)

    def input_location_id(self, location_id_v):
        location_id_a = eval(self.ele['location_id'])
        stall_number_e = self.ui.find_element(self.driver, location_id_a)
        self.ui.input(stall_number_e, location_id_v)

    def input_address(self, address_v):
        address_a = eval(self.ele['address'])
        stall_number_e = self.ui.find_element(self.driver, address_a)
        self.ui.input(stall_number_e, address_v)

    def click_add_button(self):
        add_button_a = eval(self.ele['add_button'])
        add_button_e = self.ui.find_element(self.driver, add_button_a)
        self.ui.click(add_button_e)

    def do_add_stall(self, number, size_id, location_id, address):
        self.skip_iframe()
        self.click_add_stall_button()
        self.input_stall_number(number)
        self.input_size_id(size_id)
        self.input_location_id(location_id)
        self.input_address(address)
        self.click_add_button()

    def get_add_stall_actual(self, number, size_id, location_id, address):
        self.do_add_stall(number, size_id, location_id, address)
        actual_a = eval(self.ele['add_stall_actual'])
        actual_e = self.ui.find_element(self.driver, actual_a)
        return self.ui.get_text(actual_e)


if __name__ == '__main__':
    print(LessorHomepage().get_add_stall_actual('2345', '1', '4200', '第五国际'))
