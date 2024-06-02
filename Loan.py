import Account_book


user1 = Account_book.Account_book("이현철", 5000)

user1.show_account()
user1.put_credit_score()

# 신용 점수에 따라서 다른 금융권 추천
def Loan(obj):
    if(obj.get_credit_score() >= 800):
        print("1금융권 (은행)을 추천합니다.")
    elif(obj.get_credit_score() >= 700):
        print("2금융권 (저축은행, 보험사, 카드사)을 추천합니다.")
    elif(obj.get_credit_score() >= 600):
        print("3금융권 (캐피탈사, 대부업채)을 추천합니다.")
    elif(obj.get_credit_score() >= 200):
        print("4금융권 (사채)을 추천합니다.")
        
    
    else:
        ans = input("장기매매... 가격 알아봐드릴까요? (y/n): ")
        if(ans == 'y'):
            print("\n---귀신 헬리콥터('귀하의 신장', Heart(심장), Liver(간), Cornea(각막), Pancreas(췌장), Tendon(힘줄), Retina(망막)---\n\n"
                  "| 신장(2억9,560만원), 간(1억7,000만원), 심장(1억3,420만원), 소장(280만원),\n"
                  "| 심장동맥(170만원), 쓸개(137만원), 두피(68만원), 위(57만원), 어깨(56만원),\n"
                  "| 손과 팔(43만원), 혈액 0.473L(38만원), 피부 평방인치당(1만1000원)")
            print("\n사람은 신장이 2개라는 것을 아시나요?")
        else:
            print("다행이에요. 열심히 일을 하시는 것을 추천드려요.")     


Loan(user1)