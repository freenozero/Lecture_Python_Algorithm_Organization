# N = 떡의 개수 & M = 요청한 떡의 길이
N, M = map(int, input().split())

# 떡의 개별 높이
H = list(map(int, input().split()))


def search_tteok(H, M):
    end = max(H)  # 가장 긴 떡볶이 떡을 끝 점으로 설정
    start = 0  # 첫번 쨰 점을 0으로 설정
    mid = (start + end) // 2  # 중간점을 end와 start 점 중앙으로 설정

    while (True):
        tteok = 0
        mid = (start + end) // 2
        for i in range(len(H)):
            if H[i] - mid >= 0:
                tteok += H[i] - mid

        if tteok > M:
            start = mid + 1
            continue

        elif tteok < M:
            end = mid - 1
            continue

        else:
            return mid


# 떡 N개를 이진탐색으로 잘라 보면서 맞추기?
mid = search_tteok(H, M)
print(mid)
