from WTFV1.tools.api_util import ApiUtil


class ApiLogin:

    def __init__(self):
        # 获取session
        self.session = ApiUtil.get_session()
        # 获取cookie
        ApiUtil.set_cookie(self.session)

    def api_login(self, url):
        login_resp = self.session.get(url)
        return login_resp.text


if __name__ == '__main__':
    al = ApiLogin()
    print(al.api_login('http://172.16.9.129:8080/SharedParkingPlace/login?uname=出租方1&upass=123&imgcode=0000'))




