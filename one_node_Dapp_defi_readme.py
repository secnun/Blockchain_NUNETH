

### 아래는 defi_1.py 에서 contract_code 부분 내용.
# Staking Token 정의 코드
# 예치 사용자 정보 저장용 staking_status = {}
'''
"contract_code" :"token_name = 'pySTAKINGTOKEN' 
                token_total_volume = 100000 
                token_owner = {'token_maker' : 10000}
                staking_status = {}",W
'''                

### 아래는 defi_1.py내 contract_function_getBalance 에 넣은 스마트컨트랙트 코드
def get_balance(user_id): #잔액 조회 기능 
    print('{} Balance is : '.format(user_id), token_owner[user_id])
    return token_owner[user_id]

def send_token(sender,recipent,amount): # 송금 기능
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

# 예치자 정보, 예치 금액 입력시 해당 예치자가 실제 존재하는지, 예치 금액보다 많은 잔액을 보유 중인지 확인
# 확인 후 예치정보(staking_status)에 예치자(staker)의 예치 내역을 저장.
def token_staking(staker,amount): # 토큰 예치 기능
    if staker in token_owner.keys():
        if get_balance(staker) > amount:
            token_owner[staker]  = token_owner[staker] - amount
            staking_status [len(staking_status)] =  {'staker':staker,'amount':amount}
            print("Staing Completed")
            get_balance(staker) 
            
        else:
            return "Insufficient Balance"
    else:
        return "Unavailable Staker id"

# 예치 이자 지급 함수 정의
# 예치 정보(staking_status)에 저장된 사용자들의 예치금의 10% 예치 이자 지급
def staking_yield(staking_status):
    for t in staking_status:
        print(staking_status[t])
        staking_status[t]['amount'] = staking_status[t]['amount'] * 1.1
    return staking_status