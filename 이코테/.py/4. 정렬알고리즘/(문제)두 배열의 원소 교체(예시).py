# 문제 해결 아이디어
# 핵심 아이디어: 매번 배열 A에서 가장 작은 원소를 골라서, 배열 B에서 가장 큰 원소와 교체한다.
# 1. 가장 먼저 배열 A와 B가 주어지면, A에 대하여 오름차순 정렬하고, B에 대하여 내림차순 정렬한다.
# 2. 이후에 두 배열의 원솔르 첫 번째 인덱스부터 차례로 확인하면서 A의 원소가 B의 원소보다 작을 때에만 교체를 수행한다.
# 이 문제에서는 두 배열의 원소가 최대 100,000개까지 입력될 수 있으므로, 최악의 경우 O(NlogN)을 보장하는 정렬 알고리즘을 이용해야한다.
n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

for i in range(k):
    # a의 원소가 b의 원소보다 작은경우
    if a[i] < b[i]:
        # 두 원소를 교체
        a[i], b[i] = b[i], a[i]
    else:
        break

print(sum(a))

# 내가 문제를 풀 때에는 sort()가 k번 반복하게 되었는데 b를 reverse=True로 변경하여 sort()를 한번 사용하도록 한 것을 볼 수 있다!
