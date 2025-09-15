import requests
import json
import pandas as pd
import hashlib
import random


### 01. 복권 
headers = {'Content-Type' : 'application/json; charset=utf-8'}
data = {
        "sender": "test_from",
        "recipient": "smart_contract",
        "amount": 0,
        "smart_contract": {
                           "contract_code" : """
def Lottery():
    lottery_number = random.sample(range(1,46),6)
    lottery_number = sorted(lottery_number, key=lambda x: x)
    lottery_number
    print(lottery_number) 
    return lottery_number
                           """}
}
result = requests.post("http://localhost:5000/transactions/new", headers=headers, data=json.dumps(data)).content
contract_address = json.loads(result)['contract_address']

headers = {'Content-Type' : 'application/json; charset=utf-8'}
res = requests.get("http://localhost:5000/mine")
print(res)



### 02. 확인
headers = {'Content-Type' : 'application/json; charset=utf-8'}
res = requests.get("http://localhost:5000/chain", headers=headers)
res_json = json.loads(res.content)

contract_address="87c6fc10d6b5d713f14656d3db9eff44da47ec3e20833865fc130d1e24783ddf" # 직접 확인 필요

for _block in res_json['chain']:
    for _tx in _block['transactions']:
        if _tx['smart_contract']['contract_address'] ==contract_address:
            exec( _tx['smart_contract']['contract_code'])
            break   

print(Lottery())       
