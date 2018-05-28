import random

def Sum(tup,len):
    sum=0
    i=0
    while i<len:
        sum=sum+tup[i]  #sum에 튜플에 저장된 값을 차례로 더해줌
        i=i+1
    return sum

def Avg(tup,len):
    avg=0
    sum=0
    i=0
    while i<len:
        sum=sum+tup[i]
        i=i+1
    avg=sum/5
    return avg

def Max(tup,len):
    max=0
    for i in tup:
        if max<i:   #max 값과 튜플에 저장된 값을 차례로 비교
            max=i
    return max
    
def Min(tup,len):
    min=tup[0]
    for i in tup:
        if min>i:
            min=i
    return min

a1=random.randint(1,100) #1~100사이 랜덤값
a2=random.randint(1,100)
a3=random.randint(1,100)
a4=random.randint(1,100)
a5=random.randint(1,100)

tup=(a1,a2,a3,a4,a5) #튜플에 랜덤 값 5개 저장
print(tup)
print('합계 :',Sum(tup,5)) #튜플, 저장된 숫자의 개수 전달
print('평균 :',Avg(tup,5))
print('최대값 :',Max(tup,5))
print('최소값 :',Min(tup,5))
