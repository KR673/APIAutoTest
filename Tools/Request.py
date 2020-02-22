'''
封装post,get方法
'''

import requests
from Conf import Config

conf = Config.Config()

def post_request(path, data):
    return requests.post(url = '{}?toke={}'.format(path,conf.token), data = data, headers = conf.header)


def get_request(path, data):
     return requests.get(url = '{}?toke={}'.format(path,conf.token), data = data, headers = conf.header)