from  testcase import test_case_base
from page.menu_home_page import MenuHomePage
from page.customer.customer_search_page import SearchCustomer
from page.customer.customer_create_page import CreatCustomerPage
from page.customer.customer_import_page import ImportCustomerPage
import unittest
import time,os

class CustomerBaseCase(test_case_base.MyTest, MenuHomePage,SearchCustomer,CreatCustomerPage,ImportCustomerPage):

    #初始化进入客户列表页面

    """客户列表模块"""
    def setUp(self):
        self.in_leads_customerhome()

    #case1.新增客户用例
    def test_case_createCustomer(self):
        self.in_leads_createCustomer()
        time.sleep(3)
        self.submit("女神999","17070001000")
        time.sleep(3)
        self.next_time()


    # case2.导入客户用例(上传csv)
    def test_case_importCustomer(self):
        print('22222222')
        time.sleep(3)
        self.handles_get()
        self.in_leads_importCustomer()
        self.import_csvfile()
        # self.import_fromchanel()
        # self.import_submit()

    # def test_case_deleteCustomer(self):
    #     print("删除客户")
    # def test_case_shareCustomer(self):
    #     print("共享客户")
    # def test_case_moveToPoolCustomer(self):
    #     print("移入公海")
    # def test_case_searchCustomer(self):
    #     print("搜索客户")
    #     self.serch_mark()
        # self.search_tag()

    # -------------销毁清除进程------------------
    # def tearDown(cls):
    #     # os.system('taskkill -f -im chromedriver.exe')
    #     # os.system('taskkill -f -im chrome.exe')
    #     cls.driver.quit()

    if __name__ == '__main__':
       unittest.main()