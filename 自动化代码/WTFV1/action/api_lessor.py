from WTFV1.tools.api_util import ApiUtil


class ApiLessor:

    def __init__(self):
        # 获取session
        self.session = ApiUtil.get_session()
        # 获取cookie
        ApiUtil.set_cookie(self.session)
        self.session.get('http://172.16.9.129:8080/SharedParkingPlace/login?uname=出租方1&upass=123&imgcode=0000')

    def api_add_stall(self, url, data):
        add_stall_resp = self.session.post(url, data)
        return add_stall_resp.text

    def api_query_order_info(self, url):
        query_order_info_resp = self.session.get(url)
        return query_order_info_resp.text

    def api_query_comment(self, url):
        query_comment_resp = self.session.get(url)
        return query_comment_resp.text


if __name__ == '__main__':
    al = ApiLessor()
    #
    # url =' http://172.16.9.129:8080/SharedParkingPlace/admin/auditsManagement/parkinginformation/'
    # data = {'parkingnumber': '123', 'parkingstatus': '1', 'uid': '6ade98f4-a14c-4bf0-a993-8ca936030245',
    #         'parkingsizeid':'1', 'locationid': '4531', 'detailslocation': '第五国际'}
    # print(al.api_add_stall(url, data))