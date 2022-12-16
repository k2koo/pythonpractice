#https://school.programmers.co.kr/learn/courses/30/lessons/120837

def solution(hp):
    answer = 0
    a = hp // 5
    b = (hp % 5) // 3
    c = (hp % 5) % 3
    answer = a + b + c
    
    return answer
  
  def solution(hp):    
    return hp // 5 + (hp % 5 // 3) + ((hp % 5) % 3)
  
  def solution(hp):
    answer = 0
    for ant in [5, 3, 1]:
        d, hp = divmod(hp, ant)
        answer += d
    return answer
  
  divmod = 
