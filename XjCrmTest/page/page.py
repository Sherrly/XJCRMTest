from selenium.webdriver.support.ui import Select,WebDriverWait

#--------所有页面的基类------
class Page(object):

    base_url = "http://crm.guxiansheng.cn/"


    def __init__(self, driver, url=base_url):
        self.driver = driver
        self.timeout = 30
        self.url = url

    #打开网址
    def open(self):
        self.driver.get(self.url)
        self.driver.implicitly_wait(self.timeout)


    #重新封装find_element方法，主要是为了规划定位器，让find_element方法可以接收一个元祖作为参数
    def find_element(self, loc):
        return self.driver.find_element(*loc)


    #封装方法，为了iframe情况
    def iframe_find(self,num):
        return self.driver.switch_to.frame(num)

    #封装方法，为了返回清空iframe
    def iframe_return(self):
        return self.driver.switch_to.default_content()

    #封装方法，为了句柄留在新的浏览器页面窗口上
    def handles_get(self):
        handles = self.driver.window_handles
        print(handles)
        return self.driver.switch_to.window(self.driver.window_handles[len(handles)-1])


    #静态方法，不用实例化就可以调用该方法，可以忽略(重新封装select的方法)
    @staticmethod
    def select(locator, value):
        select = Select(locator)
        if isinstance(value, int):
            select.select_by_index(value)
        elif isinstance(value, str) and value:
            select.select_by_visible_text(value)
        else:
            select.select_by_index(0)



