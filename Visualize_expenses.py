import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from datetime import datetime
import numpy as np

class Expense:
    def __init__(self, month, year, amount):
        self.month = month
        self.year = year
        self.amount = amount

def create_expense(month, year, amount):
    return Expense(month, year, amount)

def visualize_expenses():
    global expenses
    global canvas  # canvas 변수를 전역 변수로 선언
    selected_period = period_combobox.get()
    if selected_period == "월간":
        visualize_monthly_expenses(expenses)
    elif selected_period == "년간":
        visualize_yearly_expenses(expenses)
        

def visualize_monthly_expenses(expenses):
    global canvas  # canvas 변수를 전역 변수로 선언
    selected_year = int(year_combobox.get())

    # 선택한 연도에 해당하는 지출만 필터링
    filtered_expenses = [expense for expense in expenses if expense.year == selected_year]

    # 월 지출 계산
    monthly_amounts = [0] * 12
    for expense in filtered_expenses:
        monthly_amounts[expense.month - 1] += expense.amount

    fig = Figure(figsize=(10, 6))  # 그래프의 크기를 조정
    ax = fig.add_subplot(111)
    ax.bar([str(i+1) for i in range(12)], monthly_amounts)
    ax.set_xlabel('Month')
    ax.set_ylabel('Amount')
    ax.set_title(f'{selected_year}monthly expenditure')

    # 월 평균 계산
    monthly_average = np.mean(monthly_amounts)
    ax.text(0.5, 0.98, f'monthly average: {monthly_average:.2f}', horizontalalignment='center', verticalalignment='center', transform=ax.transAxes)

    ax.set_xlim(0, 12)  # 가로축 범위를 1부터 12까지로 지정

    if canvas:  # 기존의 canvas가 존재하는 경우에만 destroy
        canvas.get_tk_widget().destroy()

    canvas = FigureCanvasTkAgg(fig, master=app)
    canvas.draw()
    canvas.get_tk_widget().grid(row=5, columnspan=2)

def visualize_yearly_expenses(expenses):
    global canvas  # canvas 변수를 전역 변수로 선언
    fig = Figure(figsize=(10, 6))  # 그래프의 크기를 조정
    ax = fig.add_subplot(111)

    yearly_expenses = {}
    for expense in expenses:
        if expense.year not in yearly_expenses:
            yearly_expenses[expense.year] = []
        yearly_expenses[expense.year].append(expense.amount)

    years = list(yearly_expenses.keys())
    amounts = [sum(yearly_expenses[year]) / len(yearly_expenses[year]) for year in years]

    ax.bar([str(year) for year in years], amounts)
    ax.set_xlabel('Year')
    ax.set_ylabel('Amount')
    ax.set_title('annual expenditure')

    # 연 평균 계산
    total_expense = sum(expense.amount for expense in expenses)
    num_years = len(set(expense.year for expense in expenses))
    yearly_average = total_expense / num_years

    ax.text(0.5, 0.98, f'annual average: {yearly_average:.2f}', horizontalalignment='center', verticalalignment='center', transform=ax.transAxes)

    if canvas:  # 기존의 canvas가 존재하는 경우에만 destroy
        canvas.get_tk_widget().destroy()

    canvas = FigureCanvasTkAgg(fig, master=app)
    canvas.draw()
    canvas.get_tk_widget().grid(row=5, columnspan=2)


def add_expense():
    global expenses
    month = int(month_combobox.get())
    year = int(year_combobox.get())
    amount = float(amount_entry.get())
    expense = create_expense(month, year, amount)
    expenses.append(expense)
    print("지출이 추가되었습니다.")

app = tk.Tk()
app.title("지출액 시각화")

# 기간 선택 콤보박스
period_label = tk.Label(app, text="기간 선택: ")
period_label.grid(row=0, column=0)
period_combobox = ttk.Combobox(app, values=["월간", "년간"], state="readonly")
period_combobox.grid(row=0, column=1)
period_combobox.set("월간")  # 기본값을 월간으로 설정

# 연도 선택 콤보박스
year_label = tk.Label(app, text="연도 선택: ")
year_label.grid(row=1, column=0)
year_combobox = ttk.Combobox(app, values=[str(i) for i in range(datetime.now().year - 5, datetime.now().year + 6)], state="readonly")
year_combobox.grid(row=1, column=1)
year_combobox.set(str(datetime.now().year))  # 기본값을 현재 연도로 설정

# 월 선택 콤보박스
month_label = tk.Label(app, text="월 선택: ")
month_label.grid(row=2, column=0)
month_combobox = ttk.Combobox(app, values=[str(i) for i in range(1, 13)], state="readonly")
month_combobox.grid(row=2, column=1)
month_combobox.set("1")  # 기본값을 1월로 설정

tk.Label(app, text="금액: ").grid(row=3, column=0)
amount_entry = tk.Entry(app)
amount_entry.grid(row=3, column=1)

add_button = tk.Button(app, text="지출 추가", command=add_expense)
add_button.grid(row=4, columnspan=2)

visualize_button = tk.Button(app, text="지출액 시각화", command=visualize_expenses)
visualize_button.grid(row=6, columnspan=2)

expenses = []
canvas = None  # 초기에 canvas 변수를 None으로 설정

app.mainloop()
