from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from page.page import Page
import time

#--------新建客户页面----------
class CreatCustomerPage(Page):

    #定位器
    creatCustomer_loc = (By.XPATH,".//*[@id='app']/div[2]/div[1]/div/div[2]/a[1]")#【新增客户】按钮
    add_name_loc = (By.XPATH,".//*[@id='app']/div/div[1]/div[2]/div[1]/div/div/input")
    add_phone_loc = (By.XPATH,".//*[@id='app']/div/div[1]/div[2]/div[3]/div/div[1]/input")
    add_frome_loc = (By.XPATH,".//*[@id='app']/div/div[1]/div[2]/div[7]/div/div/div[20]/i")
    add_submit_loc = (By.XPATH,".//*[@id='app']/div/div[4]/button[2]")
    add_cancel_loc = (By.XPATH,".//*[@id='app']/div/div[4]/button[1]")
    #弹框“下次再说”按钮元素定位
    add_next_time_loc = (By.XPATH,".//*[@id='layui-layer1']/div[3]/a[1]")


    #初始化新增客户页面
    def in_leads_createCustomer(self):
        time.sleep(1)
        #找到元素对应的iframe
        self.iframe_find(0)
        self.find_element(self.creatCustomer_loc).click()
        self.iframe_return()

    #新建客户对应元素的方法
    def addName(self,text):
        self.find_element(self.add_name_loc).send_keys(text)
    def addPhone(self,text):
        self.find_element(self.add_phone_loc).send_keys(text)
    def addFrome(self):
        self.find_element(self.add_frome_loc).click()
    #提交按钮
    def addSubmit(self):
        self.find_element(self.add_submit_loc).click()
    #取消按钮
    def cancel(self):
        self.iframe_find(0)
        self.find_element(self.add_cancel_loc).click()
    #弹框上的“下次再说”按钮
    def next_time(self):
        self.iframe_find(0)
        self.find_element(self.add_next_time_loc).click()
        self.iframe_return()
    #“提交”按钮
    def submit(self, name, phone):
        self.iframe_find(0)
        self.addName(name)
        self.addPhone(phone)
        self.addFrome()
        self.addSubmit()
        self.iframe_return()



