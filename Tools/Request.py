'''
封装post,get方法
'''

import requests
from Conf import Config
import json

conf = Config.Config()

def post_request(path, data):
    try:
        # 如果直接用data及为传统表单post请求, 需要先传成json格式
        r = requests.post(url = '{}?token={}'.format(path,conf.token), data = json.dumps(data), headers = conf.header)
        return r 
    except Exception as e:
        return {'text': repr(e)}

def get_request(path, data):
    try:
        r = requests.get(url = '{}?token={}'.format(path,conf.token), params=data, headers = conf.header)
        return r 
    except Exception as e:
        return {'text': repr(e)}