taxi=10000
taxitime=20
train=3000
traintime=30
bus=2000
bustime=40
bike=0
biketime=60

check=0
up1=int(input("(시)기상 시간 : "))
up2=int(input("(분)기상 시간 : "))
first1=int(input("(시)수업시간 : "))
first2=int(input("(분)수업시간 : "))
up=(up1*60)+up2
first=(first1*60)+first2
clock=first-up
money=int(input("용돈 : "))
Rmoney=0
Traffic=0
Food=0

if clock >= taxitime:
    check=1
    print("------------------------------등교-------------------------------")
    print("택시 : 10000원, 전철 : 3000원, 버스 : 2000원, 자전거 : 2000원 미만")
    print("-----------------------------------------------------------------")
    if money >= taxi:
        print("등교 추천 ) 택시,전철,버스,자전거")
        pick=input("타고갈 것 선택 : ")
        if pick=="택시":
            print("지각하지않고 등교")
            print("남은 용돈 :",money-taxi,'원')
            Rmoney=money-taxi
            Traffic=taxi
        elif pick=="전철":
            if clock >= traintime:
                print("지각하지않고 등교")
                print("남은 용돈 :",money-train,'원')
                Rmoney=money-train
                Traffic=train
            else:
                print(traintime - clock,'분 지각')
                print("남은 용돈 :",money-train,'원')
                Rmoney=money-train
                Traffic=train
        elif pick=="버스":
            if clock >= bustime:
                print("지각하지않고 등교")
                print("남은 용돈 :",money-bus,'원')
                Rmoney=money-bus
                Traffic=bus
            else:
                print(bustime - clock,'분 지각')
                print("남은 용돈 :",money-bus,'원')
                Rmoney=money-bus
                Traffic=bus
        elif pick=="자전거":
            if clock >= biketime:
                print("지각하지않고 등교")
                print("남은 용돈 :",money-bike,'원')
                Rmoney=money-bike
                Traffic=bike
            else:
                print(biketime - clock,'분 지각')
                print("남은 용돈 :",money-bike,'원')
                Rmoney=money-bike
                Traffic=bike
    elif taxi > money >= train:
        print("등교 추천 ) 전철,버스,자전거")
        pick=input("타고갈 것 선택 : ")
        if pick=="전철":
            if clock >= traintime:
                print("지각하지않고 등교")
                print("남은 용돈 :",money-train,'원')
                Rmoney=money-train
                Traffic=train
            else:
                print(traintime - clock,'분 지각')
                print("남은 용돈 :",money-train,'원')
                Rmoney=money-train
                Traffic=train
        elif pick=="버스":
            if clock >= bustime:
                print("지각하지않고 등교")
                print("남은 용돈 :",money-bus,'원')
                Rmoney=money-bus
                Traffic=bus
            else:
                print(bustime - clock,'분 지각')
                print("남은 용돈 :",money-bus,'원')
                Rmoney=money-bus
                Traffic=bus
        elif pick=="자전거":
            if clock >= biketime:
                print("지각하지않고 등교")
                print("남은 용돈 :",money-bike,'원')
                Rmoney=money-bike
                Traffic=bike
            else:
                print(biketime - clock,'분 지각')
                print("남은 용돈 :",money-bike,'원')
                Rmoney=money-bike
                Traffic=bike
    elif train > money >= bus:
        print("등교 추천 ) 버스,자전거")
        pick=input("타고갈 것 선택 : ")
        if pick=="버스":
            if clock >= bustime:
                print("지각하지않고 등교")
                print("남은 용돈 :",money-bu,'원')
                Rmoney=money-bus
                Traffic=bus
            else:
                print(bustime - clock,'분 지각')
                print("남은 용돈 :",money-bus,'원')
                Rmoney=money-bus
                Traffic=bus
        elif pick=="자전거":
            if clock >= biketime:
                print("지각하지않고 등교")
                print("남은 용돈 :",money-bike,'원')
                Rmoney=money-bike
                Traffic=bike
            else:
                print(biketime - clock,'분 지각')
                print("남은 용돈 :",money-bike,'원')
                Rmoney=money-bike
                Traffic=bike
    else:
        print("등교 추천 ) 자전거")
        pick=input("타고갈 것 선택 : ")
        if pick=="자전거":
            if clock >= biketime:
                print("지각하지않고 등교")
                print("남은 용돈 :",money-bike,'원')
                Rmoney=money-bike
                Traffic=bike
            else:
                print(biketime - clock,'분 지각')
                print("남은 용돈 :",money-bike,'원')
                Rmoney=money-bike
                Traffic=bike
else:
    print("너무 늦게 일어나 등교 포기")
steak=10000
nuddle=2500
bibimbap=5000
cup=500
if check==1 and Rmoney >= cup:
    print("--------------------------점심시간----------------------------------")
    print("스테이크 : 10000원, 라면 : 2500원, 비빔밥 : 5000원, 컵떡볶이 : 500원")
    print("--------------------------------------------------------------------")
    print("남은 용돈 :",Rmoney)
    if Rmoney >= steak:
        print("음식 추천 ) 스테이크, 라면, 비빔밥, 컵떡볶이")
        pick=input("먹을 음식 선택 : ")
        if pick=="스테이크":
            print("스테이크를 먹었습니다.")
            print("남은 용돈 :",Rmoney-steak,'원')
            Rmoney=Rmoney-steak
            Food=steak
        elif pick=="라면":
            print("라면을 먹었습니다.")
            print("남은 용돈 :",Rmoney-nuddle,'원')
            Rmoney=Rmoney-nuddle
            Food=nuddle
        elif pick=="비빔밥":
            print("비빔밥을 먹었습니다.")
            print("남은 용돈 :",Rmoney-bibimbap,'원')
            Rmoney=Rmoney-bibimbap
            Food=bibimbap
        elif pick=="컵떡볶이":
            print("컵떡볶이를 먹었습니다.")
            print("남은 용돈 :",Rmoney-cup,'원')
            Rmoney=Rmoney-cup
            Food=cup
    elif steak > Rmoney >= bibimbap:
        print("음식 추천 ) 라면, 비빔밥, 컵떡볶이")
        pick=input("먹을 음식 선택 : ")
        if pick=="라면":
            print("라면을 먹었습니다.")
            print("남은 용돈 :",Rmoney-nuddle,'원')
            Rmoney=Rmoney-nuddle
            Food=nuddle
        elif pick=="비빔밥":
            print("비빔밥을 먹었습니다.")
            print("남은 용돈 :",Rmoney-bibimbap,'원')
            Rmoney=Rmoney-bibimbap
            Food=bibimbap
        elif pick=="컵떡볶이":
            print("컵떡볶이를 먹었습니다.")
            print("남은 용돈 :",Rmoney-cup,'원')
            Rmoney=Rmoney-cup
            Food=cup
    elif bibimbap > Rmoney >= nuddle:
        print("음식 추천 ) 비빔밥, 컵떡볶이")
        pick=input("먹을 음식 선택 : ")
        if pick=="비빔밥":
            print("비빔밥을 먹었습니다.")
            print("남은 용돈 :",Rmoney-bibimbap,'원')
            Rmoney=Rmoney-bibimbap
            Food=bibimbap
        elif pick=="컵떡볶이":
            print("컵떡볶이를 먹었습니다.")
            print("남은 용돈 :",Rmoney-cup,'원')
            Rmoney=Rmoney-cup
            Food=cup
    elif nuddle > Rmoney >= cup:
        print("음식 추천 ) 컵떡볶이")
        pick=input("먹을 음식 선택 : ")
        if pick=="컵떡볶이":
            print("컵떡볶이를 먹었습니다.")
            print("남은 용돈 :",Rmoney-cup,'원')
            Rmoney=Rmoney-cup
            Food=cup
elif Rmoney<cup:
    print("음식을 사먹을 돈이 없습니다.")
else:
    print("")
        
if check==1:
    print("----------------------------하교--------------------------------")
    print("택시 : 10000원, 전철 : 3000원, 버스 : 2000원, 자전거 : 2000원 미만")
    print("---------------------------------------------------------------")
    print("남은 용돈 :",Rmoney)
    if Rmoney >= taxi:
        print("하교 추천 ) 택시,전철,버스,자전거")
        pick=input("타고갈 것 선택 : ")
        if pick=="택시":
            print("택시를 타고 하교")
            print("남은 용돈 :",Rmoney-taxi,'원')
            Rmoney=Rmoney-taxi
            Traffic=Traffic+taxi
        elif pick=="전철":
            print("전철을 타고 하교")
            print("남은 용돈 :",Rmoney-train,'원')
            Rmoney=Rmoney-train
            Traffic=Traffic+train
        elif pick=="버스":
            print("버스를 타고 하교")
            print("남은 용돈 :",Rmoney-bus,'원')
            Rmoney=Rmoney-bus
            Traffic=Traffic+bus
        elif pick=="자전거":
            print("자전거 타고 하교")
            print("남은 용돈 :",Rmoney-bike,'원')
            Rmoney=Rmoney-bike
            Traffic=Traffic+bike
    elif taxi > Rmoney >= train:
        print("하교 추천 ) 전철,버스,자전거")
        pick=input("타고갈 것 선택 : ")
        if pick=="전철":
            print("전철을 타고 하교")
            print("남은 용돈 :",Rmoney-train,'원')
            Rmoney=Rmoney-train
            Traffic=Traffic+train
        elif pick=="버스":
            print("버스를 타고 하교")
            print("남은 용돈 :",Rmoney-bus,'원')
            Rmoney=Rmoney-bus
            Traffic=Traffic+bus
        elif pick=="자전거":
            print("자전거 타고 하교")
            print("남은 용돈 :",Rmoney-bike,'원')
            Rmoney=Rmoney-bike
            Traffic=Traffic+bike
    elif train > Rmoney >= bus:
        print("하교 추천 ) 버스,자전거")
        pick=input("타고갈 것 선택 : ")
        if pick=="버스":
            print("버스를 타고 하교")
            print("남은 용돈 :",Rmoney-bus,'원')
            Rmoney=Rmoney-bus
            Traffic=Traffic+bus
        elif pick=="자전거":
            print("자전거 타고 하교")
            print("남은 용돈 :",Rmoney-bike,'원')
            Rmoney=Rmoney-bike
            Traffic=Traffic+bike
    else:
        print("하교 추천 ) 자전거")
        pick=input("타고갈 것 선택 : ")
        if pick=="자전거":
            print("자전거 타고 하교")
            print("남은 용돈 :",Rmoney-bike,'원')
            Rmoney=Rmoney-bike
            Traffic=Traffic+bike
        else:
            print("돈이 없어서 자전거를 탑니다.")
else:
    print("")
print("식비 :",Food,'원')
print("교통비 :",Traffic,'원')

