import requests
from forex_python.converter import CurrencyRates

# 환율전환에 있는 3개의 기능 중 몇번재 기능을 선택하는지에 따라서 DollarWonChange1,2,3 중 무슨 함수를 사용할지 결정됩니다.
# 3개의 DollarWonChange 함수 전부 외부 API를 이용해 환율 데이터를 불러오는 것까지는 동일합니다.
# 환율 데이터를 불러온 이후의 코드부터 3개의 함수가 서로 달라집니다.
# DollarWonChange1() == 1: 원화달러 현재환율 확인하기 == 환율 데이터를 불러와서 현재 1달러에 원화로 얼마인지 출력합니다.
# DollarWonChange2(Won) == 2: 전환: 원화 >> 달러 == 사용자에게 입력받은 원화를 환율데이터를 이용해 달러값으로 전환하여 출력합니다.
# DollarWonChange3(Dollar) == 3: 전환: 달러 >> 원화 == 사용자에게 입력받은 달러를 환율데이터를 이용해 원화값으로 전환하여 출력합니다.
def DollarWonChange1():
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        url = 'https://quotation-api-cdn.dunamu.com/v1/forex/recent?codes=FRX.KRWUSD'
        ExchangeList = requests.get(url, headers=headers).json()
        HowExchange = ExchangeList[0]['basePrice']
        print(f"현재 환율은 1달러에 ", HowExchange, "원 입니다")
    except ValueError:
        print("에러발생. 다시 시도해주세요.")

def DollarWonChange2(Won):
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        url = 'https://quotation-api-cdn.dunamu.com/v1/forex/recent?codes=FRX.KRWUSD'
        ExchangeList = requests.get(url, headers=headers).json()
        HowExchange = ExchangeList[0]['basePrice']
        HowDollar = Won / HowExchange
        print(Won, "원은 현재 환율로 ", HowDollar, "달러 입니다")
    except ValueError:
        print("에러발생. 다시 시도해주세요.")

def DollarWonChange3(Dollar):
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        url = 'https://quotation-api-cdn.dunamu.com/v1/forex/recent?codes=FRX.KRWUSD'
        ExchangeList = requests.get(url, headers=headers).json()
        HowExchange = ExchangeList[0]['basePrice']
        HowWon = Dollar * HowExchange
        print(Dollar, "원은 현재 환율로 ", HowWon, "원 입니다")
    except ValueError:
        print("에러발생. 다시 시도해주세요.")

b_is_exit = 0
while not b_is_exit:
    func = input("기능 입력 (? 입력시 도움말) : ")

    if func == "1":
        break
    elif func == "2":
        break
    elif func == "3":
        break

    elif func == "환율전환":
        while True:
            ChooseWhat = input("1: 원화달러 현재환율 확인하기\n2: 전환: 원화 >> 달러\n3: 전환: 달러 >> 원화\n원하는 기능을 선택해주세요: ")
            if ChooseWhat == "1":
                DollarWonChange1()
                break
            elif ChooseWhat == "2":
                Won = int(input("원화를 입력해주세요: "))
                DollarWonChange2(Won)
                break
            elif ChooseWhat == "3":
                Dollar = int(input("달러를 입력해주세요: "))
                DollarWonChange3(Dollar)
                break
            else:
                print("1,2,3 중에 다시 입력해주세요: ")
                # 1,2,3이 아닌 다른 값을 입력할 경우, 환율전환 내 3가지 기능 중 하나를 선택하는 작업부터 다시 시작합니다.

    elif func == "?":
        print("도움말 입력.")

        break

    else:
        b_is_exit = not b_is_exit

