#coding=utf-8

import unittest
import HTMLTestRunner
import time

#测试用例目录
test_case_list = "E:\\miaodai\\test_case"

discover = unittest.defaultTestLoader.discover(test_case_list,pattern="test*.py")

#获取当前时间
now = time.strftime("%Y_%m_%d_%H_%M_%S")

#自定义存放路径
filename = "E:\\miaodai\\test_report\\" + now + "_result.html"

fn = open(filename,"wb")

#执行测试套件
runner = HTMLTestRunner.HTMLTestRunner(
	stream=fn,
	title=u"秒贷接口测试报告",
	description="测试用例执行情况")

runner.run(discover)

