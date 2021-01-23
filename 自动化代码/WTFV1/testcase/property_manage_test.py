from WTFV1.tools.comm_util import FileUtil, LogUtil, CustomAssert
from WTFV1.action.property_manage import PropertyManage
from WTFV1.tools.ui_util import UiUtil
import time
import traceback


class PropertyManageTest:
    # 日志
    logger = LogUtil.get_logger('property_manage_test')

    def setup_class(self):
        # 一个项目模块
        self.pm = PropertyManage()
        # 获取版本号
        self.version = FileUtil.get_version('..\\data\\spp_case_ui.xlsx', 'caseinfo')
        # 获取断言实例化
        self.ca = CustomAssert(self.version, 'spp_test_result', self.pm.driver)

    def test_add_property(self):
        # 提取测试信息的配置文件
        test_info = FileUtil.get_excel('..\\data\\case_data_conf.ini', 'add_property')
        for info in test_info:
            test_data = info['case_params']
            try:
                actual = self.pm.get_add_property_actual(test_data)
                self.ca.equal(actual, info)
            except Exception as e:
                error_msg = traceback.format_exc()
                info['error_msg'] = error_msg
                self.ca.error(info)
            time.sleep(3)

    def test_change_info(self):
        # 提取测试信息的配置文件
        test_info = FileUtil.get_excel('..\\data\\case_data_conf.ini', 'change_info')
        for info in test_info:
            test_data = info['case_params']
            try:
                actual = self.pm.do_property_change_info(test_data)
                self.ca.equal(actual, info)
            except Exception as e:
                error_msg = traceback.format_exc()
                info['error_msg'] = error_msg
                self.ca.error(info)
            # actual = self.pm.do_property_change_info(test_data)
            time.sleep(3)

    def test_property_search_by_name(self):
        # 提取测试信息的配置文件
        test_info = FileUtil.get_excel('..\\data\\case_data_conf.ini', 'property_search_by_name')
        for info in test_info:
            test_data = info['case_params']
            try:
                actual = self.pm.get_property_search_by_name_actual(test_data)
                self.ca.equal(actual, info)
            except Exception as e:
                error_msg = traceback.format_exc()
                info['error_msg'] = error_msg
                self.ca.error(info)
            time.sleep(2)
            # actual = self.pm.get_property_search_by_name_actual(test_data)

    def test_property_search_by_phone(self):
        # 提取测试信息的配置文件
        test_info = FileUtil.get_excel('..\\data\\case_data_conf.ini', 'property_search_by_phone')
        for info in test_info:
            test_data = info['case_params']
            try:
                actual = self.pm.get_property_search_by_phone_actual(test_data)
                self.ca.equal(actual, info)
            except Exception as e:
                error_msg = traceback.format_exc()
                info['error_msg'] = error_msg
                self.ca.error(info)
            time.sleep(2)

    def teardown_class(self):
        UiUtil.get_driver().get('http://172.16.9.129:8080/SharedParkingPlace/')



if __name__ == '__main__':
    pmt = PropertyManageTest()
    pmt.test_property_search_by_phone()