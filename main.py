import tkinter as tk
from tkinter import ttk
import Account_book
import os

logged_in_user = None

def main():
    global logged_in_user, root, frame

    if os.path.exists('login.txt'):
        with open('login.txt', 'r', encoding='UTF-8') as fr:
            for line in fr:
                id, pw, name, phone = line.strip().split(' : ')
                Account_book.userdata[id] = pw
                Account_book.usernames[name] = id
                Account_book.userphones[phone] = id
                Account_book.userdata2[id] = {'pw': pw, 'name': name, 'phone': phone}

    root = tk.Tk()
    root.title("가계부 프로그램")
    root.geometry("400x800")
    root.resizable(False, False)

    style = ttk.Style()
    style.configure('TButton', font=('Helvetica', 12), padding=10)
    style.configure('TLabel', font=('Helvetica', 14), padding=10)

    frame = ttk.Frame(root, padding=20)
    frame.pack(fill='both', expand=True)

    update_ui()

    root.mainloop()

def update_ui():
    global budget_label

    for widget in frame.winfo_children():
        widget.destroy()

    ttk.Label(frame, text="가계부 프로그램").pack(pady=10)
    
    budget_label = ttk.Label(frame, text="")
    budget_label.pack(pady=5)

    if logged_in_user is None:
        ttk.Button(frame, text="회원가입", command=Account_book.user_reg_include_name_phone).pack(pady=5)
        ttk.Button(frame, text="로그인", command=login).pack(pady=5)
        ttk.Button(frame, text="아이디 찾기", command=Account_book.find_id_by_phone).pack(pady=5)
    else:
        ttk.Button(frame, text="지출 내역 입력", command=lambda: Account_book.input_expense(budget_label)).pack(pady=5)
        ttk.Button(frame, text="지출 내역 조회", command=Account_book.view_expenses).pack(pady=5)
        ttk.Button(frame, text="지출 내역 삭제", command=lambda: Account_book.delete_expense(budget_label)).pack(pady=5)
        ttk.Button(frame, text="계산기", command=Account_book.calculator).pack(pady=5)
        ttk.Button(frame, text="메모장 생성", command=Account_book.add_memo).pack(pady=5)
        ttk.Button(frame, text="메모장 조회", command=Account_book.view_memos).pack(pady=5)
        ttk.Button(frame, text="월별 보고서 생성", command=Account_book.generate_monthly_report).pack(pady=5)
        ttk.Button(frame, text="예산 설정", command=lambda: Account_book.set_budget(budget_label)).pack(pady=5)
        ttk.Button(frame, text="카테고리 분석", command=Account_book.analyze_categories).pack(pady=5)
        ttk.Button(frame, text="회원 정보 수정", command=Account_book.modify_user_info).pack(pady=5)
        ttk.Button(frame, text="로그아웃", command=logout).pack(pady=5)
    
    if logged_in_user:
        Account_book.update_budget_display(budget_label)

def login():
    global logged_in_user
    Account_book.user_login(budget_label)
    if Account_book.logged_in_user:
        logged_in_user = Account_book.logged_in_user
        update_ui()

def logout():
    global logged_in_user
    logged_in_user = None
    Account_book.logged_in_user = None
    update_ui()

if __name__ == "__main__":
    main()
