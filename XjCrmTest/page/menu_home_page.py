
from selenium.webdriver.common.by import By
from page.page import Page
import time

class MenuHomePage(Page):

    #指定当前路径为：http://crm.guxiansheng.cn/admin/index/index

    #定位器
    home_customer_loc = (By.PARTIAL_LINK_TEXT,"客户管理")
    home_Approval_loc = (By.PARTIAL_LINK_TEXT,"客户审批")
    home_product_loc = (By.PARTIAL_LINK_TEXT,"产品管理")

    #将元素定义成方法
    def in_leads_customerhome(self):
        time.sleep(3)
        self.find_element(self.home_customer_loc).click()









