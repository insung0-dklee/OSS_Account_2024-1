import datetime

class HouseholdBudget:
    """
    A simple class to manage household budget entries.
    
    Attributes:
    budget (list): A list to store all the entries of income and expenses.
    """
    
    def __init__(self):
        """
        Initializes an empty budget list.
        """
        self.budget = []

    def add_entry(self, amount, category, description=""):
        """
        Adds a new entry to the budget.
        
        Params:
        amount (float)        : The amount of income (positive) or expense (negative).
        category (str)        : The category of the entry (e.g., 'food', 'rent', 'salary').
        description (str)     : A short description of the entry (optional).
        
        Return:
        None
        """
        entry = {
            "date": datetime.datetime.now(),
            "amount": amount,
            "category": category,
            "description": description
        }
        self.budget.append(entry)

    def get_balance(self):
        """
        Calculates and returns the current balance.
        
        Return:
        float: The current balance which is the sum of all amounts in the budget.
        """
        return sum(entry['amount'] for entry in self.budget)

    def display_entries(self):
        """
        Prints all entries in the budget in a readable format.
        
        Return:
        None
        """
        for entry in self.budget:
            print(f"{entry['date']} - {entry['category']}: {entry['amount']} ({entry['description']})")

    def get_entries_by_category(self, category):
        """
        Retrieves all entries of a specific category.
        
        Params:
        category (str) : The category to filter entries by.
        
        Return:
        list: A list of entries that match the given category.
        """
        return [entry for entry in self.budget if entry['category'] == category]

def main():
    """
    Main function to run the budget management program. Provides a loop to interact with the user and perform different functions.
    
    Return:
    None
    """
    budget = HouseholdBudget()
    b_is_exit = 0

    while not b_is_exit:
        func = input("기능 입력 (? 입력시 도움말) : ")

        if func == "1":
            # Add a new entry
            amount = float(input("금액 입력: "))
            category = input("카테고리 입력: ")
            description = input("설명 입력 (선택): ")
            budget.add_entry(amount, category, description)
            print("항목이 추가되었습니다.")
        elif func == "2":
            # Display current balance
            print("Current Balance:", budget.get_balance())
        elif func == "3":
            # Display all entries
            budget.display_entries()
        elif func == "?":
            # Display help
            print("도움말:")
            print("1: 항목 추가")
            print("2: 현재 잔액 보기")
            print("3: 모든 항목 보기")
            print("종료하려면 다른 키를 누르세요.")
        else:
            b_is_exit = 1

if __name__ == "__main__":
    main()
