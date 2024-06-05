import tkinter as tk
from tkinter import messagebox
import random

def calculate_share(total_amount, participants, names, n):
    per_person = total_amount / n
    results = [f"{name}: {per_person:.2f}" for name in names[:n]]
    return results

def calculate_rate(total_amount, participants, names, rates):
    results = []
    random.shuffle(rates)
    total_rate = sum(rates)
    for i, name in enumerate(names):
        amount = total_amount * (rates[i] / total_rate)
        results.append(f"{name}: {amount:.2f}")
    return results

def on_submit():
    try:
        total_amount = float(entry_amount.get())
        participants = int(entry_participants.get())
        names = [entry_names[i].get() for i in range(participants)]
        option = option_var.get()

        if option == "몰아주기":
            n = int(entry_n.get())
            results = calculate_share(total_amount, participants, names, n)
        elif option == "결제 비율":
            rates = [float(entry_rates[i].get()) for i in range(participants)]
            results = calculate_rate(total_amount, participants, names, rates)
        else:
            results = []

        result_text = "\n".join(results)
        messagebox.showinfo("결과", result_text)
    except ValueError:
        messagebox.showerror("오류", "입력값을 확인하세요.")

app = tk.Tk()
app.title("계산 배분하기")

tk.Label(app, text="총 금액:").grid(row=0, column=0)
entry_amount = tk.Entry(app)
entry_amount.grid(row=0, column=1)

tk.Label(app, text="참가자 인원:").grid(row=1, column=0)
entry_participants = tk.Entry(app)
entry_participants.grid(row=1, column=1)

entry_names = []
entry_rates = []

def create_name_entries(event):
    for entry in entry_names + entry_rates:
        entry.destroy()
    entry_names.clear()
    entry_rates.clear()
    try:
        participants = int(entry_participants.get())
        for i in range(participants):
            tk.Label(app, text=f"참가자 {i+1} 이름:").grid(row=3+i, column=0)
            entry_name = tk.Entry(app)
            entry_name.grid(row=3+i, column=1)
            entry_names.append(entry_name)
            tk.Label(app, text=f"비율 {i+1}:").grid(row=3+i, column=2)
            entry_rate = tk.Entry(app)
            entry_rate.grid(row=3+i, column=3)
            entry_rates.append(entry_rate)
        
        tk.Label(app, text="n명에게 몰아주기 (몰아주기 옵션 선택 시):").grid(row=3+participants, column=0)
        entry_n.grid(row=3+participants, column=1)
        tk.Button(app, text="계산", command=on_submit).grid(row=4+participants, column=0, columnspan=4)
    except ValueError:
        pass

entry_participants.bind("<Return>", create_name_entries)

tk.Label(app, text="옵션:").grid(row=2, column=0)
option_var = tk.StringVar(value="몰아주기")
tk.Radiobutton(app, text="몰아주기", variable=option_var, value="몰아주기").grid(row=2, column=1, sticky="w")
tk.Radiobutton(app, text="결제 비율", variable=option_var, value="결제 비율").grid(row=2, column=2, sticky="w")

entry_n = tk.Entry(app)

app.mainloop()
