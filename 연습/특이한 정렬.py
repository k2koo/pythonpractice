#https://school.programmers.co.kr/learn/courses/30/lessons/120880

def solution(numlist: list, n: int) -> list:
    return sorted(numlist, key=lambda x: (abs(n-x), -x))
