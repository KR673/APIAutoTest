import pytest
import random
import requests
import json
from Tools import Request
from Tools import RandomParam

def result_judge(data):
    try:
        result = json.loads(data.text)
        return result['code'] == 0 or  result['code'] == 200
    except:
        return False

@pytest.mark.repeat(100)
def test_answer():
    url = 'http://localhost:8089/crm-manager-master/sys/login'
    data = {"username": "王晓波_14944","password": "123456@"}
    assert result_judge(Request.post_request(url, json.dumps(data)))
    RandomParam.get_param('')
    assert random.randint(0, 100) == 50