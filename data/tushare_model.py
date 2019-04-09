import tushare as ts
from config.settings import (
    TUSHARE_TOKEN,
    DB_LINK,
    DB_CONFIG
)
from sqlalchemy import create_engine
from app.database import Database


class Model(object):
    """
    基础模型
    """
    def __init__(self, *args, **kwargs):
        # 设置token
        ts.set_token(TUSHARE_TOKEN)

        # 创建mysql数据库引擎
        self.engine = create_engine(DB_LINK)

        # 创建数据库对象
        self.db = Database(**DB_CONFIG)


