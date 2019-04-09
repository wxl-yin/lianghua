from config.settings import Access_Key, Secret_Key
from datetime import datetime
from urllib import parse
import hashlib,hmac,base64
from utils.send_method import SendMethod



class HuobiApi(object):
    """
    火币API接口封装
    """

    DOMAIN = "api.huobi.pro"
    MAIN_URL = "https://api.huobi.pro"
    # 请求市场信息
    MARKET_URL = "/market/history/kline"

    # 请求方式
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"

    """
    时间粒度
    """
    MIN1 = "1min"
    MIN5 = "5min"
    MIN15 = "15min"
    MIN30 = "30min"
    MIN60 = "60min"
    DAY1 = "1day"
    MON1 = "1mon"
    WEEK1 = "1week"
    YEAR1 = "1year"

    def __init__(self):
        self.send = SendMethod()

    def _sign(self, url, method, data):
        """

        :param url: API URL
        :param method: 请求方式
        :param data: 请求数据
        :return:
        """
        # 拼接请求头
        base_params = [
            method + "\n",
            self.DOMAIN + "\n",
            url + "\n"
        ]
        base_params_str = "".join(base_params)

        # 封装参数
        # print(base_params_str)
        params_str = self._params(data)
        # print(params_str)

        # 拼接签名字符串
        signature_str = base_params_str + params_str
        # print(signature_str)

        secret = Secret_Key.encode("utf-8")
        signature_str = signature_str.encode("utf-8")
        # 请求完成的签名字符串再加密
        sign_tmp = hmac.new(secret,signature_str,digestmod=hashlib.sha256).digest()
        # print(sign)
        sign = base64.b64encode(sign_tmp).decode("utf-8")
        # print(sign)

        # 完成整的url
        full_url = self.MAIN_URL + url + "?" + params_str + "&Signature=" + sign
        return full_url

    def _params(self, data: dict):
        """
        参数处理 排序并编码
        :param data:
        :return:
        """
        params = {}
        params.update(data)
        params.update({"AccessKeyId": Access_Key})
        params.update({"SignatureMethod": "HmacSHA256"})
        params.update({"SignatureVersion": "2"})
        timestamp = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S")
        params.update({"Timestamp": timestamp})

        # 排序
        sorted_params = sorted(params.items(),key=lambda k:k[0])

        # urlencode 编码
        return parse.urlencode(sorted_params)

    def candlestick(self, symbol, period="60min", size=150, *args, **kwargs):
        """
        获取蜡烛数据
        :param symbol: 交易对
        :param period: 时间频率
        :param size: 数据长度
        :param args:
        :param kwargs:
        :return:
        """
        # 组成数据,发起请求
        data = {
            'symbol': symbol,
            'period': period,
            'size': size
        }
        # 生成签名的url
        full_url = self._sign(self.MARKET_URL, self.GET, data)

        # 发起请求
        res = self.send.run_main(self.GET,url=full_url)

        # {'id': 1554789600, 'open': 5142.91, 'close': 5141.02, 'low': 5140.62, 'high': 5142.91, 'amount': 3.6900143526015823, 'vol': 18973.42932129, 'count': 87}
        if res['status'] == "ok":
            return res['data']
        else:
            raise Exception("获取candlestick数据失败")

if __name__ == '__main__':
    hb = HuobiApi()
    a = hb.candlestick('btcusdt')
    print(a)
