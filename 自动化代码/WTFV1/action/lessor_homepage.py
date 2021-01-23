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
    """
    出租方主页
    """

    def __init__(self):
        self.driver = UiUtil.get_driver()
        LoginAction().do_login('出租方103', '123', '0000')
        self.ui = UiUtil()
        self.e = GetDesignatedPageElement(self.driver, '..\\conf\\element_attr.ini', 'lessor_homepage')
        self.skip_iframe()

    # 跳转iframe
    def skip_iframe(self):
        iframe_e = self.e.get_element('iframe')
        self.ui.skip_iframe(self.driver, iframe_e)

    # 点击添加车位按钮
    def click_add_stall_button(self):
        add_stall_e = self.e.get_element('add_stall')
        self.ui.select_by_js(self.driver, add_stall_e)

    # 输入车位id
    def input_stall_number(self, stall_number_v):
        stall_number_e = self.e.get_element('stall_number')
        self.ui.input(stall_number_e, stall_number_v)

    # 输入大小id
    def input_size_id(self, size_id_v):
        stall_number_e = self.e.get_element('size_id')
        self.ui.input(stall_number_e, size_id_v)

    # 输入位置id
    def input_location_id(self, location_id_v):
        stall_number_e = self.e.get_element('location_id')
        self.ui.input(stall_number_e, location_id_v)

    # 输入详细地址
    def input_address(self, address_v):
        stall_number_e = self.e.get_element('address')
        self.ui.input(stall_number_e, address_v)

    # 点击增加确认按钮
    def click_add_confirm_button(self):
        add_confirm_button_e = self.e.get_element('add_confirm_button')
        self.ui.click(add_confirm_button_e)

    # 执行增加车位动作
    def do_add_stall(self, data):
        self.click_add_stall_button()
        self.input_stall_number(data['stall_id'])
        self.input_size_id(data['size_id'])
        self.input_location_id(data['location_id'])
        self.input_address(data['detailed_address'])
        self.click_add_confirm_button()

    # 获取增加车位动作结果
    def get_add_stall_actual(self, data):
        self.do_add_stall(data)
        try:
            add_stall_result_e = self.e.get_element('add_stall_result')
        except:
            actual = "添加失败"
        else:
            result = self.ui.get_text(add_stall_result_e)
            if data['stall_id'] in result:
                actual = "添加成功"
            else:
                actual = "添加失败"
            time.sleep(3)
            self.click_delete_stall_button()
        return actual

    # 点击删除车位按钮
    def click_delete_stall_button(self):
        delete_stall_button_e = self.e.get_element('delete_stall_button')
        self.ui.click(delete_stall_button_e)

    # 点击修改车位按钮
    def click_modify_button(self):
        modify_button_e = self.e.get_element('modify_button')
        self.ui.click(modify_button_e)

    # 点击修改确认按钮
    def click_modify_confirm_button(self):
        modify_confirm_button_e = self.e.get_element('modify_confirm_button')
        self.ui.click(modify_confirm_button_e)

    # 执行修改车位按钮
    def do_modify_stall(self, data):
        self.click_modify_button()
        self.input_stall_number(data['stall_id'])
        self.input_size_id(data['size_id'])
        self.input_location_id(data['location_id'])
        self.input_address(data['detailed_address'])
        self.click_modify_confirm_button()

    def get_modify_stall_actual(self, data):
        self.do_modify_stall(data)
        time.sleep(3)
        modify_stall_result_e = self.e.get_element('modify_stall_result')
        modify_stall_result = self.ui.get_text(modify_stall_result_e)
        if data['stall_id'] in modify_stall_result:
            actual = '修改成功'
        else:
            actual = '修改失败'
        return actual

if __name__ == '__main__':
    print(LessorHomepage().get_modify_stall_actual(d))
    # LessorHomepage().do_modify('2345', '1', '4200', '第五国际')
