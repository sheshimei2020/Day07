# 定义封装的类
class TestTpshopRegApi:

    def __init__(self):
        # 注册的验证码url
        self.reg_verify_url = "http://localhost/index.php/Home/User/verify/type/user_reg.html"
        # 注册接口的url
        self.reg_url = "http://localhost/index.php/Home/User/reg.html"


    # 封装获取注册验证码
    def get_reg_verify_url(self, session):
        # 发送验证码请求并返回对象
        return session.get(url=self.reg_verify_url)

    # 封装注册接口
    def reg(self, data, session):
        response = session.post(url=self.reg_url, data=data,headers={"Content-Type":"application/x-www-form-urlencoded"})
        return response

