# 定义封装的类
class TestTpshopLoginApi:
    def __init__(self):
        # 登录的验证码url
        self.login_verify_url = "http://localhost/index.php?m=Home&c=User&a=verify"
        # 登录接口的url
        self.login_url = "http://localhost/index.php?m=Home&c=User&a=do_login"

    # 封装获取登录验证码
    def get_login_verify_url(self, session):
        return session.get(url=self.login_verify_url)

    # 封装登录接口
    def login(self, data, session):
        response = session.post(url=self.login_url, data=data,headers={"Content-Type":"application/x-www-form-urlencoded"})
        return response

    # 封装退出登录接口
    def logout(self,session):
        return session.get("http://localhost/index.php/Home/user/logout.html")