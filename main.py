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

    def delete_entry(self, index):
        """
        Deletes an entry from the budget by index.
        
        Params:
        index (int): The index of the entry to be deleted.
        
        Return:
        None
        """
        if 0 <= index < len(self.budget):
            del self.budget[index]
        else:
            print("Invalid index. Please try again.")

    def modify_entry(self, index, amount=None, category=None, description=None):
        """
        Modifies an existing entry in the budget.
        
        Params:
        index (int)           : The index of the entry to be modified.
        amount (float)        : The new amount of income (positive) or expense (negative) (optional).
        category (str)        : The new category of the entry (optional).
        description (str)     : The new description of the entry (optional).
        
        Return:
        None
        """
        if 0 <= index < len(self.budget):
            if amount is not None:
                self.budget[index]["amount"] = amount
            if category is not None:
                self.budget[index]["category"] = category
            if description is not None:
                self.budget[index]["description"] = description
        else:
            print("Invalid index. Please try again.")

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
        for idx, entry in enumerate(self.budget):
            print(f"{idx}: {entry['date']} - {entry['category']}: {entry['amount']} ({entry['description']})")

    def get_entries_by_category(self, category):
        """
        Retrieves all entries of a specific category.
        
        Params:
        category (str) : The category to filter entries by.
        
        Return:
        list: A list of entries that match the given category.
        """
        return [entry for entry in self.budget if entry['category'] == category]

    def summary_by_category(self):
        """
        Displays a summary of expenses and income by category.
        
        Return:
        None
        """
        summary = {}
        for entry in self.budget:
            category = entry['category']
            amount = entry['amount']
            if category in summary:
                summary[category] += amount
            else:
                summary[category] = amount
        
        for category, total in summary.items():
            print(f"{category}: {total}")

    def display_entries_by_date_range(self, start_date, end_date):
        """
        Displays all entries within a specific date range.
        
        Params:
        start_date (datetime) : The start date of the range.
        end_date (datetime)   : The end date of the range.
        
        Return:
        None
        """
        for entry in self.budget:
            if start_date <= entry["date"] <= end_date:
                print(f"{entry['date']} - {entry['category']}: {entry['amount']} ({entry['description']})")

def main():
    """
    Main function to run the budget management program. Provides a loop to interact with the user and perform different functions.
    
    Return:
    None
    """
    budget = HouseholdBudget()
    b_is_exit = False

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
        elif func == "4":
            # Delete an entry
            index = int(input("삭제할 항목의 인덱스를 입력하세요: "))
            budget.delete_entry(index)
            print("항목이 삭제되었습니다.")
        elif func == "5":
            # Modify an entry
            index = int(input("수정할 항목의 인덱스를 입력하세요: "))
            amount = input("새 금액 입력 (입력하지 않으려면 빈칸으로 두세요): ")
            category = input("새 카테고리 입력 (입력하지 않으려면 빈칸으로 두세요): ")
            description = input("새 설명 입력 (입력하지 않으려면 빈칸으로 두세요): ")
            budget.modify_entry(index, float(amount) if amount else None, category if category else None, description if description else None)
            print("항목이 수정되었습니다.")
        elif func == "6":
            # Display summary by category
            budget.summary_by_category()
        elif func == "7":
            # Display entries by date range
            start_date_str = input("시작 날짜를 입력하세요 (YYYY-MM-DD): ")
            end_date_str = input("끝 날짜를 입력하세요 (YYYY-MM-DD): ")
            start_date = datetime.datetime.strptime(start_date_str, "%Y-%m-%d")
            end_date = datetime.datetime.strptime(end_date_str, "%Y-%m-%d")
            budget.display_entries_by_date_range(start_date, end_date)
        elif func == "?":
            # Display help
            print("도움말:")
            print("1: 항목 추가")
            print("2: 현재 잔액 보기")
            print("3: 모든 항목 보기")
            print("4: 항목 삭제")
            print("5: 항목 수정")
            print("6: 카테고리별 요약 보기")
            print("7: 날짜 범위별 항목 보기")
            print("종료하려면 다른 키를 누르세요.")
        else:
            b_is_exit = True

if __name__ == "__main__":
    main()
