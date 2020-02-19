store=0
price=0
stock=0
sold=0
earnings=0
sold_list=[]
earnings_list=[]
while True:
    choose=int(input('which function would you like to use?1=set;2=stock;3=ship;4=turnover;5=inventory:'))
    if choose==1:
        store=int(input('how many apples do you have in store?'))
        price=int(input('how much does each apple cost?'))
        print('store:',store)
        print('price:',price)
    elif choose==2:
        stock=int(input('how many apples were stocked today?'))
        store=store+stock
        print(store,' apples in store')
    elif choose==3:
        sold=int(input('how many apples were sold today?'))
        sold_list.append(sold)
        earnings=price*sold
        earnings_list.append(earnings)
        print(sold,' apples sold')
        print('earnings: ',earnings)
    elif choose==4:
        print(sold_list)
        print(earnings_list)
        print(earnings)
    elif choose==5:
        print(store,' apples in store')
    else:
        print('error')
        break