#https://school.programmers.co.kr/learn/courses/30/lessons/120904
def solution(num, k):
    answer = 0
    return str(num).index(str(k)) + 1 if str(k) in str(num) else -1
    
    return -1 if str(k) not in str(num) else str(num).find(str(k)) + 1
