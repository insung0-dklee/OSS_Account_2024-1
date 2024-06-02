"""
소득 금액에 따른 근로소득세 계산 프로그램
소득 금액마다 근로소득세의 세율이 다르기에
소득 금액을 입력하면 소득 범위에 따른 세율을 적용하여 근로소득세를 계산해주는 프로그
단, 근로소득세는 소수점 둘째 자리까지 출력된다.
"""
def calculate_income_tax(income):
    if income <= 12000000:
        tax_rate = 6
    elif income <= 46000000:
        tax_rate = 15
    elif income <= 88000000:
        tax_rate = 24
    elif income <= 150000000:
        tax_rate = 35
    elif income <= 300000000:
        tax_rate = 38
    elif income <= 500000000:
        tax_rate = 40
    elif income <= 1000000000:
        tax_rate = 42
    else:
        tax_rate = 45
    
    tax_amount = income * tax_rate / 100
    return tax_amount, tax_rate

def main():
    print("근로소득세 계산 프로그램(숫자만 입력 가능)")
    
    income = float(input("총 근로소득 금액을 입력하세요 (원): "))
    
    tax_amount, tax_rate = calculate_income_tax(income)
    
    print(f"총 근로소득 금액: {income:.0f}원")
    print(f"근로소득세: {tax_amount:.2f}원 (세율: {tax_rate}%)")

if __name__ == "__main__":
    main()
