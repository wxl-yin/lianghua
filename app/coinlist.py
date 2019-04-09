from data.tushare_model import Model
import tushare as ts
import pandas as pd

"""
常用参数说明：

name:表名，pandas会自动创建表结构
con：数据库连接，最好是用sqlalchemy创建engine的方式来替代con
flavor:数据库类型 {‘sqlite’, ‘mysql’}, 默认‘sqlite’，如果是engine此项可忽略
schema:指定数据库的schema，默认即可
if_exists:如果表名已存在的处理方式 {‘fail’, ‘replace’, ‘append’},默认‘fail’
index:将pandas的Index作为一列存入数据库，默认是True
index_label:Index的列名
chunksize:分批存入数据库，默认是None，即一次性全部写人数据库
dtype:设定columns在数据库里的数据类型，默认是None
"""


class CoinList(Model):
    """
    # 接口：coinlist
    # 描述：获取全球数字货币基本信息，包括发行日期、规模、所基于的公链和算法等。
    """

    def __init__(self, *args, **kwargs):
        super(CoinList, self).__init__(*args, **kwargs)
        # 初始化
        self.pro = ts.pro_api()

    def insert(self):
        """
        将数字货币信息保存到数据库
        :return:
        """
        # 获取数字火币列表
        df = self.pro.coinlist(start_date='20170101', end_date='20190401')
        # 保存到数据
        df.to_sql("coinlist", con=self.engine, index=False, if_exists="append")

    def get_data(self):
        """
        查询所有数字火币信息
        :return:
        """
        sql = "select * from coinlist"
        df = pd.read_sql_query(sql,self.engine)
        return df

if __name__ == '__main__':
    coin = CoinList()
    # print(coin.get_data())
    df = coin.get_data()
    print(df)