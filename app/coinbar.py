import pandas as pd
import tushare as ts
from huobi import RequestClient

from data.tushare_model import Model
from datetime import datetime, timedelta
import pymysql
from config.settings import Secret_Key, Access_Key
from utils.send_method import SendMethod


class CoinPair(Model):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 获取请求数据
        self.send = SendMethod()


    def insert(self):
        # 初始化
        pro = ts.pro_api()

        # 获取火币数据
        start_date_tmp = datetime.now() - timedelta(days=120)
        start_date = start_date_tmp.strftime("%Y%m%d")

        end_date_tmp = datetime.now() - timedelta(days=1)
        end_date = end_date_tmp.strftime("%Y%m%d%H%M%S")
        # df = pro.coinbar(exchange='huobi', symbol='btcusdt', freq='daily', start_date=start_date, end_date=end_date)
        request_client = RequestClient(api_key=Access_Key, secret_key=Secret_Key)
        # print(df)
        # candlestick_list = request_client.get_latest_candlestick("btcusdt", "Day1", 20)
        # print(candlestick_list)
        # 保存到数据库

    def get_data(self):
        """
        获取数据
        :return:
        """
        sql = """
        select * from coinpair
        """
        return pd.read_sql_query(sql, self.engine)


if __name__ == '__main__':
    c = CoinPair()
    c.insert()
    # print(c.get_data())
