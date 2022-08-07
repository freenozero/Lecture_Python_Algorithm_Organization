stack = []

#삽입(5)-삽입(2)-삽입(3)-삽입(7)-삭제()-삽입(1)-삽입(4)-삭제()
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop() #첫 번째 삭제
print(stack[::-1]) #최상단 원소부터 출력
print(stack) #최하단 원소부터 출력
stack.append(1)
stack.append(4)
stack.pop() #두 번째 삭
print(stack[::-1]) #최상단 원소부터 출력
print(stack) #최하단 원소부터 출력

#append와 pop의 함수의 시간복잡도는 상수시간이며 스택자료구조에 활용하기 쉬움.
