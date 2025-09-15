import requests
import json
import pandas as pd
import hashlib
import random


### 01. 발행자 토큰 확인
headers = {'Content-Type' : 'application/json; charset=utf-8'}
res = requests.get("http://localhost:5000/chain", headers=headers)
res_json = json.loads(res.content)

contract_address="b84fc82f9b8f5f6608e24f9be32899a7d46fa703c6c2f085cf0002f2ddd29051" #확인 필요

for _block in res_json['chain']:
    for _tx in _block['transactions']:
        if _tx['smart_contract']['contract_address'] == contract_address:
            exec( _tx['smart_contract']['contract_code'])
            break

exec(_tx['smart_contract']['contract_function_getBalance'])
get_balance('token_maker') #발행자 -> 생성과 동시에 발행량 그대로를 가짐. 1만개 확인


### 02. 토큰 예치 수행
# 이거 수행시 위 코드 주석처리x, get_balance 때문.
exec(_tx['smart_contract']['contract_function_token_staking'])
token_staking('token_maker',100)

### 03. 예치자 이자 지급
exec(_tx['smart_contract']['contract_function_staking_yield'])
staking_yield(staking_status)

exec(_tx['smart_contract']['contract_function_staking_yield'])
staking_yield(staking_status)

exec(_tx['smart_contract']['contract_function_staking_yield'])
staking_yield(staking_status)