
__author__ = "wjj"
# =========================================
#     用来处理列表页中的table
# =========================================

from selenium.webdriver.common.by import By


class Table(object):

    def __init__(self, driver):
        self.driver = driver

    def row_cell_get_table_text(self, locator, row, cell):
        """
        根据输入的行列值，获取该行列单元格中的文本。
        :param locator: 定位到table的定位语句
        :param row: 行
        :param cell: 列
        :return: 单元格文本
        """
        # cell = str(cell)
        # row = str(row + 1)
        locator = "%s/tbody/tr[%s]/td[%s]" % (locator, row+1, cell)
        text = self.driver.find_element_by_xpath(locator).text
        return text

    def text_get_table_row_cell(self, locator, text):
        """通过xpath定位的方式，根据参数中的文本返回文本所在的行列，排除了表头的情况"""

        table_text_list = []

        # 获取行数，除去表头
        table_tr = self.driver.find_elements(By.XPATH, locator + "/tbody/tr")[1:]
        row = len(table_tr)

        # 获取列数
        table_td = self.driver.find_elements(By.XPATH, locator + "/tbody/tr/td")
        cell = int(len(table_td)/row)

        # 遍历table中的所有文本，并根据行列数，存为一个二位列表
        for i in range(2, row + 2):
            row_text_list = []
            for j in range(1, cell + 1):
                tl = locator + "/tbody/tr[" + str(i) + "]/td[" + str(j) + "]"
                table_text = self.driver.find_element(By.XPATH, tl).text
                row_text_list.append(table_text)
            table_text_list.append(row_text_list)

        # 遍历二位列表，逐一进行字符串匹配
        for r in table_text_list:
            for c in r:
                if text in c:
                    return table_text_list.index(r) + 1, r.index(c) + 1

    def text_get_table_row_cell_by_css(self, csslocator, text):
        """通过css定位的方式，根据参数中的文本返回文本所在的行列，排除了表头的情况"""

        locator = csslocator + ">tbody>tr"

        #去表头
        table_tr_list = self.driver.find_elements(By.CSS_SELECTOR, locator)[1:]

        # 遍历table中的所有文本，并根据行列数，存为一个二位列表
        table_text_list = []
        for tr in table_tr_list:
            table_td_list = tr.find_elements(By.TAG_NAME, "td")
            row_text_list = []
            for td in table_td_list:
                row_text_list.append(td.text)
            table_text_list.append(row_text_list)

        # 遍历二位列表，逐一进行字符串匹配
        for r in table_text_list:
            for c in r:
                if text in c:
                    return table_text_list.index(r) + 1, r.index(c) + 1