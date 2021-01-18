import os
from WTFV1_test.tools.comm_util import LogUtil


class Collection:

    logger = LogUtil.get_logger(os.path.join(os.getcwd(), 'collection'))
    driver = None

    @classmethod
    def do_get_driver(cls, browser):
        """
        关键字“打开浏览器”操作
        :param browser: 浏览器
        """
        from selenium import webdriver
        if cls.driver is None:
            if hasattr(webdriver, browser):
                cls.driver = getattr(webdriver, browser)()
            else:
                cls.logger.error("浏览器名称不正确")
                cls.driver = webdriver.Chrome
        cls.driver.maximize_window()
        # cls.driver.set_window_size(1000, 30000)

    @classmethod
    def do_open(cls, url):
        """
        关键字“获取页面”操作
        :param url: url
        """
        cls.driver.get(url)

    @classmethod
    def get_element(cls, attr):
        """
        获取元素方法
        :param attr: 例如（ID=name）
        :return: 获取的元素对象
        """
        attr = str(attr).split('='[0])
        from selenium.webdriver.common.by import By
        if hasattr(By, attr[0]):
            return cls.driver.find_element(getattr(By, attr[0]), attr[1])
        else:
            return None

    @classmethod
    def do_input(cls, attr, value):
        """
        关键字“输入”方法
        :param attr: 获取元素
        :param value: 输入的值
        """
        element = cls.get_element(attr)
        if element is not None:
            element.click()
            element.clear()
            element.send_keys(value)
        else:
            cls.logger.error('元素没找到')

    @classmethod
    def do_click(cls, attr):
        """
        关键字“点击”方法
        :param attr: 获取元素
        """
        element = cls.get_element(attr)
        if element is not None:
            element.click()
        else:
            cls.logger.error('元素没找到')

    @classmethod
    def do_sleep(cls, wt):
        """
        关键字“等待”方法
        :param wt: 等待时间
        """
        wt = int(wt)
        import time
        time.sleep(wt)

    @classmethod
    def do_close(cls):
        """
        关键字“关闭浏览器”方法
        """
        cls.driver.close()

    @classmethod
    def do_confirm(cls):
        """
        关键词“确认”方法
        """
        cls.driver.switch_to.alert.accept()

    @classmethod
    def do_refresh(cls):
        """
        关键字“刷新”方法
        """
        cls.driver.refresh()

    @classmethod
    def do_quit(cls):
        """
        关键词“退出”方法
        :return:
        """
        cls.driver.quit()

    @classmethod
    def do_roll_click(cls, attr):
        attr = str(attr).split('='[0])
        from selenium.webdriver.common.by import By
        if hasattr(By, attr[0]):
            element = cls.driver.find_element(getattr(By, attr[0]), attr[1])
            js_code = "arguments[0].scrollIntoView();"
            cls.driver.execute_script(js_code)
            element.click()

    @classmethod
    def do_roll_input(cls, attr, value):
        js_code = "arguments[0].scrollIntoView();"
        element = cls.get_element(attr)
        if element is not None:
            cls.driver.execute_script(js_code, element)
            element.click()
            element.clear()
            element.send_keys(value)
        else:
            cls.logger.error('元素没找到')










