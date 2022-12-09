#https://school.programmers.co.kr/learn/courses/30/lessons/120841?language=python3

def solution(dot):
    answer = 0
    if dot[0] > 0 and dot [1] > 0:
        answer = 1
    elif dot[0] > 0 and dot[1] < 0:
        answer = 4
    elif dot[0] < 0 and dot[1] > 0:
        answer = 2
    else:
        answer = 3
    return answer
    
    def solution(dot):
    a, b = 1, 0
    if dot[0]*dot[1] > 0:
        b = 1
    if dot[1] < 0:
        a = 2
    return 2*a-b
    
def solution(dot):
    quad = [(3,2),(4,1)]
    return quad[dot[0] > 0][dot[1] > 0]
