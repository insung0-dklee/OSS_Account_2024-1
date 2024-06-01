from math import * 
from tkinter import * 

"""
 US달러와 KR원을 환율에 따라 계산해주는 환율 계산기
 """
class USD_KRW_ExchangeCalculator(): 

    def __init__(self, master): 
        frame = LabelFrame(master, text="USD_KRW Exchange Calculator", relief=GROOVE)
        frame.pack()
        self.USD_KRW_Ratio = DoubleVar() 
        self.us_dollar_var = DoubleVar() 
        self.kr_won_var = DoubleVar() 
        Label(frame, text = 'Exchange Ratio (1 USD => x KRW)').grid(row=0, column=0) 
        Entry(frame, textvariable=self.USD_KRW_Ratio, justify=RIGHT).grid(row=0, column=1)
        Label(frame, text = 'US Dollar').grid(row=1, column=0)
        Entry(frame, textvariable=self.us_dollar_var, justify=RIGHT).grid(row=1, column=1)
        Label(frame, text = 'Korean Won').grid(row=2, column=0) 
        Entry(frame, textvariable=self.kr_won_var, justify=RIGHT).grid(row=2, column=1)
       
        button = Button(frame, text='US Dollar -> Kr Won', command=self.convert_USD_KRW, bg="light pink") 
        button.grid(row=3, column=0) 
        button = Button(frame, text='Kr Won-> US Dollar', command=self.convert_KRW_USD, bg="sky blue") 
        button.grid(row=3, column=1) 

    def convert_USD_KRW(self): 
        currency_ratio = self.USD_KRW_Ratio.get() #환율
        usd = self.us_dollar_var.get()
        krw = usd * currency_ratio #달러->원으로 바꾸는 계산
        krw_round = round(krw, 2)
        self.kr_won_var.set(krw_round) #값 대입

    def convert_KRW_USD(self): 
        currency_ratio = self.USD_KRW_Ratio.get() #환율
        krw = self.kr_won_var.get()
        usd = krw / currency_ratio #원->달러로 바꾸는 계산
        usd_round = round(usd, 2)
        self.us_dollar_var.set(usd_round) #값 대입


def main():
    win = Tk()
    win.wm_title('USD_KRW Exchange Calculator')
    app = USD_KRW_ExchangeCalculator(win)
    win.mainloop()

if __name__ == "__main__": 
    main() #실행
