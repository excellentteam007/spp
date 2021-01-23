import os
import json
import pymysql


"""
公共的方法
"""


class TimeUtil:
    """
    关于时间的方法
    """

    @classmethod
    def get_time_file(cls):
        """
        读取当前时间
        :return: 时间字符串
        """
        import time
        return time.strftime('%Y.%m.%d-%H.%M.%S', time.localtime())


class LogUtil:
    # 单例模式
    logger = None

    @classmethod
    def get_logger(cls, module_name):
        """
        获取logger对象  module_name一般可以放调用该对象的模块的字符串名称
        普通有4种信息级别：error,warn,info,debug
        判断logs路径是否存在，如果不存在则创建它
        """
        import logging
        if cls.logger is None:
            cls.logger = logging.getLogger(module_name)
            cls.logger.setLevel("INFO")
            if not os.path.exists('..\\logs'):
                os.mkdir('..\\logs')
            # 获取时间字符串
            c_time = TimeUtil.get_time_file()
            # 拼接日志文件的名称
            log_time = "..\\logs\\" + module_name + "." + c_time + ".log"
            # 创建句柄，用于和文件的关联
            handle = logging.FileHandler(log_time, encoding="utf-8")
            # 定义日志信息的保存格式
            formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            # 句柄具有规定的格式
            handle.setFormatter(formatter)
            cls.logger.addHandler(handle)
            cls.logger.info(
                '--------------------------------------------------------------\n')
        return cls.logger


class FileUtil:
    logger = LogUtil.get_logger("GetFileTools")

    @classmethod
    def get_version(cls, path, sheet):
        """
        获取测试系统的版本号
        :param path: 测试路径
        :param sheet: sheet页
        :return: 版本号的值
        """
        import xlrd
        workbook = xlrd.open_workbook(path)
        sheet_content = workbook.sheet_by_name(sheet)
        return sheet_content.cell_value(1, 1)

    @classmethod
    def get_txt(cls, path):
        """
        读取普通文本文件内容，返回字符串
        :param path: 文本文件路径
        :return: 文本文件内容字符串
        # """
        li = []
        try:
            with open(path, "r", encoding="utf-8")as f:
                contents = f.readlines()
                for content in contents:
                    li.append(content.strip())
        except Exception as e:
            cls.logger.error(f"文件{path}读取失败-->{e}")
        return li

    @classmethod
    def get_csv(cls, path):
        """
        读取csv文件
        :param path: 文件路径
        :return: 结果列表套列表，
        """
        import csv
        li = []
        try:
            with open(path, encoding="utf8") as f:
                contents = csv.reader(f)
                for content in contents:
                    li.append(content)
        except Exception as e:
            cls.logger.error(f"读取{path}错误-->{e}")
        return li

    @classmethod
    def get_json(cls, path):
        """
        从json格式文件中读取原始格式内容并返回
        :param path:要读取的json文件路径
        :return:原始数据类型的数据
        """
        contents = None
        try:
            with open(path, "r", encoding="utf-8")as f:
                contents = json.load(f)
        except Exception as e:
            cls.logger.error(f"json{path}读取失败-->{e}")
        return contents

    @classmethod
    def get_ini_by_section(cls, path, section):
        """
        读取ini配置文件
        :param path: 配置文件路径
        :param section: 要读取的节段
        :return:列表套元组的格式
        """
        import configparser
        contents = None
        try:
            # 创建配置器对象
            cp = configparser.ConfigParser()
            cp.read(path, encoding="utf-8")
            contents = cp.items(section)
        except Exception as e:
            cls.logger.error(f"读取{path}的{section}节点错误-->{e}")

        return contents

    @classmethod
    def get_ini_value(cls, path, section, option):
        """
        读取ini配置文件通过选项（等号左边的）取里面的内容
        :param path: ini配置文件路径
        :param section: 要读取的节段
        :param option: 要读取的选项
        :return:文件中节点下对应选项的值的原始数据
        """
        import configparser
        cp = configparser.ConfigParser()
        content = None
        try:
            cp.read(path, encoding='utf8')
            contents = cp.get(section, option)
            # eval内置函数把看起来像具有元组，列表格式的字符串转换为相应的格式
            content = eval(contents)
        except Exception as e:
            cls.logger.error(f"读取文件{path}下{section}节点下{option}错误-->{e}")
        return content

    @classmethod
    def trans_ini_tuple_to_dict(cls, path, section):
        """
        把读取的ini的列表套元组的格式转换成字典格式
        :param path: 配置文件路径
        :param section:要读取的节段
        :return: 字典格式
        """
        contents = cls.get_ini_by_section(path, section)
        dict1 = {}
        try:
            for c in contents:
                dict1[c[0]] = c[1]
        except Exception as e:
            cls.logger.error(f"ini的列表套元组的格式转换成字典格式-->{e}")
        return dict1

    @classmethod
    def get_excel(cls, path, section):
        """
        从excel文件中读取测试信息 配置文件中用对应的要读取的excel信息
        :param path:测试信息配置文件路径及文件名
        :param section: 对应功能的节点名
        :return:测试信息的json格式
        """
        import xlrd
        # 读取配置文件
        test_info = cls.trans_ini_tuple_to_dict(path, section)
        # 打卡excel文件通过路径
        workbook = xlrd.open_workbook(test_info["test_data_path"])
        # 找到对应的sheet
        contents = workbook.sheet_by_name(test_info["sheet_name"])
        list1 = []
        # 开始的行到结束的行遍历
        for i in range(int(test_info["start_row"]), int(test_info["end_row"])):
            temp1 = {}
            temp1["case_id"] = contents.cell_value(i, 0)
            temp1["module_name"] = contents.cell_value(i, 1)
            temp1["test_type"] = contents.cell_value(i, 2)
            temp1["api_uri"] = contents.cell_value(i, 3)
            temp1["request_method"] = contents.cell_value(i, 4)
            temp1["case_desc"] = contents.cell_value(i, 5)
            # 对测试用例数据单独处理
            data = contents.cell_value(i, 6)
            data_dict = {}
            if data != '':
                t1 = str(data).split("\n")
                for t in t1:
                    t = t.split("=")
                    data_dict[t[0]] = t[1]
            temp1["case_params"] = data_dict
            temp1["expect"] = contents.cell_value(i, 7)
            list1.append(temp1)
        return list1


class DBUtil:
    logger = LogUtil.get_logger("DBTools")

    def __init__(self, option):
        """
        :param option: 配置文件中db_info节点下的键
        """
        self.option = option

    def get_conn(self):
        """
        连接数据库返回数据库连接对象
        :return:数据库连接对象
        """
        # 配置文件读取配置信息
        db_info = FileUtil.get_ini_value("..\\conf\\base.ini", 'db_info', self.option)
        conn = None
        try:
            conn = pymysql.connect(host=db_info[0],
                                   port=int(db_info[1]),
                                   user=db_info[2],
                                   password=db_info[3],
                                   database=db_info[4],
                                   charset='utf8')
        except Exception as e:
            self.logger.error("数据库连接失败-->%s" % e)
        return conn

    def sql_execute(self, sql):
        """
        执行SQL语句返回元组格式
        :param sql: sql语句
        :return: 元组格式
        """
        conn = self.get_conn()
        result = None
        if conn is not None:
            # 生成游标对象
            cursor = conn.cursor()
            try:
                # 执行sql语句
                cursor.execute(sql)
                # 获取查询结果
                result = cursor.fetchall()
            except Exception as e:
                self.logger.error(f"{sql}语句错误，执行失败-->{e}")
            # 关闭游标
            cursor.close()
        else:
            self.logger.error('数据库连接错误')
        # 关闭数据库
        conn.close()
        return result

    def updata_db(self, sql):
        """
        添加数据到数据库的方法
        :param sql: sql语句
        :return: False或者True
        """
        flag = False
        conn = self.get_conn()
        if conn is not None:
            cursor = conn.cursor()
            try:
                cursor.execute(sql)
                # 提交事务（不提交不会完成添加）
                conn.commit()
                flag = True
            except Exception as e:
                self.logger.error(f'{sql}语句错误，执行失败-->{e}')
            cursor.close()
        else:
            self.logger.error('数据库连接失败')
        conn.close()
        return flag


class Common:

    @classmethod
    def get_screenshot(cls, driver, version):
        """
        截取当前屏幕的并返回图片路径
        :param driver: 用的selenium里面的方法截图，要一个driver
        :param version: 被测系统的版本
        :return: 截图路径
        """
        if not driver is None:
            screenshot_path = f'../report/{version}/screenshot'
            if not os.path.exists(screenshot_path):
                os.makedirs(screenshot_path)
            image_name = screenshot_path + str(TimeUtil.get_time_file()) + '.png'
            driver.get_screenshot_as_file(image_name)
        else:
            image_name = '无'
        return image_name


class CustomAssert:

    logger = LogUtil.get_logger('util')

    def __init__(self, version, table, driver=None):
        """
        :param version: 测试的版本号
        :param table: 数据库的表名
        :param driver: 下面需要的一个driver
        """
        self.driver = driver
        self.version = version
        self.table = table
        self.db = DBUtil('db_conn_result_info')

    def write_result_to_db(self, info, result_msg, error_msg, error_img_path):
        """
        写测试数据结果到数据库
        :param info: 测试的信息
        :param result_msg: 测试结果信息
        :param error_msg: 测试的错误信息
        :param error_img_path: 错误的截图路径
        """
        case_id = info['case_id']
        module_name = info['module_name']
        test_type = info['test_type']
        api_url = info['api_uri']
        request_method = info['request_method']
        case_desc = info['case_desc']
        case_params = info['case_params']
        expect = info['expect']
        sql = f""" insert into {self.table}(case_version,case_id,module_name,
                    test_type,api_url,request_method,case_desc,case_params,expect,
                    result_msg,error_msg,error_img_path) 
                    values ("{self.version}","{case_id}","{module_name}","{test_type}",
                    "{api_url}","{request_method}","{case_desc}","{case_params}",
                    "{expect}","{result_msg}","{error_msg}","{error_img_path}");"""
        if not self.db.updata_db(sql):
            self.logger.error('sql执行错误')

    def error(self, info):
        """
        错误的断言
        :param info: 测试的信息
        """
        result_msg = 'test_error'
        error_img_path = Common.get_screenshot(self.driver, self.version)
        self.write_result_to_db(info, result_msg, info['error_msg'], error_img_path)

    def equal(self, actual, info):
        """
        相等的断言
        :param actual: 实际的结果
        :param info: 测试的信息
        """
        import time
        if info['expect'] == actual:
            result_msg = 'test_pass'
            error_msg = '无'
            error_img_path = '无'
        else:
            result_msg = 'test_fail'
            error_msg = '无'
            error_img_path = Common.get_screenshot(self.driver, self.version)
            time.sleep(1)
        self.write_result_to_db(info, result_msg, error_msg, error_img_path)

    def contain(self, actual, info):
        """
        包含的断言，实际结果包括预期结果
        :param actual: 实际结果
        :param info: 测试信息
        """
        if info['expect'] in actual:
            result_msg = 'test_pass'
            error_msg = '无'
            error_img_path = '无'
        else:
            result_msg = 'test_fail'
            error_msg = '无'
            error_img_path = Common.get_screenshot(self.driver, self.version)
        self.write_result_to_db(info, result_msg, error_msg, error_img_path)


if __name__ == '__main__':
   print(FileUtil.get_excel('..\\data\\api_case_data_conf.ini', 'login'))