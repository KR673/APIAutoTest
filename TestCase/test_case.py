import pytest
import random
import requests
import json
from Tools import Request
from Tools import RandomParam

def result_judge(data):
    try:
        message = json.loads(data.text)
        assert message['code'] == 0 or  message['code'] == 200, json.loads(data.text)
    except:
        assert False, data.text

@pytest.mark.repeat(5)
def test_selectJiHuiChangeLog():
    url = 'http://localhost:8089/crm-manager-master/sys/jiHuiZongKu/selectJiHuiChangeLog'
    data = RandomParam.get_param(['userGroupId|int|1|'])
    result = Request.get_request(url, data)
    result_judge(result)

@pytest.mark.repeat(5)
def test_selectGouTongJiLuInDifferentPeriod():
    url = 'http://localhost:8089/crm-manager-master/sys/jiHuiZongKu/selectGouTongJiLuInDifferentPeriod'
    data = RandomParam.get_param(['tableId|int|0|','userGroupId|int|1|','page|int|1|1','step|int|1|10'])
    result = Request.post_request(url, data)
    result_judge(result)