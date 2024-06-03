# exchange_forecast.py

import json
from datetime import datetime, timedelta
import random

# 환율 변동 예측 기능을 위한 데이터 파일 경로
exchange_rate_file = 'exchange_rate.json'

def generate_exchange_rate_forecast(days=30):
    # 현재 환율 데이터 불러오기
    current_rates = load_current_exchange_rates()
    
    forecast = []
    for day in range(days):
        date = (datetime.now() + timedelta(days=day)).strftime('%Y-%m-%d')
        usd_rate = current_rates['USD'] * (1 + random.uniform(-0.05, 0.05))  # -5%에서 5% 변동
        jpy_rate = current_rates['JPY'] * (1 + random.uniform(-0.05, 0.05))
        forecast.append({'date': date, 'USD': usd_rate, 'JPY': jpy_rate})
    
    # 예측 데이터 저장
    save_exchange_rate_forecast(forecast)
    print(f"{days}일간의 환율 변동 예측이 완료되었습니다.")

def load_current_exchange_rates():
    # 현재 환율 데이터를 파일에서 불러오기
    if os.path.exists(exchange_rate_file):
        with open(exchange_rate_file, 'r') as file:
            data = json.load(file)
        return data
    else:
        return {"USD": 0.0009, "JPY": 0.1}

def save_exchange_rate_forecast(forecast):
    # 예측 데이터를 파일에 저장
    with open('exchange_rate_forecast.json', 'w', encoding='utf-8') as file:
        json.dump(forecast, file, ensure_ascii=False, indent=4)

def load_exchange_rate_forecast():
    # 예측 데이터를 파일에서 불러오기
    if os.path.exists('exchange_rate_forecast.json'):
        with open('exchange_rate_forecast.json', 'r', encoding='utf-8') as file:
            return json.load(file)
    else:
        return []

def view_exchange_rate_forecast():
    # 예측 데이터를 출력
    forecast = load_exchange_rate_forecast()
    if forecast:
        print("환율 변동 예측:")
        for entry in forecast:
            print(f"날짜: {entry['date']}, USD: {entry['USD']:.5f}, JPY: {entry['JPY']:.5f}")
    else:
        print("환율 변동 예측 데이터가 없습니다.")
