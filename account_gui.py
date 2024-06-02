import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime

class ExpenseManage(tk.Tk):
    def __init__(self):
        # 부모 클래스의 초기화 메소드 호출
        super().__init__()

        # 윈도우 설정
        self.title("가계부 프로그램")  # 윈도우 제목 설정
        self.geometry("900x600+200+50")  # 윈도우 크기와 위치 설정
        self.configure(bg="#FFF2CD")  # 배경색 설정

        # 현재 날짜 설정
        self.now = datetime.now().strftime("%Y.%m.%d")  # 현재 날짜를 "YYYY.MM.DD" 형식으로 저장

        # 위젯 생성
        self.create_widgets()

    def create_widgets(self):
        # 제목 레이블 생성
        title = tk.Label(self, text="가계부 프로그램", font=("맑은 고딕", 25, "bold"), bg="white", fg="black")
        title.grid(row=0, column=0, columnspan=4, pady=10, padx=10)  # 제목 레이블을 그리드에 배치

        # 메인 패널 생성
        self.create_main_panel()

        # 테이블 생성
        self.create_table()

    def create_main_panel(self):
        # 메인 패널 설정
        main_panel = tk.Frame(self, bg="#F2F2F2")  # 메인 패널 프레임 생성 및 배경색 설정
        main_panel.grid(row=1, column=2, columnspan=2, padx=10, pady=10, sticky="nsew")  # 메인 패널 배치

        # 서브 패널 생성
        self.create_sub_panels(main_panel)
        
        # 초기화 버튼 생성
        self.init_button = tk.Button(main_panel, text="초기화", command=self.init_table, bg="#70AD46", fg="black", font=("맑은 고딕", 12))
        self.init_button.grid(row=0, column=0, padx=10, pady=10, sticky="ew")  # 초기화 버튼을 서브 패널 위에 배치

    def create_sub_panels(self, main_panel):
        # 서브 패널 목록과 관련 함수 설정
        sub_panels = [
            ("항목 추가", self.add_entry),  # 항목 추가 패널과 함수
            ("항목 수정", self.modify_entry)  # 항목 수정 패널과 함수
        ]

        # 각 서브 패널 설정
        for i, (title, command) in enumerate(sub_panels):
            panel = tk.LabelFrame(main_panel, text=title, bg="#FFF2CD", font=("맑은 고딕", 13, "bold"))
            panel.grid(row=i+1, column=0, padx=10, pady=10, sticky="ew")  # 서브 패널 배치
            self.create_sub_panel_content(panel, command)

    def create_sub_panel_content(self, panel, command):
        # 입력 필드 및 레이블 설정
        entries = []
        labels = ["날짜", "내용", "금액"]  # 각 필드의 레이블 텍스트
        for i, label in enumerate(labels):
            lbl = tk.Label(panel, text=label, bg="#FFF2CD", font=("맑은 고딕", 12))  # 레이블 생성
            lbl.grid(row=i, column=0, padx=5, pady=5)  # 레이블 배치
            entry = tk.Entry(panel, font=("맑은 고딕", 15))  # 입력 필드 생성
            entry.grid(row=i, column=1, padx=5, pady=5)  # 입력 필드 배치
            entries.append(entry)  # 입력 필드를 리스트에 추가
        
        # 추가 및 수정 버튼 생성
        button = tk.Button(panel, text="추가" if command == self.add_entry else "수정", 
                           command=lambda: command(entries), bg="#D0CECF", font=("맑은 고딕", 15))
        button.grid(row=0, column=2, rowspan=3, padx=5, pady=5, sticky="ns")  # 버튼 배치

    def create_table(self):
        # 테이블 설정
        columns = ["날짜", "내용", "금액"]  # 테이블 열 이름 설정
        self.tree = ttk.Treeview(self, columns=columns, show="headings", height=20)  # 테이블 생성
        for col in columns:
            self.tree.heading(col, text=col)  # 각 열의 헤딩 설정
            self.tree.column(col, width=150)  # 각 열의 너비 설정
        
        # 테이블 위치 설정
        self.tree.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")  # 테이블 배치
        
        # 테이블 항목 더블 클릭 이벤트 바인딩
        self.tree.bind("<Double-1>", self.delete_row)

    def init_table(self):
        # 테이블 초기화 함수
        for item in self.tree.get_children():
            self.tree.delete(item)  # 테이블의 모든 항목 삭제

    def add_entry(self, entries):
        # 항목 추가 함수
        date, description, amount = [entry.get() for entry in entries]  # 입력된 값을 가져옴
        
        # 필수값 확인
        if not date or not description or not amount:
            messagebox.showerror("오류", "값을 입력하세요.")  # 오류 메시지 표시
            return
        
        # 테이블에 항목 추가
        self.tree.insert("", "end", values=(date, description, amount))  # 테이블에 새 항목 추가
        messagebox.showinfo("추가", "항목이 추가 되었습니다.")  # 성공 메시지 표시

    def modify_entry(self, entries):
        # 항목 수정 함수
        date, description, amount = [entry.get() for entry in entries]  # 입력된 값을 가져옴
        
        # 필수값 확인
        if not date or not description or not amount:
            messagebox.showerror("오류", "값을 입력하세요.")  # 오류 메시지 표시
            return
        
        # 선택된 항목 확인
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("오류", "수정할 항목을 선택하세요.")  # 오류 메시지 표시
            return
        
        # 테이블 항목 수정
        self.tree.item(selected_item, values=(date, description, amount))  # 선택된 항목 수정
        messagebox.showinfo("수정", "항목이 수정 되었습니다.")  # 성공 메시지 표시

    # 테이블의 항목 더블 클릭 시 해당 항목 삭제 가능
    def delete_row(self, event):
        # 항목 삭제 함수
        selected_item = self.tree.selection()[0]  # 선택된 항목 가져오기
        self.tree.delete(selected_item)  # 선택된 항목 삭제

if __name__ == "__main__":
    # 프로그램 실행
    app = ExpenseManage()  # ExpenseManage 클래스 인스턴스 생성
    app.mainloop()  # 메인 루프 실행
