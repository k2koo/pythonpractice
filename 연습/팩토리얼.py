#https://school.programmers.co.kr/learn/courses/30/lessons/120848

def solution(n):
    d = [0] * 3628801  # dp table 할당
    d[1], result = 1, 1

    while True:
        if d[result] > n:
            return result - 1

        result += 1
        d[result] = result * d[result-1]
        
        from math import factorial

def solution(n):
    k = 10
    while n < factorial(k):
        k -= 1
    return k
