import tkinter as tk
from tkinter import messagebox

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def submit():   
# 입력 상자의 내용을 가져옵니다.
    name = name_entry.get()
    money = money_entry.get()
    if not is_number(money):
        messagebox.showerror("error", "숫자가 아님이다！")
        return
    print(f"상품: {name}, 가격: {money}")
    root.destroy()
# GUI
def create_window():
    global name_entry, money_entry, root

    root = tk.Tk()
    root.title("제품정보")
    root.geometry("300x200")

    name_label = tk.Label(root, text="가격정보:")
    name_label.pack(pady=5)
    name_entry = tk.Entry(root)
    name_entry.pack(pady=5)

    money_label = tk.Label(root, text="제품:")
    money_label.pack(pady=5)
    money_entry = tk.Entry(root)
    money_entry.pack(pady=5)

    submit_button = tk.Button(root, text="제출", command=submit)
    submit_button.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    create_window()