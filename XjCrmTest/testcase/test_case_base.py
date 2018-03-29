import unittest,time
from model.driver import set_browser
from page.login_page import LoginPage
from model.function import screen_shot

#--------测试用例的基类-----------
class MyTest(unittest.TestCase):

    driver = set_browser()
    login_data = ("xj002","123456")

    @classmethod
    def setUpClass(cls):

        screen_shot(cls.driver,"rrr")

        cls.driver.maximize_window()

        #初始化直接登录
        login = LoginPage(cls.driver)
        login.open()
        time.sleep(3)
        login.login(*cls.login_data)
        time.sleep(5)









