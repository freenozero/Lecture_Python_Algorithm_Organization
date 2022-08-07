#N의 값이 1이 될 떄까지의 최소횟수
#1. N에서 1을 뺀다
#2. N을 K로 나눈다
#이 두 가지 방식 중 하나를 반복적으로 선택하여 수행한다
#두번째 방식의 경우는 N이 K로 나누어 떨어질 때만 수행한다

#내가 만든 거랑 다른 이유가 빨리 실행되고, n과 k가 큰 수여도 시간복잡도가 작아서 빠르게 해결가능하다.

#내가 푼 방식
N = int(input("N:"))
K = int(input("K:"))

count = 0

while(N != 1):
    if (N%K)==0:
        N /= K
    else: N -= 1
    count += 1
print(count)



#답안 예시
n, k = map(int, input().split())

result = 0

while True:
    target = (n//k) * k #n이 k로 나누어 떨어지는 수가 될 때까지 빼기
    result += (n - target) #1을 빼는 연산을 몇 번 수행했는지 넣기

    n = target

    #n이 k보다 작을 때 반복문 탈출
    if n < k:
        break

    result += 1
    n //= k

# 마지막으로 남은 수에 대해서 1씩 빼
result += (n -1)
print(result)


