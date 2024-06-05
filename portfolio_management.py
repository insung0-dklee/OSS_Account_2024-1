import json

class Investment:
    def __init__(self, name, amount, purchase_price):
        self.name = name
        self.amount = amount
        self.purchase_price = purchase_price
        self.current_price = purchase_price

    def update_price(self, current_price):
        self.current_price = current_price

    def get_value(self):
        return self.amount * self.current_price

    def get_profit_loss(self):
        return (self.current_price - self.purchase_price) * self.amount

class Portfolio:
    def __init__(self):
        self.investments = []

    def add_investment(self, name, amount, purchase_price):
        investment = Investment(name, amount, purchase_price)
        self.investments.append(investment)
        print(f"Investment in {name} added.")

    def update_investment(self, name, current_price):
        for investment in self.investments:
            if investment.name == name:
                investment.update_price(current_price)
                print(f"Updated current price of {name}.")
                return
        print(f"Investment {name} not found.")

    def view_portfolio(self):
        if not self.investments:
            print("No investments found.")
            return
        print("Portfolio:")
        for investment in self.investments:
            print(f"{investment.name} - Amount: {investment.amount}, Purchase Price: {investment.purchase_price}, Current Price: {investment.current_price}, Value: {investment.get_value()}, Profit/Loss: {investment.get_profit_loss()}")

    def get_total_value(self):
        return sum(investment.get_value() for investment in self.investments)

    def get_total_profit_loss(self):
        return sum(investment.get_profit_loss() for investment in self.investments)

def save_portfolio(portfolio):
    data = [
        {
            "name": inv.name,
            "amount": inv.amount,
            "purchase_price": inv.purchase_price,
            "current_price": inv.current_price
        }
        for inv in portfolio.investments
    ]
    with open('portfolio.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    print("Portfolio saved.")

def load_portfolio():
    portfolio = Portfolio()
    try:
        with open('portfolio.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            for item in data:
                portfolio.add_investment(item['name'], item['amount'], item['purchase_price'])
                portfolio.update_investment(item['name'], item['current_price'])
        print("Portfolio loaded.")
    except FileNotFoundError:
        print("No saved portfolio found.")
    return portfolio

def portfolio_management():
    portfolio = load_portfolio()
    while True:
        print("\n--- Portfolio Management ---")
        print("1: Add Investment")
        print("2: Update Investment Price")
        print("3: View Portfolio")
        print("4: Save Portfolio")
        print("0: Exit")

        choice = input("Select an option: ")
        if choice == "1":
            name = input("Investment Name: ")
            amount = float(input("Amount: "))
            purchase_price = float(input("Purchase Price: "))
            portfolio.add_investment(name, amount, purchase_price)
        elif choice == "2":
            name = input("Investment Name: ")
            current_price = float(input("Current Price: "))
            portfolio.update_investment(name, current_price)
        elif choice == "3":
            portfolio.view_portfolio()
        elif choice == "4":
            save_portfolio(portfolio)
        elif choice == "0":
            break
        else:
            print("Invalid option, please try again.")
