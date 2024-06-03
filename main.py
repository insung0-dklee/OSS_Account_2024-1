import csv
from datetime import datetime

# 로그 파일 경로 설정
LOG_FILE = 'activity_log.csv'

def log_activity(user_id, activity_type, details):
    """
    사용자 활동을 로그 파일에 기록합니다.
    
    Args:
        user_id (str): 사용자 ID
        activity_type (str): 활동 유형 (예: "로그인", "지출 추가", "지출 삭제" 등)
        details (str): 활동에 대한 상세 정보
    """
    # 로그 파일을 append 모드로 열어 기록
    with open(LOG_FILE, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # 현재 시간, 사용자 ID, 활동 유형, 상세 정보를 로그에 기록
        writer.writerow([datetime.now().strftime('%Y-%m-%d %H:%M:%S'), user_id, activity_type, details])

def view_logs(user_id=None, activity_type=None):
    """
    로그 파일에서 활동 기록을 조회합니다.
    
    Args:
        user_id (str, optional): 특정 사용자의 활동만 조회하려면 사용자 ID를 지정
        activity_type (str, optional): 특정 활동 유형만 조회하려면 활동 유형을 지정
    
    Returns:
        list: 조회된 로그 기록 리스트
    """
    logs = []
    # 로그 파일을 읽기 모드로 열기
    with open(LOG_FILE, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        # 각 로그 기록을 읽어 조건에 맞는지 확인 후 리스트에 추가
        for row in reader:
            log_time, log_user_id, log_activity_type, log_details = row
            if (user_id is None or log_user_id == user_id) and (activity_type is None or log_activity_type == activity_type):
                logs.append(row)
    return logs

# 로그 기록 예시
log_activity('user123', '로그인', '사용자 로그인 성공')  # 'user123' 사용자가 로그인 성공
log_activity('user123', '지출 추가', '지출 내역: 커피 4000원')  # 'user123' 사용자가 커피 지출 추가

# 로그 조회 예시
logs = view_logs('user123', '로그인')  # 'user123' 사용자의 로그인 활동 조회
for log in logs:
    print(log)
