import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar
import sqlite3

# 데이터베이스 설정
conn = sqlite3.connect('finance.db')
c = conn.cursor()

# 테이블 생성
c.execute('''
    CREATE TABLE IF NOT EXISTS goals (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        amount REAL,
        description TEXT
    )
''')
conn.commit()

class FinanceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("가계부")

        # 달력 생성
        self.calendar = Calendar(root, selectmode='day', year=2024, month=6, day=4)
        self.calendar.pack(pady=20)

        # 목표 추가 버튼
        self.add_goal_button = ttk.Button(root, text="목표 추가", command=self.add_goal)
        self.add_goal_button.pack(pady=10)

        # 목표 보기 버튼
        self.view_goals_button = ttk.Button(root, text="목표 보기", command=self.view_goals)
        self.view_goals_button.pack(pady=10)

    def add_goal(self):
        self.new_window = tk.Toplevel(self.root)
        self.new_window.title("목표 추가")

        tk.Label(self.new_window, text="금액:").pack(pady=5)
        self.amount_entry = tk.Entry(self.new_window)
        self.amount_entry.pack(pady=5)

        tk.Label(self.new_window, text="설명:").pack(pady=5)
        self.description_entry = tk.Entry(self.new_window)
        self.description_entry.pack(pady=5)

        save_button = ttk.Button(self.new_window, text="저장", command=self.save_goal)
        save_button.pack(pady=10)

    def save_goal(self):
        date = self.calendar.get_date()
        amount = self.amount_entry.get()
        description = self.description_entry.get()

        c.execute("INSERT INTO goals (date, amount, description) VALUES (?, ?, ?)", (date, amount, description))
        conn.commit()
        self.new_window.destroy()

    def view_goals(self):
        self.view_window = tk.Toplevel(self.root)
        self.view_window.title("목표 보기")

        date = self.calendar.get_date()
        goals = c.execute("SELECT amount, description FROM goals WHERE date = ?", (date,)).fetchall()

        for goal in goals:
            tk.Label(self.view_window, text=f"금액: {goal[0]}, 설명: {goal[1]}").pack(pady=5)

# 메인 실행
root = tk.Tk()
app = FinanceApp(root)
root.mainloop()
