import requests
from WTFV1.tools.comm_util import FileUtil


class ApiUtil:

    @classmethod
    def get_session(cls):
        """
        :return: 获取request里面的session
        """
        return requests.session()

    @classmethod
    def set_cookie(cls, session):
        """
        获取页面的cookie
        :param session: 上面的session
        """
        login_page_url = FileUtil.get_ini_value('..\\conf\\base.ini', 'api_info', 'login_page_url')
        session.get(login_page_url)


if __name__ == '__main__':
    pass


