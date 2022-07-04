#정원은 8x8 좌표 평면이다.
#나이트는 L자 형태로만 이동할 수 있고, 정원은 나갈 수 없다. 아래의 방법으로만 이동가능하다.
#1. 수평으로 두 칸 이동한 뒤에 수직으로 한 칸 이동하기
#2. 수직으로 두 칸 이동한 뒤에 수평으로 한 칸 이동하기
#나이트가 이동할 수 있는 경우의 수를 출력하시오
#행 위치를 표현할 때는 1부터 9로 표현하며, 열의 위치는 a부터h로 표현한다.
#EX)  c2에 있을 때 이동할 수 있는 경우의 수는 6가지이다.
#EX) a1에 있을 때 이동할 수 있는 경우의 수는 2가지이다.

#입력 조건은 위치한 좌표: a1
#출력 조건은 이동할 수 있는 경우의 수: 2
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int (ord('a')) + 1
steps = [(-2 , -1), (-1 , -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]
 
result = 0
for step in steps:
    next_row = row+ step[0]
    next_column = column + step[1]

    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <=8:
        result += 1

print(result)
