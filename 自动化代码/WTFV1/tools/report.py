from WTFV1.tools.comm_util import DBUtil, LogUtil, TimeUtil


class Report:
    # 日志对象
    logger = LogUtil.get_logger('report')
    # 数据库对象
    db = DBUtil('db_conn_result_info')

    @classmethod
    def generate_html_test_report(cls, table, version, app_name):
        """
        把数据库的内容写到HTML文件中
        :param table: 数据库的表名
        :param version: 版本号
        :param app_name: 报告
        """
        # 获取当前版本的所有数据
        sql = f'select * from {table} where case_version = "{version}"'
        result = cls.db.sql_execute(sql)
        if len(result) == 0:
            cls.logger.info('没有该版本的测试结果')
            return
        # 打开HTML模板
        with open('..\\tools\\template.html', encoding='utf8') as rf:
            contents = rf.read()
            base_sql = f'select count(*) from {table} where case_version = "{version}" and result_msg='

            # 统计pass fail error 的个数的sql语句
            count_success_sql = base_sql + "\"test_pass\""
            count_fail_sql = base_sql + "\"test_fail\""
            count_error_sql = base_sql + "\"test_error\""
            # 统计pass fail error 的个数
            count_success = cls.db.sql_execute(count_success_sql)[0][0]
            count_fail = cls.db.sql_execute(count_fail_sql)[0][0]
            count_error = cls.db.sql_execute(count_error_sql)[0][0]
            # 获取执行的时间
            last_time_sql = f"""SELECT case_time FROM {table} where case_version="{version}" 
                                ORDER BY  case_time DESC LIMIT 0,1"""
            last_time = cls.db.sql_execute(last_time_sql)[0][0]
            test_data = str(last_time).split(' ')[0]
            test_time = str(last_time).split(' ')[1]

            # 对固定的内容进行替换
            contents = contents.replace('$test-date', test_data)
            contents = contents.replace('$test-version', version)
            contents = contents.replace('$pass-count', str(count_success))
            contents = contents.replace('$fail-count', str(count_fail))
            contents = contents.replace('$error-count', str(count_error))
            contents = contents.replace('$last-time', test_time)
            test_result = ''
            for content in result:
                if content[10] == 'test_pass':
                    color = 'green'
                elif content[10] == 'test_fail':
                    color = 'yellow'
                else:
                    color = 'red'

                test_result += f"""<tr height="40">
                                    <td width="7%">{str(content[0])}</td>
                                    <td width="9%">{content[3]}</td>
                                    <td width="9%">{content[4]}</td>
                                    <td width="7%">{content[2]}</td>
                                    <td width="20%">{content[7]}</td>
                                    <td width="7%" bgcolor={color}>{content[10]}</td>
                                    <td width="16%">{content[11]}</td>
                                    <td width="15%">{content[12]}</td>
                                    <td width="10%"><a href={content[13]}>查看截图</a></td>
                                </tr>"""
            contents = contents.replace('$test-result', test_result)

            # 写HTML文件
            report_name = f'../report/{app_name}{version}版测试报告_{TimeUtil.get_time_file()}.html'
            with open(report_name, 'w', encoding="utf8") as wf:
                wf.write(contents)


if __name__ == '__main__':
    Report.generate_html_test_report('spp_test_result', 'v1.0', 'spp')


