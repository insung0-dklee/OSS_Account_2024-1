import hashlib #hashlib 사용
import matplotlib.pyplot as plt
import pandas as pd
import datetime

"""
add_record  :  adds the amount, type, and date of sale of the items sold.

show_record  :  shows the records that have been added

show_summary  :  Graphs the saved records.
"""

class AccountBook:
    def __init__(self):
        self.records = []

    def add_record(self, date, category, amount):
        record = {
            "date": datetime.datetime.strptime(date, '%Y-%m-%d'),
            "category": category,
            "amount": amount,
        }
        self.records.append(record)
        print("Record added successfully.")

    def show_records(self):
        if not self.records:
            print("No records")
            return
        for record in self.records:
            print(f"Date: {record['date'].strftime('%Y-%m-%d')}, Category: {record['category']}, Amount: {record['amount']}")

    def show_summary(self):
        if not self.records:
            print("No records")
            return

        df = pd.DataFrame(self.records)
        df['month'] = df['date'].dt.to_period('M')
        summary = df.groupby('month')['amount'].sum()
        
        print("\nSummary by Month:")
        print(summary)
        
        summary.plot(kind='bar')
        plt.title("Monthly Income/Expenses Summary")
        plt.xlabel("Month")
        plt.ylabel("Total Amount")
        plt.show()

def main():
    account_book = AccountBook()
    
    while True:
        print("\n1. Add Record")
        print("\n2. Show Records")
        print("\n3. Show Summary")
        print("\n4. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            date = input("Enter date (YYYY-MM-DD): ")
            category = input("Enter category: ")
            amount = float(input("Enter amount: "))
            account_book.add_record(date, category, amount)
        
        elif choice == '2':
            account_book.show_records()
        
        elif choice == '3':
            account_book.show_summary()
        
        elif choice == '4':
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

userdata = {} #아이디, 비밀번호 저장해둘 딕셔너리

def user_reg() : #회원가입
    id = input("id 입력: " ) #회원가입 시의 id 입력

    pw = input("password 입력: ") #회원가입 시의 pw 입력

    h = hashlib.sha256() #hashlib 모듈의 sha256 사용
    h.update(pw.encode()) #sha256으로 암호화
    pw_data = h.hexdigest() #16진수로 변환

    f = open('login.txt', 'wb') #login 파일 오픈

    userdata[id] = pw_data #key에 id값을, value에 비밀번호 값

    with open('login.txt', 'a', encoding='UTF-8') as fw: #utf-8 변환 후 login.txt에 작성
        for user_id, user_pw in userdata.items(): #딕셔너리 내에 있는 값을 모두 for문
            fw.write(f'{user_id} : {user_pw}\n') #key, value값을 차례로 login.txt파일에 저장

b_is_exit = 0

while not b_is_exit:
    func = input("기능 입력 (? 입력시 도움말) : ")

    if func == "1":

        break

    elif func == "2":

        break

    elif func == "3":

        break

    elif func == "?":
        print("도움말 입력.")

        break

    else:
        b_is_exit = not b_is_exit

