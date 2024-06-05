import tkinter as tk
from tkinter import ttk

class GroupedCombobox(ttk.Combobox):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.bind('<Button-1>', self.show_menu)
        self.menu = tk.Menu(self, tearoff=0)
        self.selected_option = None

    def set_options(self, options):
        self.options = options
        self.update_menu()

    def update_menu(self):
        self.menu.delete(0, tk.END)
        for option in self.options:
            if isinstance(option, dict):
                label = option.get('label', 'Group')
                submenu = tk.Menu(self.menu, tearoff=0)
                for item in option.get('items', []):
                    submenu.add_command(label=item, command=lambda val=item: self.set_value(val))
                self.menu.add_cascade(label=label, menu=submenu)
            else:
                self.menu.add_command(label=option, command=lambda val=option: self.set_value(val))

    def show_menu(self, event):
        try:
            self.menu.tk_popup(event.x_root, event.y_root)
        finally:
            self.menu.grab_release()

    def set_value(self, value):
        self.set(value)
        self.selected_option = value
        print(f"Selected option: {value}")

    def tariff_rate(self):
        value = self.selected_option
        if value in ["의류/수영복/속옷", "신발류", "텐트"]:
            return 13
        elif value == "잉크":
            return 6.5
        elif value == "꿀":
            return 20
        elif value == "페인트":
            return 7
        elif value == "금괴(골드바)":
            return 3
        else:
            return 8

def create_gui():
    def calculate_tariff():
        try:
            amount = float(price_entry.get())
            rate = combo.tariff_rate()
            tariff = amount * rate / 100
            total_amount = amount + tariff
            result_label.config(text=f"관세: {tariff:.2f}, 총 금액: {total_amount:.2f}")
        except ValueError:
            result_label.config(text="올바른 금액을 입력하세요.")

    root = tk.Tk()
    root.title("관세 계산기")
    root.geometry("600x400")

    label = tk.Label(root, text="Choose an option:")
    label.pack(pady=10)

    combo = GroupedCombobox(root)
    combo.pack(pady=10)

    options = [
        {"label": "의류", "items": ["의류/수영복/속옷", "스카프/숄/넥타이/장갑", "액세사리", "신발류", "가방/핸드백", "선글래스"]},
        {"label": "전자기기", "items": ["면도기/다리미", "CDP/MP3/오디오/스피커", "캠코더", "폴라로이드 카메라/필름 카메라", "영사기", "PDP", "가습기", "전기전자제어판", "공기청정기"]},
        {"label": "기타", "items": ["화장품/향수", "펜", "잉크", "골프채", "모터보트 관련", "행글라이더", "수상스키", "텐트", "낚시대", "동물사료", "꿀", "방독면", "건강보조식품(최대수량 6개)", "액션피규어", "자전거(부품)", "페인트", "금괴(골드바)"]}
    ]
    combo.set_options(options)

    price_label = tk.Label(root, text="가격:")
    price_label.pack(pady=5)
    
    price_entry = tk.Entry(root)
    price_entry.pack(pady=5)
    
    calculate_button = tk.Button(root, text="확인", command=calculate_tariff)
    calculate_button.pack(pady=10)
    
    result_label = tk.Label(root, text="")
    result_label.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    create_gui()
