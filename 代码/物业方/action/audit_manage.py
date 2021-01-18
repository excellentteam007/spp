from WTFV1.action.login import LoginAction
from WTFV1.tools.ui_util import UiUtil, GetDesignatedPageElement
import time

# 车辆相关模块
class AuditManage:

    def __init__(self):
        self.driver = UiUtil.get_driver()
        LoginAction().do_login('物业0', '123', '0000')
        self.ui = UiUtil()
        self.e = GetDesignatedPageElement(self.driver, '..\\conf\\element_attr.ini', 'audit_manage')

    # 点击审核管理
    def click_audit_manage_button(self):
        audit_manage_e = self.e.get_element('audit_manage')
        self.ui.select_by_js(self.driver, audit_manage_e)

    # 点击业主信息审核
    def click_audit_property_info_button(self):
        audit_property_info_e = self.e.get_element('audit_property_info')
        self.ui.select_by_js(self.driver, audit_property_info_e)

    # 跳转iframe
    def skip_iframe(self):
        iframe_e = self.e.get_element('audit_iframe')
        self.ui.skip_iframe(self.driver, iframe_e)

    # 业主信息审核页面选取所有信息
    def click_all_select(self):
        click_all_select_e = self.e.get_element('click_all_select')
        self.ui.click(click_all_select_e)

    # 点击一键审批所选按钮
    def click_onekey_audit_all_button(self):
        onekey_audit_all_button_e = self.e.get_element('onekey_audit_all_button')
        self.ui.click(onekey_audit_all_button_e)

    # 一键审核所有的动作集
    def do_all_info_pass(self):
        self.click_audit_manage_button()
        self.click_audit_property_info_button()
        self.skip_iframe()
        self.click_all_select()
        self.click_onekey_audit_all_button()

    # 物业方修改用户信息的断言
    def get_audit_all_actual(self):
        self.do_all_info_pass()
        time.sleep(3)
        actual_e = self.e.get_element('audit_all')
        result = self.ui.get_text(actual_e)
        if result == '修改成功':
            actual = '审批成功'
        else:
            actual = '审批失败'
        return actual


if __name__ == '__main__':
    print(AuditManage().get_audit_all_actual())