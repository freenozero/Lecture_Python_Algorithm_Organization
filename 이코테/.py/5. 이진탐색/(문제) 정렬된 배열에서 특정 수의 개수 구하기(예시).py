from bisect import bisect_left, bisect_right
import time

# 측정 시작
start_time = time.time()


def count_by_range(array, left_value, right_value):
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array, left_value)
    return right_index - left_index


n, x = map(int, input().split())
array = list(map(int, input().split()))

# 값이 [x, x] 범위에 있는 데이터의 개수 계산
count = count_by_range(array, x, x)

if count == 0:
    print(-1)
else:
    print(count)


# 측정 종료
end_time = time.time()
# 수행 시간 출력
print('함수에 넣은거 성능 측정:', end_time - start_time)

# 내가 문제를 풀 때에는 함수로 만들지 않았는데, 함수로 만들어진 것을 볼 수 있다.
# 해당 문제는 시간 복잡도 O(logN)이기에 함수에 넣지 않으면 시간 초과 판정을 받나보다..! 싶었는데
# 수행 시간 측정해보니까 풀어쓴게 더 빠르고, 2.2 정도 차이난다.
