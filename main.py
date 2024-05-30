b_is_exit = 0
Allproduct=[]
Allcost=[]
exit=0
while not b_is_exit:
    func = input("기능 입력 (? 입력시 도움말) : ")
    print("1: 가게부 입력 ")
    if func == "1":
        product=input("무엇을 구매하였는지 작성하시오 : ")
        cost=int(input("얼마에 구매하였는지 작성하시오 : "))
        for i in range(0,len(Allproduct)):
            if Allproduct[i]==product:
                ALLcost[i]+=cost
                exit=1
                break
        if exit!=1:
            Allproduct.append(product)
            Allcost.append(cost) 
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

