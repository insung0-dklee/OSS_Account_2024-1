import tkinter as tk

class Calculator(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry("200x200")  # GUI 크기 조정
        self.create_widgets()
        
    def create_widgets(self):
        # 계산기에 대한 위젯들을 생성합니다.
        self.display = tk.Entry(self)
        self.display.grid(row=0, column=0, columnspan=4)
        
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]
        
        # 버튼들을 생성하고 그리드에 배치합니다.
        row = 1
        col = 0
        for button_text in buttons:
            tk.Button(self, text=button_text, command=lambda text=button_text: self.on_button_click(text)).grid(row=row, column=col)
            col += 1
            if col > 3:
                col = 0
                row += 1

    def on_button_click(self, button_text):
        # 버튼 클릭 시 동작하는 함수
        if button_text == '=':
            try:
                result = eval(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except Exception as e:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        elif button_text == 'C':
            self.display.delete(0, tk.END)
        else:
            self.display.insert(tk.END, button_text)