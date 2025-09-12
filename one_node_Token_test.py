import requests
import json
import pandas as pd
import hashlib
import random

'''
####01. 기본 토큰 생성 (1만개)
headers = {'Content-Type' : 'application/json; charset=utf-8'}
data = {
        "sender": "test_from",
        "recipient": "smart_contract",
        "amount": 0,
        "smart_contract": {"contract_address":"make_token",
                           "contract_code" :"token_name = 'pyTOKEN' \ntoken_total_volume = 10000"
                                            }
            }
requests.post("http://localhost:5000/transactions/new", headers=headers, data=json.dumps(data)).content

headers = {'Content-Type' : 'application/json; charset=utf-8'}
res = requests.get("http://localhost:5000/mine")
print(res)
'''

'''
###02. 실제 사용가능하도록 토큰 생성 테스트
## 01과는 별개임. 01는 간단 테스트용
headers = {'Content-Type' : 'application/json; charset=utf-8'}
data = {
        "sender": "test_from",
        "recipient": "test_to",
        "amount": 3,
        "smart_contract": {"contract_address":"make_token2",
                           "contract_code" :"token_name = 'pyTOKEN' \ntoken_total_volume = 10000\ntoken_owner = {'USER1' : 10000}",
                           "contract_function_getBalance" :"""
def get_balance(user_id):
    print('{} Balance is : '.format(user_id), token_owner[user_id])
    return token_owner[user_id]
""",
                           "contract_function_sendToken" :"""
def send_token(sender,recipent,amount):
    if sender in token_owner.keys():
        if get_balance(sender) > amount:
            token_owner[sender]  = token_owner[sender] - amount
            if recipent in token_owner.keys():
                token_owner[recipent]  = token_owner[recipent] + amount
            else :
                token_owner[recipent]  =  amount
            print("Transaction Completed")
            get_balance(sender) 
            get_balance(recipent) 

        else:
            return "Insufficient Balance"
    else:
        return "Unavailable Sender id"
"""}
}
requests.post("http://localhost:5000/transactions/new", headers=headers, data=json.dumps(data)).content

headers = {'Content-Type' : 'application/json; charset=utf-8'}
res = requests.get("http://localhost:5000/mine")
print(res)
'''

'''
####03 확인
headers = {'Content-Type' : 'application/json; charset=utf-8'}
res = requests.get("http://localhost:5000/chain", headers=headers)
res_json = json.loads(res.content)

make_token2="ab9deae395481ba7130882638090e33f16f619ecf4c45b23c644a59f26b825fc" #make_token2 해시값
#if _tx['smart_contract']['contract_address'] == 'make_token2' 에서 make_token2값이 해싱된 상태이기 때문에 contract_address인 make_token2를 알아야 함.
#여기선 하드코딩으로 박아놓음. 

for _block in res_json['chain']:
    for _tx in _block['transactions']:
        if _tx['smart_contract']['contract_address'] == 'make_token2':
            exec( _tx['smart_contract']['contract_code'])
            break
'''

####03-1 확인
##03 으로 테스트를 할 수는 있으나, 내 쉘 화면에서는 출력결과를 보지 못하므로 아래와 같이 구성하여 테스트하면 내 화면에 테스트(exec결과)결과 볼 수 있음.
headers = {'Content-Type' : 'application/json; charset=utf-8'}
res = requests.get("http://localhost:5000/chain", headers=headers)
res_json = json.loads(res.content)

make_token2 = "ab9deae395481ba7130882638090e33f16f619ecf4c45b23c644a59f26b825fc"  # 해시값

for _block in res_json['chain']:
    for _tx in _block['transactions']:
        if _tx['smart_contract']['contract_address'] == make_token2:
            # 로컬 네임스페이스 준비
            local_vars = {}
            exec(_tx['smart_contract']['contract_code'], {}, local_vars)

            # exec로 생성된 변수/함수 확인
            print("=== exec 실행 결과 ===")
            print(local_vars)

            # 만약 토큰 이름/발행량 확인하고 싶으면
            if "token_name" in local_vars:
                print("token_name:", local_vars["token_name"])
            if "token_total_volume" in local_vars:
                print("token_total_volume:", local_vars["token_total_volume"])

            break



#### 01 생성 결과
#{
#  "chain": [
#    {
#      "hash": "b57335438fa61ab4f75c040f92db4bced24d1fd7e39d506f045db76d050679a8",
#      "index": 1,
#      "nonce": 100,
#      "previous_hash": 1,
#      "timestamp": 1757641503.11568,
#      "transactions": []
#    },
#    {
#      "hash": "32f8afc844d24e9a1634e1bfe7c59605dde0020b452a05c0e867ef9c12237afb",
#      "index": 2,
#      "nonce": 560502,
#      "previous_hash": "43b29002dbae2d3341cef12c410acbb10761f96dc1bbc3024bb8e9fb7a15feb5",
#      "timestamp": 1757641588.92474,
#      "transactions": [
#        {
#          "amount": 0,
#          "recipient": "smart_contract",
#          "sender": "test_from",
#          "smart_contract": {
#            "contract_address": "34be4e90e44d5fbf54d662f4e1d80784009573ca49cf1996432b924f0e132211",
#            "contract_code": "token_name = 'pyTOKEN' \ntoken_total_volume = 10000"
#          },
#          "timestamp": 1757641588.8698
#        },
#        {
#          "amount": 0.1,
#          "recipient": "node_5000",
#          "sender": "master",
#          "smart_contract": {
#            "contract_address": "mining_profit"
#          },
#          "timestamp": 1757641588.92469
#        }
#      ]
#    }
#  ],
#  "length": 2
#}



####02 생성 결과
#{
#  "chain": [
#    {
#      "hash": "6fc45a5ae27a3bbe4dde9407a23bcb6ee6a3dbbfe54ded540a65983a1b22c0ca",
#      "index": 1,
#      "nonce": 100,
#      "previous_hash": 1,
#      "timestamp": 1757641771.73981,
#      "transactions": []
#    },
#    {
#      "hash": "3cb19733ad486b9f48d2dfe889d47ab0fae21bcaa1c298c0b7c4a92c5536bcb8",
#      "index": 2,
#      "nonce": 889040,
#      "previous_hash": "22217dac5dd3eb033a8cad62b58f1801b3e9bda2499b38fcfc9f9475f358caa2",
#      "timestamp": 1757641778.01029,
#      "transactions": [
#        {
#          "amount": 3,
#          "recipient": "test_to",
#          "sender": "test_from",
#          "smart_contract": {
#            "contract_address": "8e18c1cf60389051dbd1c7bbdfb15e12446d8e683cd197a9bb5b062fe326f3df",
#            "contract_code": "token_name = 'pyTOKEN' \ntoken_total_volume = 10000\ntoken_owner = {'USER1' : 10000}",
#            "contract_function_getBalance": "\ndef get_balance(user_id):\n    print('{} Balance is : '.format(user_id), token_owner[user_id])\n    return token_owner[user_id]\n",
#            "contract_function_sendToken": "\ndef send_token(sender,recipent,amount):\n    if sender in token_owner.keys():\n        if get_balance(sender) \u003E amount:\n            token_owner[sender]  = token_owner[sender] - amount\n            if recipent in token_owner.keys():\n                token_owner[recipent]  = token_owner[recipent] + amount\n            else :\n                token_owner[recipent]  =  amount\n            print(\"Transaction Completed\")\n            get_balance(sender) \n            get_balance(recipent) \n\n        else:\n            return \"Insufficient Balance\"\n    else:\n        return \"Unavailable Sender id\"\n"
#          },
#          "timestamp": 1757641777.99577
#        },
#        {
#          "amount": 0.1,
#          "recipient": "node_5000",
#          "sender": "master",
#          "smart_contract": {
#            "contract_address": "mining_profit"
#          },
#          "timestamp": 1757641778.01024
#        }
#      ]
#    }
#  ],
#  "length": 2
#}



###03-1 확인 결과
#=== exec 실행 결과 ===
#{'token_name': 'pyTOKEN', 'token_total_volume': 10000, 'token_owner': {'USER1': 10000}}
#token_name: pyTOKEN
#token_total_volume: 10000