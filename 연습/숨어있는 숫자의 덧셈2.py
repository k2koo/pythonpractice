#https://school.programmers.co.kr/learn/courses/30/lessons/120864

answer = 0
    num = ''

    for x in my_string:
        if x.isdigit():
            num += x
        else:
            if num:
                answer += int(num)
                num = ''

    if num.isdigit():
        answer += int(num)

    return answer #정규식 안쓰기
  
  s = ''.join(i if i.isdigit() else ' ' for i in my_string)
    return sum(int(i) for i in s.split())
  
  import re

def solution(my_string):
    return sum([int(i) for i in re.findall(r'[0-9]+', my_string)])
  
  import re

def solution(my_string):
    return sum(map(int, re.findall(r"\d+", my_string)))
