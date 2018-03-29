from selenium.webdriver.common.by import By
from .page import Page

class LoginPage(Page):

    #指定当前页面的url
    #url = "http://crm.guxiansheng.cn"

    #定位器
    login_username_text_loc = (By.NAME, "loginusername")
    login_password_text_loc = (By.NAME,"loginpassword")
    login_button_loc = (By.CLASS_NAME,"layui-btn")


    #将元素的操作都定义为方法
    def login_username(self, text):
        """账号"""
        self.find_element(self.login_username_text_loc).clear()
        self.find_element(self.login_username_text_loc).send_keys(text)

    def login_password(self, text):
        """密码"""
        self.find_element(self.login_password_text_loc).clear()
        self.find_element(self.login_password_text_loc).send_keys(text)

    def login_button(self):
        """登录按钮"""
        self.find_element(self.login_button_loc).click()

    #登录操作
    def login(self,username, password):
        self.login_username(username)
        self.login_password(password)
        self.login_button()
