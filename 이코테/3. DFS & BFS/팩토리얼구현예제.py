#n! = 1 * 2 * 3 * ... * (n-1) * n
#수학적으로 0!과 1!의 값은 1이다.

#반복적으로 구현한 n!
def factorial_iterative(n):
    result = 1
    #1부터 n까지의 수를 차례대로 곱하기
    for i in range(1, n+1):
        result *= i
    return result

def factorial_reCursive(n):
    if n<=1:
        return 1
    #n! = n*(n-1)!을 그대로 코드 작성
    return n * factorial_reCursive(n-1)

print('반복적으로 구현:',factorial_iterative(5))
print('재귀적으로 구현:',factorial_reCursive(5))
