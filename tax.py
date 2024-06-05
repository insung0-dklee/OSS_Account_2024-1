def calculate_tax(income):
    if income <= 14000000:
        return income * 0.06
    elif income <= 50000000:
        return 14000000 * 0.06 + (income - 14000000) * 0.15
    elif income <= 88000000:
        return 14000000 * 0.06 + 36000000 * 0.15 + (income - 50000000) * 0.24
    elif income <= 150000000:
        return 14000000 * 0.06 + 36000000 * 0.15 + 38000000 * 0.24 + (income - 88000000) * 0.35
    elif income <= 300000000:
        return 14000000 * 0.06 + 36000000 * 0.15 + 38000000 * 0.24 + 62000000 * 0.35 + (income - 150000000) * 0.38
    elif income <= 500000000:
        return 14000000 * 0.06 + 36000000 * 0.15 + 38000000 * 0.24 + 62000000 * 0.35 + 150000000 * 0.38 + (income - 300000000) * 0.40
    elif income <= 1000000000:
        return 14000000 * 0.06 + 36000000 * 0.15 + 38000000 * 0.24 + 62000000 * 0.35 + 150000000 * 0.38 + 200000000 * 0.40 + (income - 500000000) * 0.42
    else:
        return 14000000 * 0.06 + 36000000 * 0.15 + 38000000 * 0.24 + 62000000 * 0.35 + 150000000 * 0.38 + 200000000 * 0.40 + 500000000 * 0.42 + (income - 1000000000) * 0.45

def calculate_comprehensive_income_tax():
    business_income = float(input("사업소득을 입력하세요 (원): "))
    earned_income = float(input("근로소득을 입력하세요 (원): "))
    interest_income = float(input("이자소득을 입력하세요 (원): "))
    dividend_income = float(input("배당소득을 입력하세요 (원): "))
    pension_income = float(input("연금소득을 입력하세요 (원): "))
    other_income = float(input("기타소득을 입력하세요 (원): "))

    total_income = business_income + earned_income + interest_income + dividend_income + pension_income + other_income

    earned_income_deduction = calculate_earned_income_deduction(earned_income)
    taxable_income = total_income - earned_income_deduction
    pre_tax = calculate_tax(taxable_income)
    after_tax = pre_tax - calculate_tax_deductions(pre_tax)

    print(f"총 소득: {total_income} 원")
    print(f"근로소득공제: {earned_income_deduction} 원")
    print(f"과세 표준: {taxable_income} 원")
    print(f"세금 공제 전: {pre_tax} 원")
    print(f"세금 공제 후: {after_tax} 원")

def calculate_earned_income_deduction(earned_income):
    if earned_income <= 5000000:
        return earned_income * 0.7
    elif earned_income <= 15000000:
        return 3500000 + (earned_income - 5000000) * 0.4
    elif earned_income <= 45000000:
        return 7500000 + (earned_income - 15000000) * 0.15
    elif earned_income <= 100000000:
        return 12000000 + (earned_income - 45000000) * 0.05
    else:
        return 14750000 + (earned_income - 100000000) * 0.02

def calculate_tax_deductions(pre_tax):
    return pre_tax * 0.07

def calculate_wage_income_tax():
    total_income = float(input("총 소득을 입력하세요 (원): "))
    earned_income_deduction = calculate_earned_income_deduction(total_income)
    taxable_income = total_income - earned_income_deduction
    pre_tax = calculate_tax(taxable_income)
    after_tax = pre_tax - calculate_tax_deductions(pre_tax)

    print(f"총 소득: {total_income} 원")
    print(f"근로소득공제: {earned_income_deduction} 원")
    print(f"과세 표준: {taxable_income} 원")
    print(f"세금 공제 전: {pre_tax} 원")
    print(f"세금 공제 후: {after_tax} 원")

def calculate_vat():
    price_with_vat = float(input("부가가치세가 포함된 물품의 가격을 입력하세요 (원): "))
    vat = price_with_vat * 0.1
    price_without_vat = price_with_vat / 1.1

    print(f"물품 가격 (부가가치세 포함): {price_with_vat} 원")
    print(f"물품 가격 (부가가치세 제외): {price_without_vat:.2f} 원")
    print(f"부가가치세: {vat:.2f} 원")

def calculate_insurance():
    total_income = float(input("총 소득을 입력하세요 (원): "))
    health_insurance = total_income * 0.03495
    long_term_care = health_insurance * 0.1227
    national_pension = total_income * 0.045
    employment_insurance = total_income * 0.008

    total_deductions = health_insurance + long_term_care + national_pension + employment_insurance
    after_deductions = total_income - total_deductions

    print(f"총 소득: {total_income} 원")
    print(f"건강보험료: {health_insurance:.2f} 원")
    print(f"노인장기요양보험료: {long_term_care:.2f} 원")
    print(f"국민연금: {national_pension:.2f} 원")
    print(f"고용보험료: {employment_insurance:.2f} 원")
    print(f"총 공제액: {total_deductions:.2f} 원")
    print(f"공제 후 금액: {after_deductions:.2f} 원")

def year_end_settlement_simulation():
    print("연말정산 시뮬레이션 기능입니다.")
    total_income = float(input("총 소득을 입력하세요 (원): "))
    health_insurance = total_income * 0.03495
    long_term_care = health_insurance * 0.1227
    national_pension = total_income * 0.045
    employment_insurance = total_income * 0.008
    insurance_deductions = health_insurance + long_term_care + national_pension + employment_insurance
    income_after_deductions = total_income - insurance_deductions

    standard_deduction = 1500000
    special_deduction = 0.12 * income_after_deductions
    total_deductions = standard_deduction + special_deduction
    taxable_income = income_after_deductions - total_deductions

    pre_tax = calculate_tax(taxable_income)
    tax_deductions = calculate_tax_deductions(pre_tax)
    after_tax = pre_tax - tax_deductions

    print(f"총 소득: {total_income} 원")
    print(f"건강보험료: {health_insurance:.2f} 원")
    print(f"노인장기요양보험료: {long_term_care:.2f} 원")
    print(f"국민연금: {national_pension:.2f} 원")
    print(f"고용보험료: {employment_insurance:.2f} 원")
    print(f"총 보험 공제액: {insurance_deductions:.2f} 원")
    print(f"보험 공제 후 소득: {income_after_deductions:.2f} 원")
    print(f"기본공제: {standard_deduction} 원")
    print(f"특별공제: {special_deduction:.2f} 원")
    print(f"총 공제액: {total_deductions:.2f} 원")
    print(f"과세 표준: {taxable_income:.2f} 원")
    print(f"세금 공제 전: {pre_tax:.2f} 원")
    print(f"세금 공제 후: {after_tax:.2f} 원")

def calculate_inheritance_tax():
    print("상속세 계산 기능입니다.")
    total_inheritance = float(input("총 상속 재산을 입력하세요 (원): "))
    if total_inheritance <= 100000000:
        tax_rate = 0.1
        deduction = 0
    elif total_inheritance <= 500000000:
        tax_rate = 0.2
        deduction = 10000000
    elif total_inheritance <= 1000000000:
        tax_rate = 0.3
        deduction = 60000000
    elif total_inheritance <= 3000000000:
        tax_rate = 0.4
        deduction = 160000000
    else:
        tax_rate = 0.5
        deduction = 460000000

    inheritance_tax = total_inheritance * tax_rate - deduction

    print(f"총 상속 재산: {total_inheritance} 원")
    print(f"상속세율: {tax_rate * 100}%")
    print(f"상속세 공제액: {deduction} 원")
    print(f"상속세: {inheritance_tax:.2f} 원")

def calculate_gift_tax():
    print("증여세 계산 기능입니다.")
    total_gift = float(input("총 증여 재산을 입력하세요 (원): "))
    if total_gift <= 100000000:
        tax_rate = 0.1
        deduction = 0
    elif total_gift <= 500000000:
        tax_rate = 0.2
        deduction = 10000000
    elif total_gift <= 1000000000:
        tax_rate = 0.3
        deduction = 60000000
    elif total_gift <= 3000000000:
        tax_rate = 0.4
        deduction = 160000000
    else:
        tax_rate = 0.5
        deduction = 460000000

    gift_tax = total_gift * tax_rate - deduction

    print(f"총 증여 재산: {total_gift} 원")
    print(f"증여세율: {tax_rate * 100}%")
    print(f"증여세 공제액: {deduction} 원")
    print(f"증여세: {gift_tax:.2f} 원")

def calculate_real_estate_transfer_tax():
    print("부동산 양도소득세 계산 기능입니다.")
    purchase_price = float(input("취득가액을 입력하세요 (원): "))
    selling_price = float(input("양도가액을 입력하세요 (원): "))
    other_costs = float(input("기타 비용을 입력하세요 (원): "))
    holding_period = int(input("보유 기간을 입력하세요 (년): "))

    capital_gain = selling_price - purchase_price - other_costs

    if holding_period <= 1:
        tax_rate = 0.5
    elif holding_period <= 2:
        tax_rate = 0.4
    else:
        if capital_gain <= 12000000:
            tax_rate = 0.06
        elif capital_gain <= 46000000:
            tax_rate = 0.15
        elif capital_gain <= 88000000:
            tax_rate = 0.24
        elif capital_gain <= 150000000:
            tax_rate = 0.35
        elif capital_gain <= 300000000:
            tax_rate = 0.38
        elif capital_gain <= 500000000:
            tax_rate = 0.40
        elif capital_gain <= 1000000000:
            tax_rate = 0.42
        else:
            tax_rate = 0.45

    transfer_tax = capital_gain * tax_rate

    print(f"취득가액: {purchase_price} 원")
    print(f"양도가액: {selling_price} 원")
    print(f"기타 비용: {other_costs} 원")
    print(f"양도차익: {capital_gain} 원")
    print(f"보유 기간: {holding_period} 년")
    print(f"양도소득세율: {tax_rate * 100}%")
    print(f"양도소득세: {transfer_tax:.2f} 원")

def calculate_local_income_tax():
    print("지방소득세 계산 기능입니다.")
    total_income = float(input("총 소득을 입력하세요 (원): "))
    local_income_tax_rate = 0.1  # 지방소득세율 10%

    local_income_tax = total_income * local_income_tax_rate

    print(f"총 소득: {total_income} 원")
    print(f"지방소득세율: {local_income_tax_rate * 100}%")
    print(f"지방소득세: {local_income_tax:.2f} 원")

def calculate_retirement_income_tax():
    print("퇴직소득세 계산 기능입니다.")
    total_income = float(input("총 퇴직 소득을 입력하세요 (원): "))
    years_of_service = int(input("근속 연수를 입력하세요 (년): "))

    average_income_per_year = total_income / years_of_service

    if average_income_per_year <= 8000000:
        tax_rate = 0.06
    elif average_income_per_year <= 70000000:
        tax_rate = 0.15
    elif average_income_per_year <= 140000000:
        tax_rate = 0.24
    elif average_income_per_year <= 280000000:
        tax_rate = 0.35
    elif average_income_per_year <= 420000000:
        tax_rate = 0.38
    elif average_income_per_year <= 700000000:
        tax_rate = 0.40
    elif average_income_per_year <= 1400000000:
        tax_rate = 0.42
    else:
        tax_rate = 0.45

    retirement_income_tax = total_income * tax_rate

    print(f"총 퇴직 소득: {total_income} 원")
    print(f"근속 연수: {years_of_service} 년")
    print(f"연평균 소득: {average_income_per_year} 원")
    print(f"퇴직소득세율: {tax_rate * 100}%")
    print(f"퇴직소득세: {retirement_income_tax:.2f} 원")


def tax_menu():
    while True:
        tax_func = input("세금 및 보험 계산 항목을 선택하세요:\n1: 종합소득세 계산\n2: 근로소득세 계산\n3: 부가가치세 계산\n4: 4대 보험 계산\n5: 연말정산 시뮬레이션\n6: 상속세 계산\n7: 증여세 계산\n8: 부동산 양도소득세 계산\n9: 지방소득세 계산\n10: 퇴직소득세 계산\n0: 돌아가기\n선택: ")
        if tax_func == "1":
            calculate_comprehensive_income_tax()
        elif tax_func == "2":
            calculate_wage_income_tax()
        elif tax_func == "3":
            calculate_vat()
        elif tax_func == "4":
            calculate_insurance()
        elif tax_func == "5":
            year_end_settlement_simulation()
        elif tax_func == "6":
            calculate_inheritance_tax()
        elif tax_func == "7":
            calculate_gift_tax()
        elif tax_func == "8":
            calculate_real_estate_transfer_tax()
        elif tax_func == "9":
            calculate_local_income_tax()
        elif tax_func == "10":
            calculate_retirement_income_tax()
        elif tax_func == "0":
            break
        else:
            print("올바른 선택이 아닙니다.")

