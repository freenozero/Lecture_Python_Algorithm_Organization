from bisect import bisect_left, bisect_right
import time

# 측정 시작
start_time = time.time()

N, x = map(int, input().split())
array = list(map(int, input().split()))

left_index = bisect_left(array, x)
right_index = bisect_right(array, x)

if right_index > left_index:
    print(right_index - left_index)
else:
    print(-1)

# 측정 종료
end_time = time.time()
# 수행 시간 출력
print('풀어쓴거 정렬 성능 측정:', end_time - start_time)
