#각 자리가 숫자(0~9)로만 이루어진 문자열이 주어졌을 떄,
#왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하며 숫자 사이에 곱하기 또는 더하기 연산자를 넣어 만들어질 수
#있는 가장 큰 수를 구하는 프로그램을 작성하시오
#단, +보다 x가 먼저 계산되는 방식이 아닌 모든 연산은 왼쪽에서부터 순서대로 이루어지는 방식이다.
#ex) 02984라는 문자열일 경우에 ((((0+2)*9)*8)*4) = 576이다.

#직접 풀기 1
##S = list(input("문자열:"))
##result = 0
##for i in range(len(S)):
##    if ((result + int(S[i])) >= (result * int(S[i]))): #덧셈이 더 크면
##        result += int(S[i])
##    else:
##        result *= int(S[i])
##print(result)

#직접풀기 2
##S = list(input("문자열:"))
##result = int(S[0])
##for i  in range(1, len(S)):
##    if (result == 1 or result == 0 or int(S[i]) == 0 or int(S[i]) == 1):
##        result += int(S[i])
##    else:
##        result *= int(S[i])
##print(result)


#풀이 == 직접 풀이2
data = input()
result = int(data[0])

for i in range(1, len(data)):
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num
print(result)
            
