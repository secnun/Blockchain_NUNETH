import requests
import json
import pandas as pd
import hashlib
import random
#####one_node.py 하나의 NFT 테스트 위함.

'''
#### 01. NFT 생성
headers = {'Content-Type' : 'application/json; charset=utf-8'}
data = {
        "sender": "test_from",
        "recipient": "smart_contract",
        "amount": 0,
        "smart_contract": {"contract_code":"""
myNFT = {'NFT_NAME':'SMARTCONTRACT_NFT',
         'NFT_URL': 'https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png'}
                                            """}
}
result = requests.post("http://localhost:5000/transactions/new", headers=headers, data=json.dumps(data)).content
contract_address = json.loads(result)['contract_address']
print(contract_address) #이 주소를 아래 03 과정의 contract_adress에 넣어 확인해야 함.
'''
'''
# 02. 채굴을 통하여 거래내역을 블록에 저장
headers = {'Content-Type' : 'application/json; charset=utf-8'}
res = requests.get("http://localhost:5000/mine")
print(res)
'''

#### 03. 스마트컨트랙트 호출&확인
headers = {'Content-Type' : 'application/json; charset=utf-8'}
res = requests.get("http://localhost:5000/chain", headers=headers)
res_json = json.loads(res.content)

contract_address = "44ce5db246f781a0e7abb73614f494c01f242bbd1de141835e35bd8599f01a6a"


for _block in res_json['chain']:
    for _tx in _block['transactions']:
        if _tx['smart_contract']['contract_address'] == contract_address:
            exec( _tx['smart_contract']['contract_code'])

print(myNFT)
#결과 : {'NFT_NAME': 'SMARTCONTRACT_NFT', 'NFT_URL': 'https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png'}


####아래는 01, 02 과정을 통해 생성된 블럭 내용 결과
#{
#  "chain": [
#    {
#      "hash": "9a29ea2f4346b043792af8ab5cf3cdfa713fa46b299a855997995f478c8c26f9",
#      "index": 1,
#      "nonce": 100,
#      "previous_hash": 1,
#      "timestamp": 1757553164.08949,
#      "transactions": []
#    },
#    {
#      "hash": "7db13b494a4a1eed524572265158f5f26d51b4e7f1d7b2a6d0b7794ed401e0fd",
#      "index": 2,
#      "nonce": -320603,
#      "previous_hash": "3c4eb5ce8644b9c9c96f966167e236a87c8aca83154abeb535f32ce72a1cb66f",
#      "timestamp": 1757553253.61873,
#      "transactions": [
#        {
#          "amount": 0,
#          "recipient": "smart_contract",
#          "sender": "test_from",
#          "smart_contract": {
#            "contract_address": "44ce5db246f781a0e7abb73614f494c01f242bbd1de141835e35bd8599f01a6a",
#            "contract_code": "\nmyNFT = {'NFT_NAME':'SMARTCONTRACT_NFT',\n         'NFT_URL': 'https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png'}\n                                            "
#          },
#          "timestamp": 1757553210.04857
#        },
#        {
#          "amount": 0.1,
#          "recipient": "node_5000",
#          "sender": "master",
#          "smart_contract": {
#            "contract_address": "mining_profit"
#          },
#          "timestamp": 1757553253.61869
#        }
#      ]
#    }
#  ],
#  "length": 2
#}