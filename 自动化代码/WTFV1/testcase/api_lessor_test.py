import time
from WTFV1.tools.comm_util import FileUtil, CustomAssert
from WTFV1.action.api_lessor import ApiLessor


class ApiLessorTest:

    def setup_class(self):
        # 一个模块
        self.al = ApiLessor()
        # 获取基本url信息
        self.base_url = FileUtil.get_ini_value('..\\conf\\base.ini', 'api_info', 'base_url')
        # 获取版本号
        self.version = FileUtil.get_version('..\\data\\spp_case_api.xlsx', 'caseinfo')
        # 获取断言实例化
        self.ca = CustomAssert(self.version, 'spp_test_result')

    def test_add_stall(self):
        test_info = FileUtil.get_excel('..\\data\\api_case_data_conf.ini', 'add_stall')
        for info in test_info:
            add_stall_url = self.base_url + info['api_uri']
            add_stall_data = info['case_params']
            actual = self.al.api_add_stall(add_stall_url, add_stall_data)
            self.ca.equal(actual, info)
            time.sleep(2)

    def test_query_order_info(self):
        test_info = FileUtil.get_excel('..\\data\\api_case_data_conf.ini', 'query_comment')
        for info in test_info:
            query_order_info_url = self.base_url + info['api_uri']
            actual = self.al.api_query_comment(query_order_info_url)
            self.ca.contain(actual, info)
            time.sleep(2)

    def test_query_comment(self):
        test_info = FileUtil.get_excel('..\\data\\api_case_data_conf.ini', 'query_comment')
        for info in test_info:
            query_comment_url = self.base_url + info['api_uri']
            actual = self.al.api_query_comment(query_comment_url)
            self.ca.contain(actual, info)
            time.sleep(2)
