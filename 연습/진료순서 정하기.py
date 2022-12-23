#https://school.programmers.co.kr/learn/courses/30/lessons/120835

def solution(emergency):
    answer = []
    dict = {num: index for index, num in enumerate(sorted(emergency, reverse=True), start=1)}
    
    return [dict[x] for x in emergency]
 
def solution(emergency):
    return [sorted(emergency, reverse=True).index(a) + 1 for a in emergency]
    #응급도를 내림차순으로 정렬한뒤 index(위치 확인) 을통해 1씩 추가하는 방법으로 풀이
