# 导包
import json

import app
import logging
from logging import handlers

# 编写初始化日志的代码
# 1.首先定义一个初始化日志的函数
def init_logging():
    # 2.在函数中设置日志器
    logger = logging.getLogger()
    # 3.设置日志等级
    logger.setLevel(logging.INFO)
    # 4.设置控制台处理器
    sh = logging.StreamHandler()
    # 5.设置文件处理器(文件处理的作用是设置保存日志的地址的)
    log_path = app.BASE_DIR + "/log/tpshop.log"
    fh = logging.handlers.TimedRotatingFileHandler(log_path,when='M',interval=1,backupCount=3,encoding='utf-8')
    # 6.设置格式化器
    fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)]  %(message)s'
    formatter = logging.Formatter(fmt)
    # 7.将格式化器添加到文件处理器和控制台处理器当中
    sh.setFormatter(formatter)
    fh.setFormatter(formatter)
    # 8.将文件处理器和控制台处理器添加到日志器当中
    logger.addHandler(sh)
    logger.addHandler(fh)

# 定义断言函数
def assert_common(self,http_code,status,msg,response):
    self.assertEqual(http_code, response.status_code)
    self.assertEqual(status, response.json().get("status"))
    self.assertIn(msg, response.json().get("msg"))

# 编写读取注册数据的函数
def read_data(filepath):
    # 打开数据文件
    with open(filepath,'r',encoding='utf-8') as f:
        # 使用json加载数据文件为json格式
        result_dict = []
        jsonData = json.load(f)
        for i in jsonData.values():
            # 把每一组登录数据的values值转化为元组形式,并添加到空的列表中
            result_dict.append(list(i.values()))

    # print("查看读取的登录数据为:",result_dict)
    return result_dict
