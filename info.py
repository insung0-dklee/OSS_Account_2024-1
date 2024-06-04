#기능추가 경제신문 사이트 방문기능 
"""
 sites에 여러 경제신문 사이트 URL과 방문 횟수를 저장합니다.
 읽고 싶은 신문 번호를 누르면 바로 그 사이트로 연결되어 신문을 볼 수 있습니다.
display_sites 함수는 방문 횟수에 따라 사이트 목록을 정렬하여 출력합니다.
"""
import webbrowser

# 경제신문 사이트 목록
sites = {
    '1': {
        'name': '한국경제',
        'url': 'https://www.hankyung.com',
        'visits': 0
    },
    '2': {
        'name': '매일경제',
        'url': 'https://www.mk.co.kr',
        'visits': 0
    },
    '3': {
        'name': '서울경제',
        'url': 'https://www.sedaily.com',
        'visits': 0
    },
    '4': {
        'name': '연합뉴스',
        'url': 'https://www.yna.co.kr',
        'visits': 0
    },
    '5': {
        'name': '파이낸셜뉴스',
        'url': 'https://www.fnnews.com',
        'visits': 0
    }
}

#위의 경제신문 사이트를 보여주는 함수
def display_sites():
  sorted_sites = sorted(sites.items(), key=lambda item: -item[1]['visits'])
  print("경제신문 목록:")
  for key, site in sorted_sites:
    print(f"{key}. {site['name']} (방문 횟수: {site['visits']})")
  print("6. 종료")

#원하는 사이트의 번호를 사용자가 선택하면, 사이트로 바로 연결되어 열람가능
#방문횟수가 기록됨
def open_site(choice):
  if choice in sites:
    site = sites[choice]
    webbrowser.open(site['url'])
    site['visits'] += 1
  else:
    print("잘못된 선택입니다.")


def main():
  while True:
    display_sites()
    choice = input("읽고 싶은 신문 번호를 입력하세요: ")
    if choice == '6':
      break
    open_site(choice)


if __name__ == "__main__":
  main()