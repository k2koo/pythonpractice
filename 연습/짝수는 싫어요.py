#https://school.programmers.co.kr/learn/courses/30/lessons/120813

def solution(n):
    answer = [x for x in range (1, n+1) if x % 2 == 1]
    return answer
