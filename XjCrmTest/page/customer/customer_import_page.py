from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select,WebDriverWait
from page.page import Page
import time
import os

class ImportCustomerPage(Page):
    print()

    #定位器
    import_loc = (By.XPATH,".//*[@id='app']/div[2]/div[1]/div/div[2]/a[2]")
    import_csv_loc = (By.XPATH,".//*[@id='fileUp']")
    import_fromchnel_loc = (By.XPATH,".//*[@id='layui-layer3']/div[2]/div/div[1]/div[2]/form/div/div/div/div/input")
    import_fromchnel_menu_loc = (By.XPATH,".//*[@id='layui-layer5']/div[2]/div/div[1]/div[2]/form/div/div/div/dl/dd[2]")
    import_submit_loc =     (By.XPATH,".//*[@id='layui-layer3']/div[2]/div/div[2]/p/button")

    #初始化“导入客户”页面
    def in_leads_importCustomer(self):
        self.iframe_find(0)
        self.find_element(self.import_loc).click()
        self.iframe_return()

    def import_csvfile(self):
        # time.sleep(2)
        self.iframe_find(0)
        time.sleep(3)
        #方法一：input标签，直接利用send_keys上传
        self.find_element(self.import_csv_loc).send_keys('E:\pyWorks\XjCrmTest\import.csv')
        # self.find_element(self.import_csv_loc).click()
        # time.sleep(1)
        #方法二：非input标签，利用AutoIt工具来上传文件
        # os.system("'E:\pyWorks\XjCrmTest\importxj.exe' 'chrome' 'E:\pyWorks\XjCrmTest\import.csv'")
        # time.sleep(2)
        #等待上传成功弹窗出现

    def import_fromchanel(self):
        # m = self.find_element(self.import_fromchnel_loc)
        m = self.driver.find_element_by_xpath(".// *[ @ id = 'layui-layer3'] / div[2] / div / div[1] / div[2]")
        # m.find_element(self.import_fromchnel_menu_loc).click()
        time.sleep(2)
        m.find_element_by_xpath(".//*[@id='layui-layer5']/div[2]/div/div[1]/div[2]/form/div/div/div/dl/dd[2]").click()
        time.sleep(2)



    def import_submit(self):
       self.find_element(self.import_submit_loc).click()







        # self.iframe_return()











