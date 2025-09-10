import requests
import json
import pandas as pd
import hashlib
import random
#####one_node.py 하나의 smartcontract 노드 객체 테스트를 위함.
## mining 


# 01. 트랜잭션 발생(transactions/new)
# 결과 예시 : {'contract_address': 'b9447537e7ef22c652181cf5fa6d11b795be3251c8763e1b5b58642ad38526d9', 'message': 'Transaction will be added to Block {2}'}
'''
headers = {'Content-Type' : 'application/json; charset=utf-8'}
data = {
        "sender": "test_from",
        "recipient": "smart_contract",
        "amount": 0,
        "smart_contract": {"contract_code":"print('Ｈello Ｓmart－Ｃontract')"}
}
result = requests.post("http://localhost:5000/transactions/new", headers=headers, data=json.dumps(data)).content
print(json.loads(result))
'''

# 02. mining 수행
# 결과 예시 : <Response [200]>
'''
headers = {'Content-Type' : 'application/json; charset=utf-8'}
res = requests.get("http://localhost:5000/mine")
print(res)
'''


#체인 확인(flask로 돌려놨으니 브라우저로 확인해도 됨.)
'''
headers = {'Content-Type' : 'application/json; charset=utf-8'}
res = requests.get("http://localhost:5000/chain", headers=headers)
print(json.loads(res.content))
'''
## 결과 예시 
#{
#  "chain": [
#    {
#      "hash": "1b938a55680ba1e9608a4980bc09a3cb776a3c8217a6045b09b18f1178488a0f",
#      "index": 1,
#      "nonce": 100,
#      "previous_hash": 1,
#      "timestamp": 1757484069.10596,
#      "transactions": []
#    },
#    {
#      "hash": "62af4ca07b040cad551afaab5a62855d1361c569dc7476e3c8a9c57014178cca",
#      "index": 2,
#      "nonce": 560502,
#      "previous_hash": "f08ff2c52ce359a74d2bbe10fcc184aeae7d016a37746fd85a7c3e8ffaeaf064",
#      "timestamp": 1757484153.52448,
#      "transactions": [
#        {
#          "amount": 0,
#          "recipient": "smart_contract",
#          "sender": "test_from",
#          "smart_contract": {
#            "contract_address": "b9c7922dc722995c4bd07697faac8584d8a4501ea9e8e4cf89151e9bbaa414f1",
#            "contract_code": "print('Ｈello Ｓmart－Ｃontract')"
#          },
#          "timestamp": 1757484128.18017
#        },
#        {
#          "amount": 0.1,
#          "recipient": "node_5000",
#          "sender": "master",
#          "smart_contract": {
#            "contract_address": "mining_profit"
#          },
#          "timestamp": 1757484153.52442
#        }
#      ]
#    }
#  ],
#  "length": 2
#}


# 스마트컨트랙트 호출
headers = {'Content-Type' : 'application/json; charset=utf-8'}
res = requests.get("http://localhost:5000/chain", headers=headers)
res_json = json.loads(res.content)

contract_address = "b9c7922dc722995c4bd07697faac8584d8a4501ea9e8e4cf89151e9bbaa414f1"


for _block in res_json['chain']:
    for _tx in _block['transactions']:
        if _tx['smart_contract']['contract_address'] == contract_address:
            exec( _tx['smart_contract']['contract_code'])
