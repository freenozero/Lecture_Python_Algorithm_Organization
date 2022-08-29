array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i  # 가장 작은 원소의 인덱스
    # i는 array 끝까지, j는 i+1부터 array 끝까지 돈다.
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:  # 가장 작은 원소의 인덱스가 j보다 클경우!
            min_index = j  # 가장 작은 원소의 인덱스가 j로 변경된다..!
            # 이 상황을 반복하면, 가장 작은 원소의 인덱스가 min_index가 된다..
    array[i], array[min_index] = array[min_index], array[i]
print(array)
