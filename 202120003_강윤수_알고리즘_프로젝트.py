Coffee = ['아메리카노', '카페라떼', '바닐라라떼']
Drink = ['에이드', '스무디']
name=[""]  
price=[2500, 3000, 3500,4000, 4500]
total=0 #총 주문금액
order = [] #주문서
i=0     #음료이름[i] 초기값 0 

print("어서오세요. 상명 카페입니다.")
print('<Coffee>', Coffee)
print('<Drink>', Drink)


while True:
    print("주문하시겠습니까?")
    print("결제를 원하시면 '주문완료'를 입력해주세요.")
    name[i] = input("")
    #커피
    if name[i] == '아메리카노':
        print('아이스로 변경하시겠습니까?(예/아니오)')
        ice = str(input(''))
        if ice == '예':
            print('500원 추가됩니다.')
            print()
            print('아이스아메리카노 선택되었습니다.\n몇 잔 주문하시겠어요?')
            count = int(input(''))
            print('아이스아메리카노', count,'잔 주문하셨습니다. 가격:', price[1]*count)
            print()
            total = total+(price[1]*count)
            order.append('아이스아메리카노')
            print()
        elif ice == '아니오':
            print('아메리카노 선택되었습니다.\n몇 잔 주문하시겠어요?')
            count = int(input(''))
            print('아메리카노', count,'잔 주문하셨습니다. 가격:', price[0]*count)
            print()
            total = total+(price[0]*count)
            order.append('아메리카노')
            print()
        else:
            print('죄송합니다. "예" 또는 "아니오"로 입력해주세요.')
            print()
    elif name[i] == '카페라떼':
        print('아이스로 변경하시겠습니까?(예/아니오)')
        print()
        ice = str(input(''))
        if ice == '예':
            print('500원 추가됩니다.')
            print()
            print('아이스카페라떼 선택되었습니다.\n몇 잔 주문하시겠어요?')
            count = int(input(''))
            print('아이스카페라떼', count,'잔 주문하셨습니다. 가격:', price[2]*count)
            print()
            total = total+(price[2]*count)
            order.append('아이스카페라떼')
        elif ice == '아니오':
            print('카페라떼 선택되었습니다.\n몇 잔 주문하시겠어요?')
            count = int(input(''))
            print('카페라떼', count,'잔 주문하셨습니다. 가격:', price[1]*count)
            print()
            total = total+(price[1]*count)
            order.append('카페라떼')
        else:
            print('죄송합니다. "예" 또는 "아니오"로 입력해주세요.')
            print()
    elif name[i] == '바닐라라떼':
        print('아이스로 변경하시겠습니까?(예/아니오)')
        print()
        ice = str(input(''))
        if ice == '예':
            print('500원 추가됩니다.')
            print()
            print('아이스바닐라라떼 선택되었습니다.\n몇 잔 주문하시겠어요?')
            count = int(input(''))
            print('아이스바닐라라떼', count,'잔 주문하셨습니다. 가격:', price[3]*count)
            print()
            total = total+(price[3]*count)
            order.append('아이스바닐라라떼')
        elif ice == '아니오':
            print('바닐라라떼 선택되었습니다.\n몇 잔 주문하시겠어요?')
            count = int(input(''))
            print('바닐라라떼', count,'잔 주문하셨습니다. 가격:', price[2]*count)
            print()
            total = total0+(price[2]*count)
            order.append('바닐라라떼')
        else:
            print('죄송합니다. "예" 또는 "아니오"로 입력해주세요.')
            print()
    #음료
    elif name[i] == '에이드':
        print('종류를 선택해주세요.\n자몽, 망고')
        print()
        ade = str(input(''))
        if ade == '자몽':
            print('자몽에이드 선택되었습니다.\n몇 잔 주문하시겠어요?')
            count = int(input(''))
            print('자몽에이드', count,'잔 주문하셨습니다. 가격:', price[4]*count)
            print()
            total = total+(price[4]*count)
            order.append('자몽에이드')
        elif ade == '망고':
            print('망고에이드 선택되었습니다.\n몇 잔 주문하시겠어요?')
            count = int(input(''))
            print('망고에이드', count,'잔 주문하셨습니다. 가격:', price[4]*count)
            print()
            total = total+(price[4]*count)
            order.append('망고에이드')
        else:
            print('해당 메뉴는 준비 중입니다.\n다른 메뉴를 선택해주세요.')
            print()
    elif name[i] == '스무디':
        print('종류를 선택해주세요.\n요거트, 망고')
        print()
        smoothie = str(input(''))
        if smoothie == '요거트':
            print('요거트스무디 선택되었습니다.\n몇 잔 주문하시겠어요?')
            count = int(input(''))
            print('요거트스무디', count,'잔 주문하셨습니다. 가격:', price[4]*count)
            print()
            total = total+(price[4]*count)
            order.append('요거트스무디')
        elif smoothie == '망고':
            print('망고스무디 선택되었습니다.\n몇 잔 주문하시겠어요?')
            count = int(input(''))
            print('망고스무디', count,'잔 주문하셨습니다. 가격:', price[4]*count)
            print()
            total = total+(price[4]*count)
            order.append('망고스무디')
        else:
            print('해당 메뉴는 준비 중입니다.\n다른 메뉴를 선택해주세요.')
            print()

    elif name[i] == '주문완료':
        print()
        print('*영수증*')
        print(order)
        print('합계:', total)
        print()
        print('감사합니다:)') 
        break
    else:
        print('해당 메뉴는 준비 중입니다.\n다른 메뉴를 선택해주세요.')
        print()
        continue
        
   
