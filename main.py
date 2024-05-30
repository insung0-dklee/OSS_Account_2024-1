import hashlib #hashlib 사용

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
import tkinter as tk
w=tk.Tk()
w.title('가계부') # 제목을 '가계부로 설정'
w.geometry('200x400') # 가로 200, 세로 400으로 설정
name_label=tk.Label(w,text='품목')#라벨을 생성해 '품목'이라는 텍스트 표시
name_label.pack() #라벨을 화면에 표시
name_entry=tk.Entry(w) #라벨을 생성해 품목을 입력할 수 있는 공간 생성
name_entry.pack() #라벨을 화면에 표시

amount_label=tk.Label(w, text='금액') #라벨을 생성해 '금액'이라는 텍스트 표시
amount_label.pack() #라벨을 화면에 표시
amount_entry=tk.Entry(w) #엔트리를 생성해 금액을 입력할 수 있는 공간 생성
amount_entry.pack() # 생성한 엔트리를 화면에 표시
add_button=tk.Button(w,text='추가') #버튼을 생성해 '추가'라는 텍스트를 표시 
add_button.pack() # 생성한 버튼을 화면에 표시
remove_button=tk.Button(w,text='삭제') #버튼을 생성해 '삭제'라는 텍스트를표시 
remove_button.pack() # 생성한 버튼을 화면에 표시
save_button=tk.Button(w,text='저장') #버튼을 생성해 '저장'이라는 텍스트를 표시
save_button.pack() # 생성한 버튼을 화면에 표시
listbox=tk.Listbox(w,selectmode=tk.SINGLE) #리스트박스를 생성해 화면에 표시
listbox.pack()#생성한 리스트박스를 화면에 표시
total_label=tk.Label(w,text='총 지출: 0원') #라벨을 생성해 '총 지출: 0원'이라는 텍스트를 표시  
total_label.pack() #생성한 라벨을 화면에 표시
w.mainloop() 
