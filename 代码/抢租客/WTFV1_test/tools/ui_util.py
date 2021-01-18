import os
from pykeyboard import PyKeyboard
from pymouse import PyMouse


class UiUtil:
    """
    GUI自动化的工具方法
    """

    from WTFV1_test.tools.comm_util import LogUtil
    logger = LogUtil.get_logger(os.path.join(os.getcwd(), 'ui_util'))
    driver = None
    keyboard = PyKeyboard()
    mouse = PyMouse()

    def __init__(self):
        pass

    @classmethod
    def get_driver(cls, browser="Chrome"):
        """
        webdriver封装，默认“Chrome”
        :param browser: 浏览器。可以为（Chrome，Firefox,Ie,Edge）
        :return: driver
        """
        from selenium import webdriver
        if cls.driver is None:
            try:
                cls.driver = getattr(webdriver, browser)()
            except Exception as e:
                cls.logger.error('输入不正确，使用了默认谷歌浏览器->%s' % e)
                cls.driver = webdriver.Chrome
        cls.driver.implicitly_wait(3)
        cls.driver.maximize_window()
        cls.driver.get("http://172.16.9.86:18080/SharedParkingPlace/")
        return cls.driver

    @classmethod
    def match_image(cls, target):
        """
        通过opencv库对图像的识别，通过模板图片（小图），和全屏图（大图）进行算法对比
        :param target: 模板图片的名字
        :return: 图片中心位置的坐标
        """
        from PIL import ImageGrab
        import cv2
        image_path = "..\\image"
        screen_path = os.path.join(image_path, 'screen.png')
        # 对大图进行截图，并保存在指定路径
        ImageGrab.grab().save(screen_path)
        # 读取大图
        screen = cv2.imread(screen_path)
        # 读取小图
        template = cv2.imread(os.path.join(image_path, target))
        # 调用匹配算法
        result = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
        # 获取坐标
        min, max, min_loc, max_loc = cv2.minMaxLoc(result)
        # 计算矩形十字中心点坐标
        x = max_loc[0] + int(template.shape[1]/2)
        y = max_loc[1] + int(template.shape[0]/2)
        return x, y

    @classmethod
    def click_image(cls, target):
        """
        找到这个图片单击这个图片
        :param target: 图片名字
        """
        x, y = cls.match_image(target)
        if x == -1 or y == -1:
            cls.logger.error(f"没有找到{target}的图片")
            return
        cls.mouse.click(x, y)

    @classmethod
    def double_click_image(cls, target):
        """
        找到这个图片双击这个图片
        :param target: 图片名字
        """
        x, y = cls.match_image(target)
        if x == -1 or y == -1:
            cls.logger.error(f"没有找到{target}的图片")
            return
        cls.mouse.click(x, y, n=2)

    @classmethod
    def input_image(cls, target, msg):
        """
        找到输入框图片在里面输入内容
        :param target: 图片名字
        :param msg: 输入的内容
        """
        x, y = cls.match_image(target)
        if x == -1 or y == -1:
            cls.logger.error(f'没有找到{target}的图片')
            return
        cls.keyboard.type_string(msg)

    @classmethod
    def select_image(cls, target, count):
        """
        找到下拉框图片，点击一下，然后通过按下键选择一个
        :param target: 图片名字
        :param count:循环几次
        """
        cls.click_image(target)
        for i in range(count):
            cls.keyboard.press_key(cls.keyboard.down_key)
        cls.keyboard.press_key(cls.keyboard.enter_key)

    def find_element(self, driver, elment_attr):
        """
        自己写的找元素的方法，通多find_element（定位方式，定位方式对应的内容）
        :param driver: 需要的一个webdriver
        :param elment_attr: 提取的页面元素配置文件的信息，里面内容是（定位方式，定位方式对应的内容）
        :return:元素的对象
        """
        from selenium.webdriver.common.by import By
        return driver.find_element(getattr(By, elment_attr[0]), elment_attr[1])

    def input(self, element, value):
        """
        输入框找到，点击，清空，输入内容
        :param element:页面上的输入框元素
        :param value:给输入框输入的值
        """
        element.click()
        element.clear()
        element.send_keys(value)

    def click(self, element):
        """
        找到元素点击
        :param element:要单击的元素
        """
        element.click()

    def select_drop_down_box(self, element, value):
        """
        下拉框选择元素
        :param element: 下拉框的元素
        :param value: 要选择的下拉框元素
        """
        from selenium.webdriver.support.select import Select
        myselect = Select(element)
        myselect.select_by_visible_text(value)

    def select_by_js(self, driver, element):
        """
        通过js代码找到选择需要滚动鼠标中键才能找到的元素
        :param element: 页面上的元素
        """
        js_code = 'arguments[0].scrollIntoView();'
        driver.execute_script(js_code, element)
        element.click()

    def get_text(self,element):
        """
        :param element: 页面上的元素
        :return: 页面元素的文本内容
        """
        return element.text

    def skip_iframe(self, driver, element):
        """
        跳转iframe
        :param element: iframe定位
        """
        driver.switch_to.frame(element)

    def select_date(self):
        pass

class GetDesignatedPageElement:
    """
    找指定页面的元素
    """

    def __init__(self, driver, attr_path, section):
        """
        :param driver: 浏览器驱动
        :param attr_path: 配置文件路径
        :param section: 节点名字
        """
        from WTFV1_test.tools.comm_util import FileUtil
        self.driver = driver
        self.ele = FileUtil.trans_ini_tuple_to_dict(attr_path, section)
        self.ui = UiUtil()

    def get_element(self, option):
        """
        找到指定页面的元素定位方式
        :param option: 键
        :return: 找到的元素对象
        """
        attr = eval(self.ele[option])
        return self.ui.find_element(self.driver, attr)





if __name__ == '__main__':
   UiUtil.input_image("wyy.lllllpng", "lllll")