import smtplib,os,time
from selenium import  webdriver
from email.mime.text import MIMEText #定义邮件正文MIMEText()
from email.header import Header      #定义邮件标题Header()
import xlrd
import pymysql



#---------------发送测试报告到邮箱----------------------
def send_mail(smtp_dict, report):
    """
    smpt_dict = {
        "smtp_server": "发送邮件的smtp eg:smtp.126.com",
        "send_user": "发送邮件的邮箱 eg:admin@126.com",
        "send_pwd": "发送邮件的邮箱密码 eg：123456",
        "sender": "用于显示收到邮件的发件人 eg:admin@126.com",
        "receiver": "收件人邮箱 eg：zhangsan@sina.cn 多个s收件人用list[,,,]",
        "subject": "邮件的主题 eg:邮件自动化测试主题"
    }: 
    """


    #获取测试报告的内容
    file_result = open(report, "rb")
    mail_body = file_result.read()
    file_result.close()

    #组装邮件的内容格式
    msg = MIMEText(mail_body,'html','utf-8')#编写HTML类型的邮件的正文
    msg['Subject'] = Header(smtp_dict["subject"],'utf-8')
    msg['From'] = smtp_dict["send_user"]

    #发送邮件
    try:
        smtp = smtplib.SMTP()
        smtp.connect(smtp_dict["smtp_server"])
        smtp.login(smtp_dict["send_user"],smtp_dict["send_pwd"])
        smtp.sendmail(smtp_dict["sender"],smtp_dict["receiver"],msg.as_string())
    except smtplib.SMTPException as sme:
        print("邮件发送失败！")
        print(sme)



#-----------------测试用例再执行过程中的截图------------
def screen_shot(driver,filename):
    top_dir = "./report/image/"
    times = time.strftime("%Y%m%d%H%M%S")
    image_file = top_dir + times + filename + ".png"
    driver.get_screenshot_as_file(image_file)



#-----------------读取excel中的数据，组装为字典---------
def excel_data(file, sheet_name):
    """
    ex：
      user    pwd     assert
      nemo    123     sucess
      nemo    321     fail
    :return: [{'user': 'nemo', 'pwd': 123.0, 'islogin': 'success'},{'user': 'nemo', 'pwd': '', 'islogin': 'failed'}]
    """
    data = xlrd.open_workbook(file)        #打开一个excel
    table = data.sheet_by_name(sheet_name) #获取工作表，通过sheet名称打开
    excel_list = []                        #用于存储格式转换后的存储一个个字典的列表
    header_row = table.row_values(0)       #获取表格整行整列的值
    for n_row in range(1,table.nrows):
        excel_list.append(dict(zip(header_row,table.row_values(n_row))))
    return excel_list



#------------获取当前文件目录的n层上级目录------------
def parent_path(n):
    current_path = os.getcwd()#获取当前目录
    #拼接上级目录字符串
    p = ".."
    li = []
    if n > 1:
        for i in  range(n):
            li.append(p)
        p = "/".join(li)
        p_path = os.path.abspath(os.path.join(current_path,p))
    elif n == 1:
        p_path = os.path.abspath(os.path.join(current_path,p))
    else:
        p_path = os.path.abspath(current_path)
    return p_path




#-----通过数据库获取所有数据，返回的sql中能查询所有数据----
def mysql_data(config, sql):
    """
    :param 
    config = {                                             
        'host': '127.0.0.1',
        'port': 3306,
        'user': 'root',
        'password': 'root',
        'db': 'gxscrm',
        'charset': 'utf8mb4',
        'cursorclass': pymysql.
        #加上这个参数会将查询结果变为[{"key":"value",......},{},{},{}]
    }
    sql = "SELECT * FROM customer_employee"
    :return: 
    count,语句执行的条数
    all_data,fetchall,也就是通过sql语句能查出的所有数据((),()),是一个二维元祖
    """

    db = pymysql.connect(**config)#打开数据库连接
    try:
        cur = db.cursor()            #使用cursor()方法获取操作游标
        cur.execute(sql)             #执行sql语句
        all_data = cur.fetchall()    #获取数据库中的所有数据
    except pymysql.err.DatabaseError as de:
        print(de)
    finally:
        db.close()
    return all_data




