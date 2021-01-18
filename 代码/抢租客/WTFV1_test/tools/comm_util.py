import os
import json
import pymysql

# 公共的方法
#


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
            log_time = "..\\logs\\"+module_name+"."+c_time+".log"
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
            cls.logger.error("文件读取失败-->%s" % e)
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
        with open(path, encoding="utf8") as f:
            contents = csv.reader(f)
            for content in contents:
                li.append(content)
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
        except FileNotFoundError as e:
            cls.logger.error("json读取失败-->%s" % e)
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
        # 创建配置器对象
        cp = configparser.ConfigParser()
        cp.read(path, encoding="utf-8")
        contents = cp.items(section)
        return contents

    @classmethod
    def get_ini_value(cls, path, section, option):
        """
        读取ini配置文件通过选项（等号左边的）取里面的内容
        :param path: ini配置文件路径
        :param section: 要读取的节段
        :param option: 要读取的选项
        :return:
        """
        import configparser
        cp = configparser.ConfigParser()
        cp.read(path, encoding='utf8')
        contents = cp.get(section, option)
        # eval内置函数把看起来像具有元组，列表格式的字符串转换为相应的格式
        return eval(contents)

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
        for c in contents:
            dict1[c[0]] = c[1]
        return dict1

    @classmethod
    def get_excel(cls, path, section):
        """
        从excel文件中读取测试信息 配置文件中用对应的要读取的excel信息
        :param path:测试信息配置文件路径及文件名
        :return:测试信息的json格式
        """
        import xlrd
        test_info = cls.trans_ini_tuple_to_dict(path, section)

        workbook = xlrd.open_workbook(test_info["test_data_path"])
        table = workbook.sheet_by_name(test_info["sheet_name"])
        list1 = []
        for i in range(int(test_info["start_row"]), int(test_info["end_row"])):
            params = table.cell_value(i, int(test_info["data_col"]))
            temp = {}
            t1 = str(params).split("\n")
            for t in t1:
                p_v = t.split("=")
                temp[p_v[0]] = p_v[1]
            temp["expect"] = table.cell_value(i, int(test_info["expect_col"]))
            list1.append(temp)
        return list1


class DBUtil:
    logger = LogUtil.get_logger("DBTools")

    @classmethod
    def get_conn(cls):
        """
        连接数据库返回数据库连接对象
        :return:数据库连接对象
        """
        # 配置文件读取配置信息
        db_info = FileUtil.get_ini_value("..\\conf\\base.ini", 'db_info', 'db_conn_info')
        try:
            dbconn = pymysql.connect(host=db_info[0],
                                     port=int(db_info[1]),
                                     user=db_info[2],
                                     password=db_info[3],
                                     database=db_info[4],
                                     charset='utf8')
            cursor = dbconn.cursor()
            cls.logger.info("数据库连接成功")
            return cursor
        except Exception as e:
            cls.logger.error("数据库连接失败-->%s" % e)

    def sql_execute(self, sql):
        """
        SQL语句执行
        :return: 语句执行完返回的结果
        """
        cursor = self.get_conn()
        cursor.execute(sql)
        consequence = cursor.fetchall()
        return consequence

    def query_one(self, sql):
        """
        查询一条结果
        :param sql: 查询语句
        :return: 单条结果集，以元组方式返回
        """

        pass

    def updata_db(self, sql):
        """
        增删改操作
        :param sql: DML语句
        :return:执行成功或失败的标记
        """
        pass


if __name__ == '__main__':
    print(FileUtil.get_txt('..\\kwdriver\\keyword_scrip.conf'))
    # print(FileUtil.get_ini_value("..\\conf\\base.ini", 'db_info', 'db_conn_info'))

