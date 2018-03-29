from selenium.webdriver.common.by import By
from page.page import Page
import time

class  SearchCustomer(Page):

    #定位器
    search_mark_loc = (By.XPATH,".//*[@id='app']/div[2]/div[2]/div/div[1]/ul/li[7]/a")
    # search_tag_loc  = (By.XPATH,".//*[@id='app']/div[2]/div[2]/div/div[2]/ul/li[23]/a")


    #将元素定义成方法

    def serch_mark(self):
        print("mark备注搜索搜索")
        time.sleep(10)
        self.find_element(self.search_mark_loc).click()


    # def search_tag(self):
    #     # self.find_element(self.search_tag_loc).click()
    #     print("为什么定位不到a标签的值呢")

