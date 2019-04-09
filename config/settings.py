import os

# 项目根目录设置
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# tushare 的token设置
TUSHARE_TOKEN = "0df296dfec52d60ad8d6e0c4110870d2c5972d8bc52363cf0a7f2d7a"

# 数据库配置
DB_LINK = 'mysql+pymysql://root:root@127.0.0.1/lianghua?charset=utf8'
DB_CONFIG = {
    'password': 'root',
    'db': 'lianghua',
    "host": '127.0.0.1',
    "user": 'root',
    "charset": 'utf8',
    "port": 3306
}

"""
火币配置
"""
Access_Key = "07a86163-f6253ec7-7b6b173d-dc620"
Secret_Key = "356960ef-7ca2e3e7-469ed22c-4b40d"

