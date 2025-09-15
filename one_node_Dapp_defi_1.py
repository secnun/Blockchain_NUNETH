import requests
import json
import pandas as pd
import hashlib
import random

'''
### 01. Defi 생성
headers = {'Content-Type' : 'application/json; charset=utf-8'}
data = {
        "sender": "test_from",
        "recipient": "test_to",
        "amount": 3,
        "smart_contract": {
                           "contract_code" :"token_name = 'pySTAKINGTOKEN' \ntoken_total_volume = 100000\ntoken_owner = {'token_maker' : 10000}\nstaking_status = {}",
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
""",
                           "contract_function_token_staking" :"""
def token_staking(staker,amount):
    if staker in token_owner.keys():                       ## 예치자(staker)가 실제 존재하는 사용자인지 확인
        if get_balance(staker) > amount:                   ## 예치자(staker)의 잔고가 예치 금액보다 많은지 확인
            token_owner[staker]  = token_owner[staker] - amount   ## 예치자(staker)의 잔고에서 예치 금액 제외
            staking_status [len(staking_status)] =  {'staker':staker,'amount':amount}  
            ## 예치 정보(staking_status)에 예치자(staker)의 예치내역 저장
            print("Staing Completed")
            get_balance(staker) 
            
        else:
            return "Insufficient Balance"
    else:
        return "Unavailable Staker id"
""",
                           "contract_function_staking_yield" :"""
def staking_yield(staking_status):                                 ## 예치 이자 지급함수
    for t in staking_status:
        print(staking_status[t])
        staking_status[t]['amount'] = staking_status[t]['amount'] * (1+0.1)    ## 예치 이자가 10% 지급된 금액으로 예치금 변경
    return staking_status
"""                       

                                            }
            }
result = requests.post("http://localhost:5000/transactions/new", headers=headers, data=json.dumps(data)).content
contract_address = json.loads(result)['contract_address']


headers = {'Content-Type' : 'application/json; charset=utf-8'}
res = requests.get("http://localhost:5000/mine")
print(res)
'''


### 02. 토큰 생성 여부 확인
headers = {'Content-Type' : 'application/json; charset=utf-8'}
res = requests.get("http://localhost:5000/chain", headers=headers)
res_json = json.loads(res.content)

contract_address="b84fc82f9b8f5f6608e24f9be32899a7d46fa703c6c2f085cf0002f2ddd29051" #확인 필요

for _block in res_json['chain']:
    for _tx in _block['transactions']:
        if _tx['smart_contract']['contract_address'] == contract_address:
            exec( _tx['smart_contract']['contract_code'])
            break

print(f"토큰명 : {token_name}")
print(f"총 토큰 개수 : {token_total_volume} 개")
