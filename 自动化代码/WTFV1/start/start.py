from WTFV1.tools.comm_util import FileUtil


class Start:

    def do_start(self):
        """
        获取测试脚本一起执行
        :return:
        """
        # 读取测试脚本的配置文件
        test_class_name = FileUtil.get_txt('..\\conf\\test_class_names.txt')
        for class_name in test_class_name:
            # 判断不以#开头的
            if not class_name.startswith('#'):
                # 把路径和类名分开
                temp = class_name.split(' ')
                # 返回模块名对应的模块对象
                module_obj = __import__(temp[0], fromlist=temp[1])
                if hasattr(module_obj, temp[1]):
                    # 模块对象反射
                    class_obj = getattr(module_obj, temp[1])
                    # 获取类下面的所有方法
                    contents = dir(class_obj)
                    # 把方法都放入字典
                    method_dict = {}
                    # 测试方法所需要的列表
                    test_method = []
                    for content in contents:
                        if content == 'setup':
                            method_dict['setup'] = content
                        if content == 'teardown':
                            method_dict['teardown'] = content
                        if content == 'setup_class':
                            method_dict['setup_class'] = content
                        if content == 'teardown_class':
                            method_dict['teardown_class'] = content
                        if content.startswith('test_'):
                            test_method.append(content)
                            method_dict['test_method'] = test_method
                    c = class_obj()
                    if 'setup_class' in method_dict.keys():
                        if hasattr(c, method_dict['setup_class']):
                            getattr(c, method_dict['setup_class'])()
                    for method_name in method_dict['test_method']:
                        if 'setup' in method_dict.keys():
                            if hasattr(c, method_dict['setup']):
                                getattr(c, method_dict['setup'])()
                        if hasattr(c, method_name):
                            getattr(c, method_name)()
                        if 'teardown' in method_dict.keys():
                            if hasattr(c, method_dict['teardown']):
                                getattr(c, method_dict['teardown'])()
                    if 'teardown_class' in method_dict.keys():
                        if hasattr(c, method_dict['teardown_class']):
                                getattr(c, method_dict['teardown_class'])()


if __name__ == '__main__':
    Start().do_start()