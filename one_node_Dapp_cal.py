import requests
import json
import pandas as pd
import hashlib
import random


### 01. 계산을 위한 값을 받는 스마트컨트랙트
## 숫자2개, 부호 고정 입력 받음
headers = {'Content-Type' : 'application/json; charset=utf-8'}
data = {
        "sender": "test_from",
        "recipient": "smart_contract",
        "amount": 0,
        "smart_contract": {
                           "contract_code" : "calculate_result = {}{}{}"}
}
result = requests.post("http://localhost:5000/transactions/new", headers=headers, data=json.dumps(data)).content
contract_address = json.loads(result)['contract_address']

headers = {'Content-Type' : 'application/json; charset=utf-8'}
res = requests.get("http://localhost:5000/mine")
print(res)


### 02. 값을 받아 더하는 요청
## EVM에서 요청하는게 아닌 한계로 직접 파이썬 엔진을 활용한 덧셈 처리
headers = {'Content-Type' : 'application/json; charset=utf-8'}
res = requests.get("http://localhost:5000/chain", headers=headers)
res_json = json.loads(res.content)

for _block in res_json['chain']:
    for _tx in _block['transactions']:
        if _tx['smart_contract']['contract_address'] ==contract_address:
            exec( _tx['smart_contract']['contract_code'].format(120,"+",360))
            break
print(calculate_result)        


### 03. 값을 받아 곱하는 요청
headers = {'Content-Type' : 'application/json; charset=utf-8'}
res = requests.get("http://localhost:5000/chain", headers=headers)
res_json = json.loads(res.content)

for _block in res_json['chain']:
    for _tx in _block['transactions']:
        if _tx['smart_contract']['contract_address'] ==contract_address:
            exec( _tx['smart_contract']['contract_code'].format(3,"*",5))
            break
print(calculate_result)        


### 04. 값을 받아 나누는 요청
headers = {'Content-Type' : 'application/json; charset=utf-8'}
res = requests.get("http://localhost:5000/chain", headers=headers)
res_json = json.loads(res.content)

for _block in res_json['chain']:
    for _tx in _block['transactions']:
        if _tx['smart_contract']['contract_address'] ==contract_address:
            exec( _tx['smart_contract']['contract_code'].format(12000,"/",12))
            break
print(calculate_result)        