#https://school.programmers.co.kr/learn/courses/30/lessons/120825?language=python3

def solution(my_string, n):
    answer = ''
    for i in my_string:
        answer += i*n
    return answer
