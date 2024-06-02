import schedule
import time

def send_notification():
    # 이 함수 내에서 알림을 보내는 로직을 구현합니다.
    # 예를 들어, print 함수를 사용하여 콘솔에 메시지를 출력할 수 있습니다.
    print("알림: 오늘의 지출을 입력하세요!")

# 매일 오후 8시에 send_notification 함수를 실행하도록 스케줄을 설정합니다.
schedule.every().day.at("20:00").do(send_notification)

while True:
    schedule.run_pending()
    time.sleep(1)