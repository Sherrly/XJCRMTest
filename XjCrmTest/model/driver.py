from selenium import  webdriver

def set_browser(browser_name = "chrome"):
    #浏览器选择：启动不同的浏览器选择对应的浏览器
    if browser_name.lower() == "ie":
        driver = webdriver.Ie()
        return driver
    elif browser_name.lower() == "firefox":
        driver = webdriver.Firefox(executable_path= 'E:\pyWorks\XjCrmTest\webDrivweCHandFir\geckodriver.exe')
        return driver
    elif browser_name.lower() == "chrome":
        driver = webdriver.Chrome(executable_path= 'E:\pyWorks\XjCrmTest\webDrivweCHandFir\chromedriver.exe')
        return driver
    elif browser_name.lower() == "phantomjs":
        driver = webdriver.PhantomJS()
        return driver
    else:
        raise NameError("浏览器名称错误！请输入正确的浏览器名称，类似ie，chrome，firefox等且不用区分大小写！")
