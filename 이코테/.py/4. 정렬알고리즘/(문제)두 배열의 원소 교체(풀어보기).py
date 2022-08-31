# N개의 원소, K번의 바꿔치기
N, K = map(int, input().split(' '))

A = list(map(int, input().split()))
B = list(map(int, input().split()))

# K번만 바꿀 수 있으므로 A에서 가장 작은 숫자 K개, B에서 가장 큰 숫자 K개를 바꾸기
for _ in range(K):
    A.sort()
    B.sort()
    A[0], B[N-1] = B[N-1], A[0]

print(sum(A))
