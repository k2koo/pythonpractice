#https://school.programmers.co.kr/learn/courses/30/lessons/120885?language=python3

def solution(bin1, bin2):
    answer = ''
    a = int(bin1, 2)
    b = int(bin2, 2)
    answer = bin(a+b)
    return answer[2:]
