from WTFV1.action.login import LoginAction
from WTFV1.tools.ui_util import UiUtil, GetDesignatedPageElement
import time

class PropertyManage:

    def __init__(self):
        self.driver = UiUtil.get_driver()
        LoginAction().do_login('物业0', '123', '0000')
        self.ui = UiUtil()
        self.e = GetDesignatedPageElement(self.driver, '..\\conf\\element_attr.ini', 'property_manage')

    # 点击用户管理
    def click_user_management_button(self):
        user_management_e = self.e.get_element('user_management')
        self.ui.select_by_js(self.driver, user_management_e)

    # 点击物业方信息
    def click_info_property_button(self):
        info_property_e = self.e.get_element('info_property')
        self.ui.select_by_js(self.driver, info_property_e)

    # 点击抢租客信息
    def click_info_rentuser_button(self):
        info_rentuser_e = self.e.get_element('info_rentuser')
        self.ui.select_by_js(self.driver, info_rentuser_e)

    # 跳转iframe
    def skip_iframe(self):
        iframe_e = self.e.get_element('property_iframe')
        self.ui.skip_iframe(self.driver, iframe_e)

    # 点击物业方的增加按钮
    def click_add_property_button(self):
        add_property_button_e = self.e.get_element('add_property_button')
        self.ui.click(add_property_button_e)

    # 点击物业方修改的按钮
    def click_change_property_button(self):
        change_button_e = self.e.get_element('change_property_button')
        self.ui.click(change_button_e)

    # 输入物业名
    def input_property_name(self, name):
        property_name_e = self.e.get_element('property_name')
        self.ui.input(property_name_e,name)

    # 输入用户电话
    def input_property_phone(self, phone):
        user_phone_e = self.e.get_element('property_phone')
        self.ui.input(user_phone_e,phone)

    # 输入物业简介
    def input_property_introduce(self, introduce):
        property_introduce_e = self.e.get_element('property_introduce')
        self.ui.input(property_introduce_e, introduce)

    # 输入物业证书
    def input_property_credential(self, credential):
        property_credential_e = self.e.get_element('property_credential')
        self.ui.input(property_credential_e, credential)

    # 输入物业密码
    def input_property_password(self, password):
        property_password_e = self.e.get_element('property_password')
        self.ui.input(property_password_e, password)

    # 物业方确认增加信息的按钮
    def click_add_button(self):
        add_button_e = self.e.get_element('add_button')
        self.ui.click(add_button_e)

    # 物业方确认修改信息的按钮
    def click_change_button(self):
        change_button_e = self.e.get_element('change_button')
        self.ui.click(change_button_e)

    # 增加物业的所有动作集
    def do_add_property(self, name,phone, introduce, credential, password):
        self.click_user_management_button()
        self.click_info_property_button()
        self.skip_iframe()
        self.click_add_property_button()
        self.input_property_name(name)
        self.input_property_phone(phone)
        self.input_property_introduce(introduce)
        self.input_property_credential(credential)
        self.input_property_password(password)
        self.click_add_button()

    # 增加物业用例的断言
    def get_add_property_actual(self, name, phone, introduce, credential, password):
        self.do_add_property(name, phone, introduce, credential, password)
        time.sleep(2)
        actual_e = self.e.get_element('add_property_actual')
        return self.ui.get_text(actual_e)

    # 输入要搜索的物业方姓名
    def input_search_name(self, name):
        input_search_property_name_e = self.e.get_element('input_search_property_name')
        self.ui.input(input_search_property_name_e, name)

    # 输入要搜索的抢租客的姓名
    def input_search_rent_name(self,name):
        input_search_rent_name_e = self.e.get_element('input_search_rent_name')
        self.ui.input(input_search_rent_name_e, name)

    # 点击放大镜图标进行搜索
    def click_search_enter(self):
        search_enter_e = self.e.get_element('search_enter')
        self.ui.click(search_enter_e)

    # 勾选物业方页面第一个方块
    def click_property_square(self):
        property_square_e = self.e.get_element('click_property_square')
        self.ui.click(property_square_e)

    # 通过名字进行搜索动作集
    def do_property_search_by_name(self, name):
        self.click_user_management_button()
        self.click_info_property_button()
        self.skip_iframe()
        self.input_search_name(name)
        self.click_search_enter()

    # 通过姓名搜索的断言
    def get_property_search_by_name_actual(self, name):
        self.do_property_search_by_name(name)
        actual_e = self.e.get_element('property_search_by_name_actual')
        time.sleep(2)
        result = self.ui.get_text(actual_e)
        time.sleep(2)
        if result == name:
            actual = '搜索成功'
        else:
            actual = '搜索失败'
        return actual

    # 物业方鼠标悬浮打开下拉框
    def open_property_select_method(self):
        open_property_select_method_e = self.e.get_element('open_property_select_method')
        self.ui.mouse_hover(self.driver,open_property_select_method_e)

    # 出租方鼠标悬浮打开下拉框
    def open_rent_select_method(self):
        open_rent_select_method_e = self.e.get_element('open_rent_select_method')
        self.ui.mouse_hover(self.driver,open_rent_select_method_e)

    # 物业方在下拉框打开后选择电话
    def click_property_select_phone(self):
        click_property_select_phone_e = self.e.get_element('click_property_select_phone')
        self.ui.click(click_property_select_phone_e)

    # 抢租客方在下拉框打开后选择电话
    def click_rent_select_phone(self):
        click_rent_select_phone_e = self.e.get_element('click_rent_select_phone')
        self.ui.click(click_rent_select_phone_e)

    # 物业方输入要搜索的电话号码
    def input_property_search_phone(self, phone):
        input_property_search_phone_e = self.e.get_element('input_property_search_phone')
        self.ui.input(input_property_search_phone_e, phone)

    # 抢租客输入要搜索的电话号码
    def input_rent_search_phone(self, phone):
        input_rent_search_phone_e = self.e.get_element('input_rent_search_phone')
        self.ui.input(input_rent_search_phone_e, phone)

    #根据电话搜索物业方的动作集
    def do_property_search_by_phone(self,phone):
        self.click_user_management_button()
        self.click_info_property_button()
        self.skip_iframe()
        self.open_property_select_method()
        self.click_property_select_phone()
        self.input_property_search_phone(phone)
        self.click_search_enter()

    # 物业方信息通过电话搜索的断言
    def get_property_search_by_phone_actual(self, phone):
        self.do_property_search_by_phone(phone)
        time.sleep(3)
        actual_e = self.e.get_element('property_search_by_phone_actual')
        time.sleep(5)
        result = self.ui.get_text(actual_e)
        if result == phone:
            actual = '根据电话搜索成功'
        else:
            actual = '根据电话搜索失败'
        return actual

    #抢租客信息，根据姓名搜索的动作集
    def do_search_rent_by_name(self,name):
        self.click_user_management_button()
        self.click_info_rentuser_button()
        self.skip_iframe()
        self.input_search_rent_name(name)
        self.click_search_enter()

    # 抢租客信息通过名字搜索的断言
    def get_rent_search_by_name_actual(self, name):
        self.do_search_rent_by_name(name)
        time.sleep(3)
        actual_e = self.e.get_element('rent_by_name_actual')
        time.sleep(5)
        result = self.ui.get_text(actual_e)
        if result == name:
            actual = '根据姓名搜索抢租客成功'
        else:
            actual = '根据姓名搜索抢租客失败'
        return actual

    #根据电话搜索抢租客的动作集
    def do_rent_search_by_phone(self,phone):
        self.click_user_management_button()
        self.click_info_rentuser_button()
        self.skip_iframe()
        self.open_rent_select_method()
        self.click_rent_select_phone()
        self.input_rent_search_phone(phone)
        self.click_search_enter()

    # 抢租客信息通过电话搜索的断言
    def get_rent_search_by_phone_actual(self, phone):
        self.do_rent_search_by_phone(phone)
        time.sleep(3)
        actual_e = self.e.get_element('rent_search_by_phone_actual')
        time.sleep(5)
        result = self.ui.get_text(actual_e)
        if result == phone:
            actual = '根据电话搜索抢租客信息成功'
        else:
            actual = '根据电话搜索抢租客信息失败'
        return actual

    # 修改物业方用户信息的动作集
    def do_property_change_info(self, name, new_name, new_phone, new_intro, new_cred):
        self.click_user_management_button()
        self.click_info_property_button()
        self.skip_iframe()
        self.input_search_name(name)
        self.click_search_enter()
        time.sleep(3)
        self.click_property_square()
        self.click_change_property_button()
        self.input_property_name(new_name)
        self.input_property_phone(new_phone)
        self.input_property_introduce(new_intro)
        self.input_property_credential(new_cred)
        self.click_change_button()

    # 物业方修改用户信息的断言
    def get_property_change_phone_actual(self, name, new_name, new_phone, new_intro, new_cred):
        self.do_property_change_info(name, new_name, new_phone, new_intro, new_cred)
        time.sleep(5)
        actual_e = self.e.get_element('property_actual')
        result = self.ui.get_text(actual_e)
        if result == '修改成功':
            actual = '修改用户信息成功'
        else:
            actual = '修改用户信息失败'
        return actual






if __name__ == '__main__':
    # print(PropertyManage().get_add_property_actual("物业000","18799990000","jianjie","zhengshu","11111"))
    # print(PropertyManage().get_property_search_by_name_actual('物业7777'))
    # print(PropertyManage().get_property_search_by_phone_actual('15304440333'))
    # print(PropertyManage().get_rent_search_by_name_actual("周友"))
    # print(PropertyManage().get_rent_search_by_phone_actual("15802792107"))
    print(PropertyManage().get_property_change_phone_actual('物业6666','物业6666','18678789090','33','22'))
