import unittest, time
from HTMLTestRunner import HTMLTestRunner
from model.function import send_mail,screen_shot

test_dir = "./testcase"
test_report = "./report"


#使用discover组织测试用例
discover = unittest.defaultTestLoader.discover(test_dir, pattern="customer_case_base.py")

if __name__ == '__main__':

    # 格式化当前日期
    times = time.strftime("%Y%m%d%H%M%S")
      # 组装测试报告路径和文件名
    report_file = test_report + "/WCM3.0" + times + "result.html"
    file = open(report_file, 'wb')
      # 实例化测试报告
    runner = HTMLTestRunner(stream=file,
                              title="Athena金融云数据CRM3.0自动化测试报告",
                              description="运行环境：window 10， Chrome")
    #执行测试
    # runner = unittest.TextTestRunner()
    print(discover)
    runner.run(discover)
    file.close()
    # send_mail(report_file)
