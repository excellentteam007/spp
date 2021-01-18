from WTFV1.tools.ui_util import UiUtil
from WTFV1.tools.comm_util import FileUtil

"""
命名规定：
定位元素的要进行输入的内容名字为：元素名字_v (value)
定位元素的配置文件提取的内容名字：元素名字_a (attr)
定位元素去执行的find的名字为：元素名字_e  (element)
"""


class LoginAction:

    def __init__(self):
        self.driver = UiUtil.get_driver()
        self.ui = UiUtil()
        self.ele = FileUtil.trans_ini_tuple_to_dict('..\\conf\\element_attr.ini', 'login')

    # 用户名输入
    def input_name(self, uname_v):
        uname_a = eval(self.ele["name"])
        uname_e = self.ui.find_element(self.driver, uname_a)
        self.ui.input(uname_e, uname_v)

    # 密码输入
    def input_password(self, password_v):
        password_a = eval(self.ele['password'])
        password_e = self.ui.find_element(self.driver, password_a)
        self.ui.input(password_e, password_v)

    # 验证码输入
    def input_imgcode(self, imgcode_v):
        imgcode_a = eval(self.ele['imgcode'])
        imgcode_e = self.ui.find_element(self.driver, imgcode_a)
        self.ui.input(imgcode_e, imgcode_v)

    # 登录的点击
    def click_login_button(self):
        button_a = eval(self.ele['button'])
        button_e = self.ui.find_element(self.driver, button_a)
        self.ui.click(button_e)

    # 登录动作
    def do_login(self, name, password, imgcode):
        self.input_name(name)
        self.input_password(password)
        self.input_imgcode(imgcode)
        self.click_login_button()

    # 登录后的实际结果验证
    def get_login_result(self, name, password, imgcode):
        self.do_login(name, password, imgcode)
        actual_a = eval(self.ele['actual'])
        actual_e = self.ui.find_element(self.driver, actual_a)
        return self.ui.get_text(actual_e)


if __name__ == '__main__':
    LoginAction().do_login('出租方1', '123', '0000')
    # print(LoginAction().get_login_result("222", "123", "0000"))