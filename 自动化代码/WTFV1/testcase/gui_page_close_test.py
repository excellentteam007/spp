from WTFV1.tools.ui_util import UiUtil


class GuiCloseTest:

    def test_cloes(self):
        driver = UiUtil.get_driver()
        driver.close()


