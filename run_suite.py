# 导包
import time
import os
import unittest

import HTMLTestRunner_PY3

import app
from script.test_tpshop_params import TestTpshopTest

# os.path.dirname(os.path.abspath(__file__))可以定位到当前项目的目录
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# 创建测试套件
suite = unittest.TestSuite()
# 将测试用例添加到测试套件
suite.addTest(unittest.makeSuite(TestTpshopTest))
# 定义测试报告的目录和报告的名称
report_path = app.BASE_DIR + "/report/tpshop{}.html".format(time.strftime('%Y%m%d%H%M%S'))
# 使用HTMLTestRunner_PY3生成测试报告
with open(report_path,'wb') as f:
    runner = HTMLTestRunner_PY3.HTMLTestRunner(f, verbosity=1, title='tpshop注册接口登录接口功能测试',
                                               description='注册登录接口测试报告')
    runner.run(suite)