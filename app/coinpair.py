import pandas as pd
import tushare as ts
from data.tushare_model import Model
from datetime import datetime,timedelta
import pymysql

class CoinPair(Model):
    def insert(self):
        # 初始化
        pro = ts.pro_api()

        # 获取火币数据
        trade_date_tmp = datetime.now()-timedelta(days=1)
        trade_date = trade_date_tmp.strftime("%Y%m%d")
        df = pro.coinpair(exchange='huobi', trade_date=trade_date)

        # 保存到数据库
        # df.to_sql('coinpair',self.engine,index=False)
        # 数据长度
        c_len = df.shape[0]

        args = []
        for i in range(c_len):
            res_list = list(df.ix[i])
            res_list[0] = datetime.strptime(res_list[0],"%Y%m%d").strftime("%Y-%m-%d")
            # 存储到数据列表
            args.append(res_list)

        # 准备sql语句
        sql = """
        insert into coinpair(trade_date,exchange,exchange_pair,ts_pair)
        values 
        (%s,%s,%s,%s)
        """
        res = self.db.executemany(sql,args)
        print(res)




    def get_data(self):
        """
        获取数据
        :return:
        """
        sql = """
        select * from coinpair
        """
        return pd.read_sql_query(sql,self.engine)

if __name__ == '__main__':
    c = CoinPair()
    # c.insert()
    print(c.get_data())
