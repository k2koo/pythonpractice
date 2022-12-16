#https://school.programmers.co.kr/learn/courses/30/lessons/120850

def solution(my_string):
    return sorted([int(x) for x in my_string if x.isdigit()])
  
  string indices must be integer 이기 때문에 int(x)로 바꿔서 사용 
