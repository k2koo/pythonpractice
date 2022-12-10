#https://school.programmers.co.kr/learn/courses/30/lessons/120889

def solution(sides):
    answer = sides.sort()
    if sides[0] + sides[1] <= sides[2] :
        answer = 2
    else:
        answer = 1
    
    return answer
  
  def solution(sides):
    return 1 if max(sides) < (sum(sides) - max(sides)) else 2
