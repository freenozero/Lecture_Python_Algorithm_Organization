#N원을 거슬뤄 줘야할 때 동전으로 거슬러 줄 수 있는 최소 갯
n = int(input("거슬러 줘야할 돈:"))
count = 0

array = [500,100,50,10,1]

for coin in array:
    count += n // coin #결과 값에 n을 coin으로 나눈 최대 값
    n %= coin

print(count)
