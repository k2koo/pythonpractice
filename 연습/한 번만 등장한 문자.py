#https://school.programmers.co.kr/learn/courses/30/lessons/120896
def solution(s):
    answer = ''
    dict = {}
    
    for x in s:
        if x not in dict:
            dict[x] = 1 #처음
        else:
            dict[x] += 1 #나오면 하나씩 추가
    
    for x in dict:
        if dict[x] ==1:
            answer += x
    
    return ''.join(map(str, sorted(answer)))

    answer = ''.join(sorted([ ch for ch in s if s.count(ch)==1]))
    
    
    
