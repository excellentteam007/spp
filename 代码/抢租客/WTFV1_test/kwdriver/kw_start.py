from WTFV1_test.tools.comm_util import FileUtil
from WTFV1_test.kwdriver.collection import Collection


class Start:

    @classmethod
    def start_kw_script(cls):
        """
        读取脚本的中的关键字和关键字内容，通过关键字找到关键字对应的方法并且执行
        """
        # 读取关键字配置文件
        keyword_map = FileUtil.get_json('keyword.conf')
        script_path = FileUtil.get_txt('keyword_scrip.conf')
        for path in script_path:
            if not path.startswith('#'):
                # 读取csv脚本文件
                scrip = FileUtil.get_csv(path)
                for scrip_v in scrip:
                    col = Collection
                    # 判断不是#号开头的，才是脚本内容
                    if not str(scrip_v[0]).startswith('#'):
                        # 脚本第一项为关键字
                        keyword = scrip_v[0]
                        # 除去第一项为关键字对象的内容
                        keyword_c = scrip_v[1:]
                        # 关键字和关键字方法对应
                        method_name = keyword_map[keyword]
                        if hasattr(col, method_name):
                            # 方法执行
                            method_obj = getattr(col, method_name)
                            # 传递参数
                            method_obj(*keyword_c)


if __name__ == '__main__':
    Start.start_kw_script()