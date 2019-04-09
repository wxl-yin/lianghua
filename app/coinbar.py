import pandas as pd
from data.tushare_model import Model
from data.huobi_api import HuobiApi
from btcquant import EXCHANGES

class CoinPair(Model):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.huobi = HuobiApi()

    def insert(self):
        # 获取火币数据
        # datas = self.huobi.candlestick("adabtc",size=1000)
        # print(datas)
        client = EXCHANGES('huobi')
        symbol = "BTC_USDT"
        ticker = client.ticker(symbol)
        print(ticker)

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
