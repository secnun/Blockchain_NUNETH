import requests
import json
import pandas as pd
import hashlib
import random


####생성된 토큰을 통해 추가적인 간단 기능 테스트
headers = {'Content-Type' : 'application/json; charset=utf-8'}
res = requests.get("http://localhost:5000/chain", headers=headers)
res_json = json.loads(res.content)

# 테스트할 contract_address (해시값)
make_token2 = "ab9deae395481ba7130882638090e33f16f619ecf4c45b23c644a59f26b825fc"

# ---------------------------
# 2. 트랜잭션 탐색 및 exec
# ---------------------------
for _block in res_json['chain']:
    for _tx in _block['transactions']:
        if _tx['smart_contract']['contract_address'] == make_token2:
            # 1) 로컬 네임스페이스 준비 (변수와 함수가 모두 여기 저장됨)
            local_vars = {}

            # 2) 토큰 코드(변수) 실행
            exec(_tx['smart_contract']['contract_code'], local_vars, local_vars)

            # 3) 함수 코드 실행 (get_balance, send_token)
            exec(_tx['smart_contract']['contract_function_getBalance'], local_vars, local_vars)
            exec(_tx['smart_contract']['contract_function_sendToken'], local_vars, local_vars)

            # 4) 함수 꺼내오기
            get_balance = local_vars['get_balance']
            send_token = local_vars['send_token']

            # ---------------------------
            # 5. 결과 출력
            # ---------------------------
            print("=== exec 실행 결과 ===")
            #print(local_vars)  # 모든 변수/함수 확인

            # 토큰 정보
            print(f"[+] token_name: {local_vars.get('token_name')}")
            print(f"[+] token_total_volume: {local_vars.get('token_total_volume')}")
            print("======================")
            # 여기서 get_balance, send_token 자체 print 하고 있어서 아래처럼 print 찍으면 2번씩 찍히므로 굳이 필요없음.
            # USER1 잔액 확인
            #print(f"[+] USER1 balance: {get_balance('USER1')}")

            #토큰 전달 및 확인
            print("[+] USER1 -> USER2")
            send_token('USER1','USER2',50)
            print("[+] USER1 -> USER3")
            send_token('USER1','USER3',3000)
            #print(f"[+] USER1 balance: {get_balance('USER1')}")

            print("\n======최종 지갑 확인======")
            get_balance('USER1')
            get_balance('USER2')
            get_balance('USER3')

            break

