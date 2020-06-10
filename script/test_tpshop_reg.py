# 导包
import requests
import unittest

import app
from api.reg_api import TestTpshopRegApi

# 创建测试函数的类,继承unittest.TestCase
class TestTpshopReg(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.reg_api = TestTpshopRegApi()
        cls.session = requests.Session()


    @classmethod
    def tearDownClass(cls):
        if cls.session != None:
            cls.session.close()


    def test_01_reg(self):
        # 发送注册验证码请求
        response = self.reg_api.get_reg_verify_url(self.session)
        # 断言验证码的返回数据
        self.assertIn("image",response.headers.get("Content-Type"))
        # 发送注册接口请求
        data = {"username":"13100001112",
                "verify_code":"8888",
                "password":"51947522 8fe35ad067744465c42a19b2",
                "password2":"51947522 8fe35ad067744465c42a19b2"}
        response = self.reg_api.reg(data,self.session)
        # 打印注册结果
        print("注册的结果为:",response.json())
        # 断言注册
        self.assertEqual(200,response.status_code)
        self.assertEqual(1,response.json().get("status"))
        self.assertIn("注册成功",response.json().get("msg"))

