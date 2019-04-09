import requests

"""
    1. 将所有的请求方式封装成一个类

    2. 只需要调用一个方法，通过一个参数区别不同的方法
"""


class SendMethod(object):

    def _send_get(self, url, data=None, **kwargs):
        """
            封装get请求
        """
        # 发送请求
        response = requests.get(url=url, params=data, **kwargs)
        # 获取结果
        return response.json()

    def _send_post(self, url, data=None, json=None, **kwargs):
        """
           封装post请求
       """
        # 发送请求
        response = requests.post(url=url, data=data, json=json, **kwargs)
        # 返回结果
        return response.json()

    def _send_put(self, url, data=None, json=None, **kwargs):
        """
           封装put请求
       """
        # 发送请求
        response = requests.put(url=url, json=json, data=data, **kwargs)
        # 获取
        return response.json()

    def _send_delete(self, url, data=None, **kwargs):
        """
            封装delete请求
        """
        # 发送请求
        response = requests.delete(url=url, params=data, **kwargs)
        # 获取状态码
        return response.status_code

    def run_main(self, method, url, data=None, json=None, **kwargs):
        """
            发送所有的请求，都只调用该方法
            :param method 请求方式名称
            :param url 请求地址
            :param data 请求数据是字典
            :param json 请求参数为json数据
            :return: 返回响应的结果
        """
        if method == "get":
            res = self._send_get(url=url, data=data, **kwargs)
        elif method == "post":
            res = self._send_post(url=url, data=data, json=json, **kwargs)
        elif method == "put":
            res = self._send_put(url=url, data=data, json=json, **kwargs)
        elif method == "delete":
            res = self._send_delete(url=url, data=data, **kwargs)
        else:
            res = None

        # 返回最后的结果
        return res


if __name__ == '__main__':
    # 发送get请
    send = SendMethod()
    # url = "http://127.0.0.1:8000/api/departments/"
    # rs = send.run_main("get",url=url)
    # print(rs)

    # url
    url = "http://127.0.0.1:8000/api/departments/"
    # 参数
    data = {
        "data": [
            {
                "dep_id": "T01",
                "dep_name": "Test学院",
                "master_name": "Test-Master",
                "slogan": "Here is Slogan"
            }
        ]
    }
    res = send.run_main('post', url=url, json=data)
    print(res)
