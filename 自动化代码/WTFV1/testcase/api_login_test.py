import time

from WTFV1.action.api_login import ApiLogin
from WTFV1.tools.comm_util import FileUtil, CustomAssert


class ApiLoginTest:

    def setup_class(self):
        # 一个模块
        self.al = ApiLogin()
        # 获取基本url信息
        self.base_url = FileUtil.get_ini_value('..\\conf\\base.ini', 'api_info', 'base_url')
        # 获取版本号
        self.version = FileUtil.get_version('..\\data\\spp_case_api.xlsx', 'caseinfo')
        # 获取断言实例化
        self.ca = CustomAssert(self.version, 'spp_test_result')

    def test_api_login(self):
        test_info = FileUtil.get_excel('..\\data\\api_case_data_conf.ini', 'login')
        for info in test_info:
            login_url = self.base_url + info['api_uri']
            actual = self.al.api_login(login_url)
            self.ca.contain(actual, info)
            time.sleep(2)






if __name__ == '__main__':
    alt = ApiLoginTest()
    alt.setup()
    alt.test_api_login()