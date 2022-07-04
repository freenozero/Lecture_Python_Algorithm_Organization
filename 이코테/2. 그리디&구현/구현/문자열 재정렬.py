#알파벳 대문자와 숫자(0~9)로만 구성된 문자열이 입력으로 주어집니다.
#이때 모든 알파벳을 오름차순으로 이어서 출력한 후에 그 뒤에 모든 숫자를 더한 값을 이어서 출력한다.
#입력예시1: K1KA5CB7, 출력예시1:ABCKK13
#입력예시2:AJKDLSI412K4JSJ9D, 출력예시2: ADDIJJJKKLSS20

#문제 풀이
input_datas = input()
datas_sum = 0
output_data = []
for input_data in input_datas:
    if (ord(input_data) >= 48 and ord(input_data) <= 57):
        datas_sum += int(input_data)
    else:
        output_data.append(input_data)
output_data.sort()
output_data.append(str(datas_sum))
print(''.join(output_data))

#답안 예시
data = input()
result = []
value = 0

for x in data:
    if x.isalpha():
        result.append(x)
    else:
        value += int(x)
result.sort()

if value != 0:
    result.append(str(value))

print(''.join(result))
