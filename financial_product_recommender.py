class FinancialProduct:
    def __init__(self, name, interest_rate, fee, risk_level):
        self.name = name
        self.interest_rate = interest_rate
        self.fee = fee
        self.risk_level = risk_level

def recommend_financial_product(products):
    best_product = None
    best_interest_rate = 0
    lowest_fee = float('inf')
    lowest_risk = float('inf')

    for product in products:
        if product.interest_rate > best_interest_rate and product.fee < lowest_fee and product.risk_level < lowest_risk:
            best_product = product
            best_interest_rate = product.interest_rate
            lowest_fee = product.fee
            lowest_risk = product.risk_level

    return best_product

def input_financial_products():
    products = []
    while True:
        name = input("금융 상품의 이름을 입력하세요: ")
        interest_rate = float(input(f"{name}의 이자율을 입력하세요 (%): "))
        fee = float(input(f"{name}의 수수료를 입력하세요 (원): "))
        risk_level = float(input(f"{name}의 리스크 레벨을 입력하세요 (1-10): "))
        products.append(FinancialProduct(name, interest_rate, fee, risk_level))

        more_products = input("더 입력하시겠습니까? (Y/N): ")
        if more_products.lower() != 'y':
            break

    return products

def main():
    print("금융 상품 추천 시스템을 시작합니다.")
    products = input_financial_products()
    best_product = recommend_financial_product(products)

    if best_product:
        print(f"추천하는 금융 상품: {best_product.name}")
        print(f"이자율: {best_product.interest_rate}%, 수수료: {best_product.fee}원, 리스크 레벨: {best_product.risk_level}")
    else:
        print("추천할 금융 상품이 없습니다.")
