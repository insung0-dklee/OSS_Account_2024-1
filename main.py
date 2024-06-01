import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'Malgun Gothic'


# 예시 데이터
categories = ['식비', '주거', '교통', '의료', '문화생활']
expenses = [100, 200, 150, 80, 120]  # 각 카테고리별 지출

# 그래프 생성
plt.figure(figsize=(8, 6))
plt.bar(categories, expenses, color='skyblue')

# 그래프 제목 및 축 라벨 설정
plt.title('월별 지출 현황')
plt.xlabel('카테고리')
plt.ylabel('지출 금액')

# 그래프에 숫자 표시
for i, expense in enumerate(expenses):
    plt.text(i, expense + 5, str(expense), ha='center')

# 그래프 출력
plt.tight_layout()
plt.show()
