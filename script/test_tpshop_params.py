# 导包
import pymysql
import requests
import unittest

from parameterized import parameterized

import app
from api.login_api import TestTpshopLoginApi
from api.reg_api import TestTpshopRegApi


from utils import read_data

# 创建测试函数的类,继承unittest.TestCase
class TestTpshopTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.reg_api = TestTpshopRegApi()
        cls.login_api = TestTpshopLoginApi()
        cls.session = requests.Session()
        # 初始化数据库连接
        cls.conn = pymysql.connect('localhost','root','root','tpshop2.0')
        cls.cursor = cls.conn.cursor()


    @classmethod
    def tearDownClass(cls):
        if cls.session != None:
            cls.session.close()

        if cls.cursor != None:
            cls.cursor.close()

        if cls.conn != None:
            cls.conn.close()

    def tearDown(self):
        self.login_api.logout(self.session)

    # 定义注册数据文件的路径
    filepath = app.BASE_DIR + "/data/data.json"
    @parameterized.expand(read_data(filepath))
    def test_reg_login(self,username,password,http_code,status,reg_msg,login_msg):
        # 发送注册验证码请求
        response = self.reg_api.get_reg_verify_url(self.session)
        # 断言验证码的返回数据
        # self.assertIn("image",response.headers.get("Content-Type"))
        # 发送注册接口请求
        data = {"username":username,
                "verify_code":"8888",
                "password":password,
                "password2":password}
        response_reg = self.reg_api.reg(data,self.session)
        # 打印注册结果
        print("注册的结果为:",response_reg.json())
        # 在数据库中查询注册结果
        search_sql = "select mobile from tp_users where user_id={}".format(response_reg.json().get('result').get('user_id'))
        self.cursor.execute(search_sql)
        # 获取返回结果
        result = self.cursor.fetchone()[0]
        # 断言数据库中的查询结果
        self.assertEqual(username,result)
        # 断言注册
        self.assertEqual(http_code,response_reg.status_code)
        self.assertEqual(status,response_reg.json().get("status"))
        self.assertIn(reg_msg,response_reg.json().get("msg"))


        # 发送验证码接口请求
        response = self.login_api.get_login_verify_url(self.session)
        # 断言验证码的返回数据
        # self.assertIn("image", response.headers.get("Content-Type"))
        # 发送登录接口请求
        data = {"username": username, "password": password, "verify_code": "8888"}
        response_login = self.login_api.login(data, self.session)
        # 打印登录结果
        print("登录的结果为:", response_login.json())
        # 断言登录
        self.assertEqual(http_code, response_login.status_code)
        self.assertEqual(status, response_login.json().get("status"))
        self.assertIn(login_msg, response_login.json().get("msg"))
