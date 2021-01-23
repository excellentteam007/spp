from WTFV1.tools.comm_util import FileUtil, LogUtil, CustomAssert
from WTFV1.action.tenant_personal_information import PersonalInformation
import time
import traceback
from WTFV1.tools.ui_util import UiUtil


class TenantPersonalInformationTest:
    # 日志
    logger = LogUtil.get_logger('lessor_homepage_test')

    def setup_class(self):
        # 一个项目模块
        self.lh = PersonalInformation()
        # 获取版本号
        self.version = FileUtil.get_version('..\\data\\spp_case_ui.xlsx', 'caseinfo')
        # # 获取断言实例化
        self.ca = CustomAssert(self.version, 'spp_test_result', self.lh.driver)

    def test_add_stall(self):
        # 提取测试信息的配置文件
        test_info = FileUtil.get_excel('..\\data\\case_data_conf.ini', 'personal_information')
        for info in test_info:
            test_data = info['case_params']
            try:
                actual = self.lh.do_change_information(test_data)
                time.sleep(2)
                self.ca.equal(actual, info)
            except Exception as e:
                error_msg = traceback.format_exc()
                info['error_msg'] = error_msg
                self.ca.error(info)

    def teardown_class(self):
        UiUtil.get_driver().get('http://172.16.9.129:8080/SharedParkingPlace/')


if __name__ == '__main__':
    pass
    # lht = LessorHomepageTest()
    # lht.test_add_stall()