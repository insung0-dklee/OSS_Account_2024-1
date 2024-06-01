import hashlib
import os
import json
from datetime import datetime
from tkinter import messagebox, simpledialog, ttk, Tk

userdata = {} #아이디, 비밀번호 저장해둘 딕셔너리
userphones = {}
usernames = {}
userdata2 = {}
logged_in_user = None
budget_info = {}

def user_reg_include_name_phone(): #이름과 전화번호 정보를 포함한 회원가입
    id = simpledialog.askstring("회원가입", "ID 입력:")
    if id in userdata:
        messagebox.showerror("회원가입", "이미 존재하는 ID입니다.")
        return
    name = simpledialog.askstring("회원가입", "이름 입력:")
    phone = simpledialog.askstring("회원가입", "전화번호 입력:")
    if phone in userphones: #전화번호 중복 체크 - 중복된 전화번호는 가입 불가
        messagebox.showerror("회원가입", "이미 존재하는 전화번호입니다.")
        return
    #비밀번호 입력 시 *로 표시
    pw = simpledialog.askstring("회원가입", "Password 입력:", show='*')

    h = hashlib.sha256() #hashlib 모듈의 sha256 사용
    h.update(pw.encode()) #sha256으로 암호화
    pw_data = h.hexdigest() # 16진수로 변환

    userdata[id] = pw_data #아이디와 비밀번호 맵핑
    userphones[phone] = id #전화번호와 아이디 맵핑
    usernames[name] = id #이름과 아이디 맵핑
    userdata2[id] = {'pw': pw_data, 'name': name, 'phone': phone} # key에 id값을, value에 비밀번호와 이름, 전화번호 값

    with open('login.txt', 'w', encoding='UTF-8') as fw: # utf-8 변환 후 login.txt에 작성
        for user_id, user_info in userdata2.items(): # 딕셔너리 내에 있는 값을 모두 for문
            fw.write(f'{user_id} : {user_info["pw"]} : {user_info["name"]} : {user_info["phone"]}\n')  # 아이디, 비밀번호, 이름, 전화번호 값을 차례로 login.txt파일에 저장

    messagebox.showinfo("회원가입", "회원가입이 완료되었습니다.")

"""
전화번호를 통해 아이디를 찾는 함수
"""
def find_id_by_phone():
    phone = simpledialog.askstring("아이디 찾기", "찾고자 하는 사용자의 전화번호 입력:")
    if phone in userphones:
        messagebox.showinfo("아이디 찾기", f'해당 전화번호로 등록된 아이디는 {userphones[phone]}입니다.')
    else:
        messagebox.showerror("아이디 찾기", "해당 전화번호를 가진 사용자가 없습니다.")

def user_login(budget_label):
    global logged_in_user
    id = simpledialog.askstring("로그인", "ID 입력:")
    pw = simpledialog.askstring("로그인", "Password 입력:", show='*')

    h = hashlib.sha256()
    h.update(pw.encode())
    pw_data = h.hexdigest()

    if id in userdata and userdata[id] == pw_data:
        logged_in_user = id
        load_budget()
        update_budget_display(budget_label)
        messagebox.showinfo("로그인", "로그인 성공!")
    else:
        messagebox.showerror("로그인", "ID 또는 비밀번호가 잘못되었습니다.")

#로그인을 해야만 가계부 프로그램을 이용할 수 있도록 함수 구현
def ensure_logged_in(func):
    def wrapper(*args, **kwargs):
        if not logged_in_user:
            messagebox.showerror("오류", "먼저 로그인을 해주세요.")
        else:
            return func(*args, **kwargs)
    return wrapper

"""
회원 정보를 수정하는 함수
"""
@ensure_logged_in
def modify_user_info():
    global logged_in_user

    new_phone = simpledialog.askstring("회원 정보 수정", "새로운 전화번호 입력:")

    if new_phone in userphones and userphones[new_phone] != logged_in_user:
        messagebox.showerror("회원 정보 수정", "이미 등록된 전화번호입니다. 다른 전화번호를 사용해주세요.")
        return

    new_pw = simpledialog.askstring("회원 정보 수정", "새로운 password 입력:", show='*')

    h = hashlib.sha256()
    h.update(new_pw.encode())
    new_pw_data = h.hexdigest()

    # Update user information
    old_phone = userdata2[logged_in_user]['phone']
    del userphones[old_phone]

    userdata2[logged_in_user]['pw'] = new_pw_data
    userdata2[logged_in_user]['phone'] = new_phone

    userphones[new_phone] = logged_in_user
    userdata[logged_in_user] = new_pw_data

    with open('login.txt', 'w', encoding='UTF-8') as fw:
        for user_id, user_info in userdata2.items():
            fw.write(f'{user_id} : {user_info["pw"]} : {user_info["name"]} : {user_info["phone"]}\n')

    messagebox.showinfo("회원 정보 수정", "사용자 정보가 성공적으로 수정되었습니다.")

def save_expense(expense, budget_label):
    user_expenses_file = f'expenses_{logged_in_user}.json'
    if not os.path.exists(user_expenses_file):
        with open(user_expenses_file, 'w') as file:
            json.dump([], file)
    with open(user_expenses_file, 'r') as file:
        data = json.load(file)
    data.append(expense)
    with open(user_expenses_file, 'w') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    update_budget_display(budget_label)

@ensure_logged_in
def view_expenses():
    user_expenses_file = f'expenses_{logged_in_user}.json'
    if not os.path.exists(user_expenses_file):
        with open(user_expenses_file, 'w') as file:
            json.dump([], file)
    with open(user_expenses_file, 'r') as file:
        data = json.load(file)
    if data:
        expenses = "\n".join([f"{idx + 1}. {expense['date']} - {expense['item']} : {expense['amount']}원"
                              for idx, expense in enumerate(data)])
        messagebox.showinfo("지출 내역", expenses)
    else:
        messagebox.showinfo("지출 내역", "저장된 지출 내역이 없습니다.")

@ensure_logged_in
def input_expense(budget_label):
    date = simpledialog.askstring("지출 내역 입력", "지출 날짜 (예: 2024-05-30):")
    item = simpledialog.askstring("지출 내역 입력", "지출 항목:")
    amount = simpledialog.askstring("지출 내역 입력", "지출 금액:")
    if date and item and amount:
        expense = {'date': date, 'item': item, 'amount': amount}
        save_expense(expense, budget_label)
        messagebox.showinfo("지출 내역", "지출 내역이 저장되었습니다.")
        update_budget_display(budget_label)

@ensure_logged_in
def delete_expense(budget_label):
    index = simpledialog.askinteger("지출 내역 삭제", "삭제할 지출 항목의 번호를 입력하세요:")
    user_expenses_file = f'expenses_{logged_in_user}.json'
    if not os.path.exists(user_expenses_file):
        with open(user_expenses_file, 'w') as file:
            json.dump([], file)
    with open(user_expenses_file, 'r') as file:
        data = json.load(file)
    if index and 1 <= index <= len(data):
        deleted_expense = data.pop(index - 1)
        with open(user_expenses_file, 'w') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        messagebox.showinfo("삭제 완료", f"다음 내역이 삭제되었습니다: {deleted_expense}")
        update_budget_display(budget_label)
    else:
        messagebox.showerror("오류", "잘못된 번호입니다. 다시 시도하세요.")

@ensure_logged_in
def add_memo():
    title = simpledialog.askstring("메모장", "메모장 제목:")
    if title:
        content = simpledialog.askstring("메모장", "내용 입력:")
        if content:
            user_memo_dir = f'memos_{logged_in_user}'
            if not os.path.exists(user_memo_dir):
                os.makedirs(user_memo_dir)
            with open(f"{user_memo_dir}/{title}.txt", "w", encoding="utf8") as new_f:
                new_f.write(content)
            messagebox.showinfo("메모장", "메모가 저장되었습니다.")
        else:
            messagebox.showerror("메모장", "내용을 입력해주세요.")
    else:
        messagebox.showerror("메모장", "제목을 입력해주세요.")

@ensure_logged_in
def view_memos():
    user_memo_dir = f'memos_{logged_in_user}'
    if not os.path.exists(user_memo_dir):
        os.makedirs(user_memo_dir)
    
    memos = [f.split('.')[0] for f in os.listdir(user_memo_dir) if os.path.isfile(os.path.join(user_memo_dir, f))]
    if memos:
        memo_title = simpledialog.askstring("메모장", "조회할 메모장 제목을 입력하세요:\n" + "\n".join(memos))
        if memo_title in memos:
            with open(f"{user_memo_dir}/{memo_title}.txt", "r", encoding="utf8") as memo_f:
                memo_content = memo_f.read()
            messagebox.showinfo(memo_title, memo_content)
        else:
            messagebox.showerror("메모장", "해당 제목의 메모장이 없습니다.")
    else:
        messagebox.showinfo("메모장", "저장된 메모가 없습니다.")

@ensure_logged_in
def generate_monthly_report():
    user_expenses_file = f'expenses_{logged_in_user}.json'
    if not os.path.exists(user_expenses_file):
        with open(user_expenses_file, 'w') as file:
            json.dump([], file)
    with open(user_expenses_file, 'r') as file:
        data = json.load(file)
    
    if not data:
        messagebox.showinfo("월별 보고서", "조회할 항목이 없습니다.")
        return
    
    report = {}
    for expense in data:
        date = expense['date'][:7]
        amount = int(expense['amount'])
        if date not in report:
            report[date] = 0
        report[date] += amount
    
    report_str = "\n".join([f"{month}: {total}원" for month, total in report.items()])
    messagebox.showinfo("월별 보고서", report_str)

def load_budget():
    global budget_info
    if os.path.exists('budget.json'):
        with open('budget.json', 'r') as file:
            budget_info = json.load(file)

def save_budget():
    with open('budget.json', 'w') as file:
        json.dump(budget_info, file, ensure_ascii=False, indent=4)

@ensure_logged_in
def set_budget(budget_label):
    amount = simpledialog.askinteger("예산 설정", "이번달 예산 금액을 입력하세요:")
    if amount is not None:
        budget_info[logged_in_user] = amount
        save_budget()
        messagebox.showinfo("예산 설정", f"이번달 예산이 {amount}원으로 설정되었습니다.")
        update_budget_display(budget_label)

def update_budget_display(budget_label):
    if logged_in_user:
        budget = budget_info.get(logged_in_user, 0)
        expenses = 0
        user_expenses_file = f'expenses_{logged_in_user}.json'
        if not os.path.exists(user_expenses_file):
            with open(user_expenses_file, 'w') as file:
                json.dump([], file)
        with open(user_expenses_file, 'r') as file:
            data = json.load(file)
        for expense in data:
            if expense['date'][:7] == datetime.now().strftime('%Y-%m'):
                expenses += int(expense['amount'])
        remaining_budget = budget - expenses
        budget_label.config(text=f"이번달 예산: {budget} 원\n남은 금액: {remaining_budget} 원")
        if remaining_budget < 0:
          budget_label.config(text=f"이번달 예산: {budget} 원\n예산 {-1*remaining_budget} 원 초과")



def calculator():
    try:
        expr = simpledialog.askstring("계산기", "계산할 수식을 입력하세요 (예: 2 + 3 * 4):")
        result = eval(expr)
        messagebox.showinfo("결과", f"결과: {result}")
    except Exception as e:
        messagebox.showerror("오류 발생", f"오류 발생: {e}")

@ensure_logged_in
def analyze_categories():
    user_expenses_file = f'expenses_{logged_in_user}.json'
    if not os.path.exists(user_expenses_file):
        with open(user_expenses_file, 'w') as file:
            json.dump([], file)
    with open(user_expenses_file, 'r') as file:
        data = json.load(file)
    
    if not data:
        messagebox.showinfo("카테고리 분석", "저장된 지출 내역이 없습니다.")
        return
    
    monthly_categories = {}
    keywords = {
        '식비': ['식사', '점심', '저녁', '아침', '간식', '음식', '레스토랑', '카페', '식비'],
        '교통': ['기름값', '버스', '지하철', '택시', '교통', '주유', '교통비'],
        '병원' : ['병원', '병원비', '수술'],
        '여행' : ['해외여행', '항공', '비행기', '숙소', '기차', '항공비']
    }
    
    def get_category(item):
        for category, words in keywords.items():
            if any(word in item for word in words):
                return category
        return '기타'
    
    for expense in data:
        date = expense['date'][:7]  # Extract year-month
        item = expense.get('item', '미분류')
        category = get_category(item)
        amount = int(expense['amount'])
        
        if date not in monthly_categories:
            monthly_categories[date] = {}
        
        if category not in monthly_categories[date]:
            monthly_categories[date][category] = 0
        
        monthly_categories[date][category] += amount
    
    report = ""
    for month, categories in monthly_categories.items():
        report += f"\n{month}:\n"
        for category, total in categories.items():
            report += f"  {category}: {total}원\n"
    
    messagebox.showinfo("카테고리 분석", report)
