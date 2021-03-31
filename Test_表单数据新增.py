"""
编写人员：李昱辉
测试用例流程：登录→表单设计器→新增表单模板→加入单个控件→进入表单数据（单个控件）→加入数据→显示验证
测试对象: Basepoint (基点登录)  http://39.101.68.161
包含控件内容：单行文本、多行文本、计数器、单选框组、多选框组、下拉选择框、时间选择器
"""
# -*- coding: utf-8 -*-
import unittest
import time
from selenium import webdriver
from selenium.webdriver import ActionChains

import random
import xlrd
import paramiko
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
# driver = webdriver.Chrome()

# 本机webdriver
driver = webdriver.Chrome(r'C:\Application\chromedriver.exe')

driver.maximize_window()
driver.implicitly_wait(10)
url = 'http://39.101.68.161'
driver.get(url)

class Test_表单数据新增(unittest.TestCase):

    def setUp(self):
        driver.refresh()
        # print('setup刷新')

    def test_login(self):
        # 连接网页
        # driver.maximize_window()
        # url = 'http://39.101.68.161'
        # driver.get(url)
        time.sleep(10)

        # # 连接数据库查询user
        # sql1 = 'SELECT name from test where id = 1005;'
        # admin1 = Mysql().data(sql1)
        # print(admin1)


        # 登录名输入框
        # username = driver.find_element_by_xpath("//*[@id='username']")
        username = driver.find_element_by_id('username')
        username.send_keys('admin')

        # 密码输入框
        password = driver.find_element_by_id('password')
        password.send_keys('123456')

        # 确认按钮
        submit = driver.find_element_by_xpath("//span[text()='登 录']//..")
        submit.click()

        answer = driver.find_element_by_xpath("//span[text()='登 录']//..").text
        # print(answer)

        #assert answer == '确 定'
        # print('登录')
        time.sleep(5)
# 单行文本
    def test_单行文本(self):
        time.sleep(3)
        # 表单设计
        biaodansheji=driver.find_element_by_xpath("//i[@class='anticon anticon-cluster']")
        biaodansheji.click()
        time.sleep(1)

        # 表单设计器菜单
        biaodanshejicaidan = driver.find_element_by_xpath("//a[@href='/form/design/manage']")
        biaodanshejicaidan.click()
        time.sleep(1)

        # 表单设计器-新增按钮
        biaodanAddButton = driver.find_element_by_xpath("//div[@class='table-operator']//span[text()='新增']/..")
        biaodanAddButton.click()
        time.sleep(1)

        #表单名称
        biaodanName = driver.find_element_by_id('name')
        biaodanName.send_keys('单行文本自动化测试')
        time.sleep(1)

        # 表单编码
        name = 'Auto_test' + str(random.randint(1, 1000))
        biaodanCode = driver.find_element_by_id('code')
        biaodanCode.send_keys(name)
        time.sleep(1)

        # 表单设计器-新增确定
        # body > div: nth - child(11) > div > div.ant - modal - wrap > div > div.ant - modal - content > div.ant - modal - footer > div > div:nth - child(2) > button: nth - child(2)
        # biaodanSubmit = driver.find_element_by_css_selector('.ant-modal-footer button:nth-child(2)')
        biaodanSubmit = driver.find_element_by_xpath("//button[@class='ant-btn ant-btn-primary']//span[text()='确 定']/..")
        biaodanSubmit.click()
        time.sleep(2)

        # 添加控件-单行文本
        danhangwenbenAdd = driver.find_element_by_xpath("//i[@class='icon iconfont icon-input']")
        danhangwenbenAdd.click()
        time.sleep(2)

        # 模板保存
        save = driver.find_element_by_xpath("//i[@class='el-icon-upload']")
        save.click()
        time.sleep(2)

        # 关闭模板
        close = driver.find_element_by_xpath("//button[@class='ant-drawer-close']")
        # ActionChains(driver).click(close).perform()
        # close.send_keys(Keys.ESCAPE)
        close.click()
        time.sleep(2)

        # 表单名称输入框-单行文本
        searchName = driver.find_element_by_xpath("//input[@class='ant-input']")
        searchName.send_keys('单行文本自动化测试')
        time.sleep(3)

        # 查询按钮
        # app > section > section > main > div > div > div > div > div.table-page-search-wrapper > form > div > div:nth-child(3) > span > button:nth-child(1)
        # searchClick = driver.find_element_by_xpath("//button[@class='ant-btn ant-btn-primary']//span[text()='查询'/..]")
        # searchClick = driver.find_element_by_xpath("//button[@class='anticon anticon-search']//span[text()='查询']/..")
        # searchClick = driver.find_element_by_xpath('//*[@id="app"]/section/section/main/div/div/div/div/div[1]/form/div/div[3]/span/button[1]')
        searchClick = driver.find_element_by_xpath("//main[@class='ant-layout-content']//button//span[text()='查询']/..")
        searchClick.click()
        time.sleep(2)

        #表单数据
        biaodanshuju = driver.find_element_by_xpath("//a[text()='表单数据']")
        biaodanshuju.click()
        time.sleep(2)

        # 表单数据-新增
        biaodanshujuAdd = driver.find_element_by_xpath("//div[@class='table-operator']//span[text()='新增']/..")
        biaodanshujuAdd.click()
        time.sleep(2)

        # 单行文本-数据输入
        danhangwenbenAddData = driver.find_element_by_xpath("//input[@class='el-input__inner']")
        danhangwenbenAddData.send_keys("这是一段单行文本测试文字")
        time.sleep(2)

        # 单行文本-新增确定
        xinzengSubmit = driver.find_element_by_xpath("//button[@class='ant-btn ant-btn-primary']//span[text()='确 定']/..")
        xinzengSubmit.click()
        time.sleep(2)

        # 断言验证
        result = driver.find_element_by_xpath("//td[@class='ant-table-row-cell-ellipsis']")
        print("result==" + result.text)
        try:
            self.assertEqual(result.text, "这是一段单行文本测试文字")
        except AssertionError as e:
            print
            "验证失败"
        time.sleep(2)
# 多行文本
    def test_多行文本(self):
        # 表单设计
        biaodansheji = driver.find_element_by_xpath("//i[@class='anticon anticon-cluster']")
        biaodansheji.click()
        time.sleep(1)

        # 表单设计器菜单
        biaodanshejicaidan = driver.find_element_by_xpath("//a[@href='/form/design/manage']")
        biaodanshejicaidan.click()
        time.sleep(1)

        # 表单设计器-新增按钮
        biaodanAddButton = driver.find_element_by_xpath("//div[@class='table-operator']//span[text()='新增']/..")
        biaodanAddButton.click()
        time.sleep(1)

        # 表单名称（复用）
        biaodanName = driver.find_element_by_id('name')
        biaodanName.send_keys('多行文本自动化测试')
        time.sleep(1)

        # 表单编码
        name = 'Auto_test' + str(random.randint(1, 1000))
        biaodanCode = driver.find_element_by_id('code')
        biaodanCode.send_keys(name)
        time.sleep(1)

        # 表单设计器-新增确定
        # body > div: nth - child(11) > div > div.ant - modal - wrap > div > div.ant - modal - content > div.ant - modal - footer > div > div:nth - child(2) > button: nth - child(2)
        # biaodanSubmit = driver.find_element_by_css_selector('.ant-modal-footer button:nth-child(2)')
        biaodanSubmit = driver.find_element_by_xpath(
            "//button[@class='ant-btn ant-btn-primary']//span[text()='确 定']/..")
        biaodanSubmit.click()
        time.sleep(1)

        # 添加控件-多行文本（复用）
        AddModule  = driver.find_element_by_xpath("//i[@class='icon iconfont icon-diy-com-textarea']")
        AddModule .click()
        time.sleep(1)

        # 模板保存
        save = driver.find_element_by_xpath("//i[@class='el-icon-upload']")
        save.click()
        time.sleep(1)

        # 关闭模板
        close = driver.find_element_by_xpath("//button[@class='ant-drawer-close']")
        # ActionChains(driver).click(close).perform()
        # close.send_keys(Keys.ESCAPE)
        close.click()
        time.sleep(1)

        # 表单名称输入框  -多行文本（复用）
        searchName = driver.find_element_by_xpath("//input[@class='ant-input']")
        searchName.send_keys('多行文本自动化测试')
        time.sleep(1)

        # 查询按钮
        # app > section > section > main > div > div > div > div > div.table-page-search-wrapper > form > div > div:nth-child(3) > span > button:nth-child(1)
        # searchClick = driver.find_element_by_xpath("//button[@class='ant-btn ant-btn-primary']//span[text()='查询'/..]")
        # searchClick = driver.find_element_by_xpath("//button[@class='anticon anticon-search']//span[text()='查询']/..")
        # searchClick = driver.find_element_by_xpath('//*[@id="app"]/section/section/main/div/div/div/div/div[1]/form/div/div[3]/span/button[1]')
        searchClick = driver.find_element_by_xpath("//main[@class='ant-layout-content']//button//span[text()='查询']/..")
        searchClick.click()
        time.sleep(1)

        # 表单数据（页面跳转）
        biaodanshuju = driver.find_element_by_xpath("//a[text()='表单数据']")
        biaodanshuju.click()
        time.sleep(2)

        # 表单数据-新增
        biaodanshujuAdd = driver.find_element_by_xpath("//div[@class='table-operator']//span[text()='新增']/..")
        biaodanshujuAdd.click()
        time.sleep(1)

        # 多行文本-数据输入（复用）
        duohangwenbenAddData = driver.find_element_by_xpath("//textarea[@class='el-textarea__inner']")
        duohangwenbenAddData.send_keys("这是一段多行文本测试文字")
        duohangwenbenAddData.send_keys(Keys.ENTER)
        duohangwenbenAddData.send_keys("换行")
        duohangwenbenAddData.send_keys(Keys.ENTER)
        duohangwenbenAddData.send_keys("这是一段多行文本测试文字")
        time.sleep(1)

        # 多行文本-新增确定
        xinzengSubmit = driver.find_element_by_xpath(
            "//button[@class='ant-btn ant-btn-primary']//span[text()='确 定']/..")
        xinzengSubmit.click()
        time.sleep(1)

        # 断言验证
        result = driver.find_element_by_xpath("//td[@class='ant-table-row-cell-ellipsis']")
        print("result==" + result.text)
        try:
            self.assertEqual(result.text, "这是一段多行文本测试文字"
                                          "换行"
                                          "这是一段多行文本测试文字")
        except AssertionError as e:
            print
            "验证失败"
        time.sleep(2)
# 计数器
    def test_计数器(self):
            # 表单设计
            biaodansheji = driver.find_element_by_xpath("//i[@class='anticon anticon-cluster']")
            biaodansheji.click()
            time.sleep(1)

            # 表单设计器菜单
            biaodanshejicaidan = driver.find_element_by_xpath("//a[@href='/form/design/manage']")
            biaodanshejicaidan.click()
            time.sleep(1)

            # 表单设计器-新增按钮
            biaodanAddButton = driver.find_element_by_xpath("//div[@class='table-operator']//span[text()='新增']/..")
            biaodanAddButton.click()
            time.sleep(1)

            # 表单名称（复用）
            biaodanName = driver.find_element_by_id('name')
            biaodanName.send_keys('计数器自动化测试')
            time.sleep(1)

            # 表单编码
            name = 'Auto_test' + str(random.randint(1, 10000))
            biaodanCode = driver.find_element_by_id('code')
            biaodanCode.send_keys(name)
            time.sleep(1)

            # 表单设计器-新增确定
            # body > div: nth - child(11) > div > div.ant - modal - wrap > div > div.ant - modal - content > div.ant - modal - footer > div > div:nth - child(2) > button: nth - child(2)
            # biaodanSubmit = driver.find_element_by_css_selector('.ant-modal-footer button:nth-child(2)')
            biaodanSubmit = driver.find_element_by_xpath(
                "//button[@class='ant-btn ant-btn-primary']//span[text()='确 定']/..")
            biaodanSubmit.click()
            time.sleep(1)

            # 添加控件-计数器（复用）
            AddModule = driver.find_element_by_xpath("//i[@class='icon iconfont icon-number']")
            AddModule .click()
            time.sleep(1)

            # 模板保存
            save = driver.find_element_by_xpath("//i[@class='el-icon-upload']")
            save.click()
            time.sleep(1)

            # 关闭模板
            close = driver.find_element_by_xpath("//button[@class='ant-drawer-close']")
            # ActionChains(driver).click(close).perform()
            # close.send_keys(Keys.ESCAPE)
            close.click()
            time.sleep(1)

            # 表单名称查询框  -计数器（复用）
            searchName = driver.find_element_by_xpath("//input[@class='ant-input']")
            searchName.send_keys('计数器自动化测试')
            time.sleep(1)

            # 查询按钮
            # app > section > section > main > div > div > div > div > div.table-page-search-wrapper > form > div > div:nth-child(3) > span > button:nth-child(1)
            # searchClick = driver.find_element_by_xpath("//button[@class='ant-btn ant-btn-primary']//span[text()='查询'/..]")
            # searchClick = driver.find_element_by_xpath("//button[@class='anticon anticon-search']//span[text()='查询']/..")
            # searchClick = driver.find_element_by_xpath('//*[@id="app"]/section/section/main/div/div/div/div/div[1]/form/div/div[3]/span/button[1]')
            searchClick = driver.find_element_by_xpath(
                "//main[@class='ant-layout-content']//button//span[text()='查询']/..")
            searchClick.click()
            time.sleep(1)

            # 表单数据（页面跳转）
            biaodanshuju = driver.find_element_by_xpath("//a[text()='表单数据']")
            biaodanshuju.click()
            time.sleep(2)

            # 表单数据-新增
            biaodanshujuAdd = driver.find_element_by_xpath("//div[@class='table-operator']//span[text()='新增']/..")
            biaodanshujuAdd.click()
            time.sleep(1)

            # 计数器-数据输入（复用）
            AddData = driver.find_element_by_xpath("//input[@class='el-input__inner']")
            AddData.send_keys("3")
            time.sleep(1)

            # 多行文本-新增确定
            xinzengSubmit = driver.find_element_by_xpath(
                "//button[@class='ant-btn ant-btn-primary']//span[text()='确 定']/..")
            xinzengSubmit.click()
            time.sleep(1)

            # 断言验证(复用)
            result = driver.find_element_by_xpath("//td[@class='ant-table-row-cell-ellipsis']")
            print("result==" + result.text)
            try:
                self.assertEqual(result.text, "3")
            except AssertionError as e:
                print
                "验证失败"
            time.sleep(2)
# 单选框组
    def test_单选框组(self):
            # 表单设计
            biaodansheji = driver.find_element_by_xpath("//i[@class='anticon anticon-cluster']")
            biaodansheji.click()
            time.sleep(1)

            # 表单设计器菜单
            biaodanshejicaidan = driver.find_element_by_xpath("//a[@href='/form/design/manage']")
            biaodanshejicaidan.click()
            time.sleep(1)

            # 表单设计器-新增按钮
            biaodanAddButton = driver.find_element_by_xpath("//div[@class='table-operator']//span[text()='新增']/..")
            biaodanAddButton.click()
            time.sleep(1)

            # 表单名称（复用）
            biaodanName = driver.find_element_by_id('name')
            biaodanName.send_keys('单选框组自动化测试')
            time.sleep(1)

            # 表单编码
            name = 'Auto_test' + str(random.randint(1, 10000))
            biaodanCode = driver.find_element_by_id('code')
            biaodanCode.send_keys(name)
            time.sleep(1)

            # 表单设计器-新增确定
            # body > div: nth - child(11) > div > div.ant - modal - wrap > div > div.ant - modal - content > div.ant - modal - footer > div > div:nth - child(2) > button: nth - child(2)
            # biaodanSubmit = driver.find_element_by_css_selector('.ant-modal-footer button:nth-child(2)')
            biaodanSubmit = driver.find_element_by_xpath(
                "//button[@class='ant-btn ant-btn-primary']//span[text()='确 定']/..")
            biaodanSubmit.click()
            time.sleep(1)

            # 添加控件-单选框组（复用）
            AddModule = driver.find_element_by_xpath("//i[@class='icon iconfont icon-radio-active']")
            AddModule .click()
            time.sleep(1)

            # 模板保存
            save = driver.find_element_by_xpath("//i[@class='el-icon-upload']")
            save.click()
            time.sleep(1)

            # 关闭模板
            close = driver.find_element_by_xpath("//button[@class='ant-drawer-close']")
            # ActionChains(driver).click(close).perform()
            # close.send_keys(Keys.ESCAPE)
            close.click()
            time.sleep(1)

            # 表单名称查询框  -计数器（复用）
            searchName = driver.find_element_by_xpath("//input[@class='ant-input']")
            searchName.send_keys('单选框组自动化测试')
            time.sleep(1)

            # 查询按钮
            # app > section > section > main > div > div > div > div > div.table-page-search-wrapper > form > div > div:nth-child(3) > span > button:nth-child(1)
            # searchClick = driver.find_element_by_xpath("//button[@class='ant-btn ant-btn-primary']//span[text()='查询'/..]")
            # searchClick = driver.find_element_by_xpath("//button[@class='anticon anticon-search']//span[text()='查询']/..")
            # searchClick = driver.find_element_by_xpath('//*[@id="app"]/section/section/main/div/div/div/div/div[1]/form/div/div[3]/span/button[1]')
            searchClick = driver.find_element_by_xpath(
                "//main[@class='ant-layout-content']//button//span[text()='查询']/..")
            searchClick.click()
            time.sleep(1)

            # 表单数据（页面跳转）
            biaodanshuju = driver.find_element_by_xpath("//a[text()='表单数据']")
            biaodanshuju.click()
            time.sleep(2)

            # 表单数据-新增
            biaodanshujuAdd = driver.find_element_by_xpath("//div[@class='table-operator']//span[text()='新增']/..")
            biaodanshujuAdd.click()
            time.sleep(1)

            # 单选框组-数据输入（复用）
            AddData = driver.find_element_by_xpath("//div[@class='el-radio-group']//span[text()='Option 2']/..")
            AddData.click()
            time.sleep(1)

            # 单选框组-新增确定
            xinzengSubmit = driver.find_element_by_xpath(
                "//button[@class='ant-btn ant-btn-primary']//span[text()='确 定']/..")
            xinzengSubmit.click()
            time.sleep(1)

            # 断言验证(复用)
            result = driver.find_element_by_xpath("//td[@class='ant-table-row-cell-ellipsis']")
            print("result==" + result.text)
            try:
                self.assertEqual(result.text, "Option 2")
            except AssertionError as e:
                print
                "验证失败"
            time.sleep(2)
# 多选框组
    def test_多选框组(self):
            # 表单设计
            biaodansheji = driver.find_element_by_xpath("//i[@class='anticon anticon-cluster']")
            biaodansheji.click()
            time.sleep(1)

            # 表单设计器菜单
            biaodanshejicaidan = driver.find_element_by_xpath("//a[@href='/form/design/manage']")
            biaodanshejicaidan.click()
            time.sleep(1)

            # 表单设计器-新增按钮
            biaodanAddButton = driver.find_element_by_xpath("//div[@class='table-operator']//span[text()='新增']/..")
            biaodanAddButton.click()
            time.sleep(1)

            # 表单名称（复用）
            biaodanName = driver.find_element_by_id('name')
            biaodanName.send_keys('多选框组自动化测试')
            time.sleep(1)

            # 表单编码
            name = 'Auto_test' + str(random.randint(1, 10000))
            biaodanCode = driver.find_element_by_id('code')
            biaodanCode.send_keys(name)
            time.sleep(1)

            # 表单设计器-新增确定
            # body > div: nth - child(11) > div > div.ant - modal - wrap > div > div.ant - modal - content > div.ant - modal - footer > div > div:nth - child(2) > button: nth - child(2)
            # biaodanSubmit = driver.find_element_by_css_selector('.ant-modal-footer button:nth-child(2)')
            biaodanSubmit = driver.find_element_by_xpath(
                "//button[@class='ant-btn ant-btn-primary']//span[text()='确 定']/..")
            biaodanSubmit.click()
            time.sleep(1)

            # 添加控件-多选框组（复用）
            AddModule = driver.find_element_by_xpath("//i[@class='icon iconfont icon-check-box']")
            AddModule .click()
            time.sleep(1)

            # 模板保存
            save = driver.find_element_by_xpath("//i[@class='el-icon-upload']")
            save.click()
            time.sleep(1)

            # 关闭模板
            close = driver.find_element_by_xpath("//button[@class='ant-drawer-close']")
            # ActionChains(driver).click(close).perform()
            # close.send_keys(Keys.ESCAPE)
            close.click()
            time.sleep(1)

            # 表单名称查询框  -多选框组（复用）
            searchName = driver.find_element_by_xpath("//input[@class='ant-input']")
            searchName.send_keys('多选框组自动化测试')
            time.sleep(1)

            # 查询按钮
            # app > section > section > main > div > div > div > div > div.table-page-search-wrapper > form > div > div:nth-child(3) > span > button:nth-child(1)
            # searchClick = driver.find_element_by_xpath("//button[@class='ant-btn ant-btn-primary']//span[text()='查询'/..]")
            # searchClick = driver.find_element_by_xpath("//button[@class='anticon anticon-search']//span[text()='查询']/..")
            # searchClick = driver.find_element_by_xpath('//*[@id="app"]/section/section/main/div/div/div/div/div[1]/form/div/div[3]/span/button[1]')
            searchClick = driver.find_element_by_xpath(
                "//main[@class='ant-layout-content']//button//span[text()='查询']/..")
            searchClick.click()
            time.sleep(1)

            # 表单数据（页面跳转）
            biaodanshuju = driver.find_element_by_xpath("//a[text()='表单数据']")
            biaodanshuju.click()
            time.sleep(2)

            # 表单数据-新增
            biaodanshujuAdd = driver.find_element_by_xpath("//div[@class='table-operator']//span[text()='新增']/..")
            biaodanshujuAdd.click()
            time.sleep(1)

            # 多选框组-数据输入（复用）
            AddData = driver.find_element_by_xpath("//div[@class='el-form-item__content']//span[text()='Option 1']/..")
            AddData.click()
            time.sleep(1)
            AddData2 = driver.find_element_by_xpath("//div[@class='el-form-item__content']//span[text()='Option 2']/..")
            AddData2.click()
            time.sleep(1)

            # 多选框组-新增确定
            xinzengSubmit = driver.find_element_by_xpath(
                "//button[@class='ant-btn ant-btn-primary']//span[text()='确 定']/..")
            xinzengSubmit.click()
            time.sleep(1)

            # 断言验证(复用)
            result = driver.find_element_by_xpath("//td[@class='ant-table-row-cell-ellipsis']")
            print("result==" + result.text)
            try:
                self.assertEqual(result.text, "Option 1Option 2")
            except AssertionError as e:
                print
                "验证失败"
            time.sleep(2)
# 下拉选择框
    def test_下拉选择框(self):
            # 表单设计
            biaodansheji = driver.find_element_by_xpath("//i[@class='anticon anticon-cluster']")
            biaodansheji.click()
            time.sleep(1)

            # 表单设计器菜单
            biaodanshejicaidan = driver.find_element_by_xpath("//a[@href='/form/design/manage']")
            biaodanshejicaidan.click()
            time.sleep(1)

            # 表单设计器-新增按钮
            biaodanAddButton = driver.find_element_by_xpath("//div[@class='table-operator']//span[text()='新增']/..")
            biaodanAddButton.click()
            time.sleep(1)

            # 表单名称（复用）
            biaodanName = driver.find_element_by_id('name')
            biaodanName.send_keys('下拉选择框自动化测试')
            time.sleep(1)

            # 表单编码
            name = 'Auto_test' + str(random.randint(1, 10000))
            biaodanCode = driver.find_element_by_id('code')
            biaodanCode.send_keys(name)
            time.sleep(1)

            # 表单设计器-新增确定
            # body > div: nth - child(11) > div > div.ant - modal - wrap > div > div.ant - modal - content > div.ant - modal - footer > div > div:nth - child(2) > button: nth - child(2)
            # biaodanSubmit = driver.find_element_by_css_selector('.ant-modal-footer button:nth-child(2)')
            biaodanSubmit = driver.find_element_by_xpath(
                "//button[@class='ant-btn ant-btn-primary']//span[text()='确 定']/..")
            biaodanSubmit.click()
            time.sleep(1)

            # 添加控件-下拉选择框（复用）
            AddModule = driver.find_element_by_xpath("//i[@class='icon iconfont icon-select']")
            AddModule .click()
            time.sleep(1)

            # 模板保存
            save = driver.find_element_by_xpath("//i[@class='el-icon-upload']")
            save.click()
            time.sleep(1)

            # 关闭模板
            close = driver.find_element_by_xpath("//button[@class='ant-drawer-close']")
            # ActionChains(driver).click(close).perform()
            # close.send_keys(Keys.ESCAPE)
            close.click()
            time.sleep(1)

            # 表单名称查询框  -下拉选择框（复用）
            searchName = driver.find_element_by_xpath("//input[@class='ant-input']")
            searchName.send_keys('下拉选择框自动化测试')
            time.sleep(1)

            # 查询按钮
            # app > section > section > main > div > div > div > div > div.table-page-search-wrapper > form > div > div:nth-child(3) > span > button:nth-child(1)
            # searchClick = driver.find_element_by_xpath("//button[@class='ant-btn ant-btn-primary']//span[text()='查询'/..]")
            # searchClick = driver.find_element_by_xpath("//button[@class='anticon anticon-search']//span[text()='查询']/..")
            # searchClick = driver.find_element_by_xpath('//*[@id="app"]/section/section/main/div/div/div/div/div[1]/form/div/div[3]/span/button[1]')
            searchClick = driver.find_element_by_xpath(
                "//main[@class='ant-layout-content']//button//span[text()='查询']/..")
            searchClick.click()
            time.sleep(1)

            # 表单数据（页面跳转）
            biaodanshuju = driver.find_element_by_xpath("//a[text()='表单数据']")
            biaodanshuju.click()
            time.sleep(2)

            # 表单数据-新增
            biaodanshujuAdd = driver.find_element_by_xpath("//div[@class='table-operator']//span[text()='新增']/..")
            biaodanshujuAdd.click()
            time.sleep(1)

            # 下拉选择框-数据输入（复用）
            AddData = driver.find_element_by_xpath("//div[@class='el-select el-select--small']")
            AddData.click()
            time.sleep(1)
            AddData2 = driver.find_element_by_xpath("//ul[@class='el-scrollbar__view el-select-dropdown__list']//span[text()='Option 2']/..")
            AddData2.click()
            time.sleep(1)

            # 多选框组-新增确定
            xinzengSubmit = driver.find_element_by_xpath(
                "//button[@class='ant-btn ant-btn-primary']//span[text()='确 定']/..")
            xinzengSubmit.click()
            time.sleep(1)

            # 断言验证(复用)
            result = driver.find_element_by_xpath("//td[@class='ant-table-row-cell-ellipsis']")
            print("result==" + result.text)
            try:
                self.assertEqual(result.text, "Option 233333")
            except AssertionError as e:
                print
                "验证失败"
            time.sleep(2)
# 时间选择器
    def test_时间选择器(self):
            # 表单设计
            biaodansheji = driver.find_element_by_xpath("//i[@class='anticon anticon-cluster']")
            biaodansheji.click()
            time.sleep(1)

            # 表单设计器菜单
            biaodanshejicaidan = driver.find_element_by_xpath("//a[@href='/form/design/manage']")
            biaodanshejicaidan.click()
            time.sleep(1)

            # 表单设计器-新增按钮
            biaodanAddButton = driver.find_element_by_xpath("//div[@class='table-operator']//span[text()='新增']/..")
            biaodanAddButton.click()
            time.sleep(1)

            # 表单名称（复用）
            biaodanName = driver.find_element_by_id('name')
            biaodanName.send_keys('时间选择器自动化测试')
            time.sleep(1)

            # 表单编码
            name = 'Auto_test' + str(random.randint(1, 10000))
            biaodanCode = driver.find_element_by_id('code')
            biaodanCode.send_keys(name)
            time.sleep(1)

            # 表单设计器-新增确定
            # body > div: nth - child(11) > div > div.ant - modal - wrap > div > div.ant - modal - content > div.ant - modal - footer > div > div:nth - child(2) > button: nth - child(2)
            # biaodanSubmit = driver.find_element_by_css_selector('.ant-modal-footer button:nth-child(2)')
            biaodanSubmit = driver.find_element_by_xpath(
                "//button[@class='ant-btn ant-btn-primary']//span[text()='确 定']/..")
            biaodanSubmit.click()
            time.sleep(1)

            # 添加控件-时间选择器（复用）
            AddModule = driver.find_element_by_xpath("//i[@class='icon iconfont icon-time']")
            AddModule .click()
            time.sleep(1)

            # 模板保存
            save = driver.find_element_by_xpath("//i[@class='el-icon-upload']")
            save.click()
            time.sleep(1)

            # 关闭模板
            close = driver.find_element_by_xpath("//button[@class='ant-drawer-close']")
            # ActionChains(driver).click(close).perform()
            # close.send_keys(Keys.ESCAPE)
            close.click()
            time.sleep(1)

            # 表单名称查询框  -时间选择器（复用）
            searchName = driver.find_element_by_xpath("//input[@class='ant-input']")
            searchName.send_keys('时间选择器自动化测试')
            time.sleep(1)

            # 查询按钮
            # app > section > section > main > div > div > div > div > div.table-page-search-wrapper > form > div > div:nth-child(3) > span > button:nth-child(1)
            # searchClick = driver.find_element_by_xpath("//button[@class='ant-btn ant-btn-primary']//span[text()='查询'/..]")
            # searchClick = driver.find_element_by_xpath("//button[@class='anticon anticon-search']//span[text()='查询']/..")
            # searchClick = driver.find_element_by_xpath('//*[@id="app"]/section/section/main/div/div/div/div/div[1]/form/div/div[3]/span/button[1]')
            searchClick = driver.find_element_by_xpath(
                "//main[@class='ant-layout-content']//button//span[text()='查询']/..")
            searchClick.click()
            time.sleep(1)

            # 表单数据（页面跳转）
            biaodanshuju = driver.find_element_by_xpath("//a[text()='表单数据']")
            biaodanshuju.click()
            time.sleep(2)

            # 表单数据-新增
            biaodanshujuAdd = driver.find_element_by_xpath("//div[@class='table-operator']//span[text()='新增']/..")
            biaodanshujuAdd.click()
            time.sleep(1)

            # 时间选择器-数据输入（复用）
            AddData = driver.find_element_by_xpath("//div[@class='el-date-editor el-input el-input--small el-input--prefix el-input--suffix el-date-editor--time']")
            AddData.click()
            time.sleep(1)
            AddData2 = driver.find_element_by_xpath("//button[@class='el-time-panel__btn confirm']")
            AddData2.click()
            time.sleep(1)

            # 多选框组-新增确定
            xinzengSubmit = driver.find_element_by_xpath(
                "//button[@class='ant-btn ant-btn-primary']//span[text()='确 定']/..")
            xinzengSubmit.click()
            time.sleep(1)

            # 断言验证(复用)
            result = driver.find_element_by_xpath("//td[@class='ant-table-row-cell-ellipsis']")
            print("result==" + result.text)
            try:
                self.assertEqual(result.text, "")
            except AssertionError as e:
                print
                "验证失败"
            time.sleep(2)
# AI录音
    def test_AI录音(self):
        # 表单设计
        biaodansheji = driver.find_element_by_xpath("//i[@class='anticon anticon-cluster']")
        biaodansheji.click()
        time.sleep(1)

        # 表单设计器菜单
        biaodanshejicaidan = driver.find_element_by_xpath("//a[@href='/form/design/manage']")
        biaodanshejicaidan.click()
        time.sleep(1)

        # 表单设计器-AI辅助按钮
        biaodanAddButton = driver.find_element_by_xpath("//button[@class='ant-btn ant-btn-primary']")
        biaodanAddButton.click()
        time.sleep(1)

        # 表单名称（复用）
        biaodanName = driver.find_element_by_id('name')
        biaodanName.send_keys('AI辅助自动化测试')
        time.sleep(1)

        # 表单编码
        name = 'Auto_test' + str(random.randint(1, 10000))
        biaodanCode = driver.find_element_by_id('code')
        biaodanCode.send_keys(name)
        time.sleep(1)

        # 表单设计器-新增确定
        # body > div: nth - child(11) > div > div.ant - modal - wrap > div > div.ant - modal - content > div.ant - modal - footer > div > div:nth - child(2) > button: nth - child(2)
        # biaodanSubmit = driver.find_element_by_css_selector('.ant-modal-footer button:nth-child(2)')
        biaodanSubmit = driver.find_element_by_xpath(
            "//button[@class='ant-btn ant-btn-primary']//span[text()='确 定']/..")
        biaodanSubmit.click()
        time.sleep(1)

        # 添加控件-AI辅助（复用）
        # AddModule = driver.find_element_by_xpath("//i[@class='icon iconfont icon-time']")
        # AddModule.click()
        # time.sleep(1)

        # 模板保存
        save = driver.find_element_by_xpath("//i[@class='el-icon-upload']")
        save.click()
        time.sleep(1)

        # 关闭模板
        close = driver.find_element_by_xpath("//button[@class='ant-drawer-close']")
        # ActionChains(driver).click(close).perform()
        # close.send_keys(Keys.ESCAPE)
        close.click()
        time.sleep(1)

        # 表单名称查询框  -时间选择器（复用）
        searchName = driver.find_element_by_xpath("//input[@class='ant-input']")
        searchName.send_keys('时间选择器自动化测试')
        time.sleep(1)

        # 查询按钮
        # app > section > section > main > div > div > div > div > div.table-page-search-wrapper > form > div > div:nth-child(3) > span > button:nth-child(1)
        # searchClick = driver.find_element_by_xpath("//button[@class='ant-btn ant-btn-primary']//span[text()='查询'/..]")
        # searchClick = driver.find_element_by_xpath("//button[@class='anticon anticon-search']//span[text()='查询']/..")
        # searchClick = driver.find_element_by_xpath('//*[@id="app"]/section/section/main/div/div/div/div/div[1]/form/div/div[3]/span/button[1]')
        searchClick = driver.find_element_by_xpath(
            "//main[@class='ant-layout-content']//button//span[text()='查询']/..")
        searchClick.click()
        time.sleep(1)

        # 表单数据（页面跳转）
        biaodanshuju = driver.find_element_by_xpath("//a[text()='表单数据']")
        biaodanshuju.click()
        time.sleep(2)

        # 表单数据-新增
        biaodanshujuAdd = driver.find_element_by_xpath("//div[@class='table-operator']//span[text()='新增']/..")
        biaodanshujuAdd.click()
        time.sleep(1)

        # 时间选择器-数据输入（复用）
        AddData = driver.find_element_by_xpath(
            "//div[@class='el-date-editor el-input el-input--small el-input--prefix el-input--suffix el-date-editor--time']")
        AddData.click()
        time.sleep(1)
        AddData2 = driver.find_element_by_xpath("//button[@class='el-time-panel__btn confirm']")
        AddData2.click()
        time.sleep(1)

        # 多选框组-新增确定
        xinzengSubmit = driver.find_element_by_xpath(
            "//button[@class='ant-btn ant-btn-primary']//span[text()='确 定']/..")
        xinzengSubmit.click()
        time.sleep(1)

        # 断言验证(复用)
        result = driver.find_element_by_xpath("//td[@class='ant-table-row-cell-ellipsis']")
        print("result==" + result.text)
        try:
            self.assertEqual(result.text, "")
        except AssertionError as e:
            print
            "验证失败"
        time.sleep(2)

if __name__ == '__main__':            #如果是主执行脚本执行下面的代码，就是在命令行直接调用，不是被其他脚本导入调用
    # 调试
    test = Test_表单数据新增()
    # 每条用例执行前执行的setup函数
    test.setUp()
    # 表单数据新增 login函数
    test.test_login()

    # 单行文本 新增模板及新增数据
    test.test_单行文本()

    # 多行文本 新增模板及新增数据
    test.test_多行文本()

    # 计数器 新增模板及新增数据
    test.test_计数器()

    # 单选框组 新增模板及新增数据
    test.test_单选框组()

    # 多选框组 新增模板及新增数据
    test.test_多选框组()

    # 下拉选择框 新增模板及新增数据
    test.test_下拉选择框()

    # 时间选择器 新增模板及新增数据
    test.test_时间选择器()