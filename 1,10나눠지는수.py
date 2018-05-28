#1 ~ 10 사이의 어떤 수로도 나누어 떨어지는 가장 작은 수
tu=(1,2,3,4,5,6,7,8,9,10)
j=1
while True:
    for i in range(len(tu)):
        if j%tu[i]==0:  # j를 1부터 10까지 나눠 나머지가 0이면 continue
            continue
        else:
            j=j+1       # 나머지가 0이 아니면 j를 1증가, 반복문 빠져나옴
            break
    if tu[i]==10 and j%tu[i]==0:    # 1~10까지 모두 나눠지면 j를 프린트해줌
        print(j)
        break
    
