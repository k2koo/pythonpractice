#https://school.programmers.co.kr/learn/courses/30/lessons/120888
from collections import OrderedDict

def solution(my_string):
    answer = ''.join(OrderedDict.fromkeys(my_string))
    return answer

def solution(my_string):
    answer = ''
    for i in my_string:
        if i not in answer:
            answer+=i
    return answer
