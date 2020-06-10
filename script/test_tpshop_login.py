# 导包
import requests
import unittest

from api.login_api import TestTpshopLoginApi

# 创建测试函数的类,继承unittest.TestCase
class TestTpshopReg(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.login_api = TestTpshopLoginApi()
        cls.session = requests.Session()


    @classmethod
    def tearDownClass(cls):
        if cls.session != None:
            cls.session.close()

    def test_02_login(self):
        # 发送验证码接口请求
        response = self.login_api.get_login_verify_url(self.session)
        # 断言验证码的返回数据
        self.assertIn("image", response.headers.get("Content-Type"))
        # 发送登录接口请求
        data = {"username": "13800138006", "password": "123456", "verify_code": "8888"}
        response = self.login_api.login(data, self.session)
        # 打印登录结果
        print("登录的结果为:", response.json())
        # 断言登录
        self.assertEqual(200, response.status_code)
        self.assertEqual(1, response.json().get("status"))
        self.assertIn("登陆成功", response.json().get("msg"))