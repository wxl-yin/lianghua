import pymysql
import logging


class Database(object):
    """
    数据库操作类
    """

    def __init__(self, password, db, host='127.0.0.1', user='root', charset='utf8', port=3306,
                 cursorType=pymysql.cursors.SSDictCursor):

        self.password = password
        self.db = db
        self.host = host
        self.user = user
        self.charset = charset
        self.port = port
        self.cursorType = cursorType

        # 连接数据
        self.connect()

    def connect(self):
        """
        连接数据
        :return:
        """
        self.cnn = pymysql.connect(host=self.host, port=self.port, user=self.user, password=self.password,
                                   charset=self.charset, db=self.db)

    def get_cursor(self):
        # 创建游标
        return self.cnn.cursor(cursor=self.cursorType)

    def execute(self, sql, args=None):
        """
        执行写操作
        :param sql:
        :param args:
        :return:
        """
        cursor = self.get_cursor()
        try:
            num = cursor.execute(sql, args)
            if num == 0:
                raise Exception("受影响行数为0")

            self.cnn.commit()
            cursor.close()
            return True
        except Exception as e:
            # 输出错误信息
            logging.error(e)
            self.cnn.rollback()
            return False

    def executemany(self, sql, args=None):
        """
        执行写操作
        :param sql:
        :param args:
        :return:
        """
        cursor = self.get_cursor()
        try:
            num = cursor.executemany(sql, args)
            if num == 0:
                raise Exception("受影响行数为0")

            self.cnn.commit()
            cursor.close()
            return True
        except Exception as e:
            # 输出错误信息
            logging.error(e)
            self.cnn.rollback()
            return False
    def fetchall(self, sql, args=None):
        """
        查询多条记录
        :param sql:
        :param args:
        :return:
        """
        cursor = self.get_cursor()
        try:
            cursor.execute(sql, args)
            data = cursor.fetchall()
            cursor.close()
            if len(data) == 0:
                return None
            else:
                return data
        except Exception as e:
            logging.error(e)
            return None

    def fetchone(self, sql, args=None):
        """
        查询一条记录
        :param sql:
        :param args:
        :return:
        """
        cursor = self.get_cursor()
        try:
            cursor.execute(sql, args)
            data = cursor.fetchone()
            cursor.close()
            if data:
                return data
            else:
                return None
        except Exception as e:
            logging.error(e)
            return None

    def __del__(self):
        self.cnn.close()


if __name__ == '__main__':
    db = Database(password='root', db='management')
    res = db.fetchall("select * from1 users where id=9")
    print(res)
