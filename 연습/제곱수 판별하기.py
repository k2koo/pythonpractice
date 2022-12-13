#https://school.programmers.co.kr/learn/courses/30/lessons/120909

def solution(n):
    answer = 0
    x = n ** (1/2)
    if x % 1 == 0 :
        answer = 1
    else :
        answer = 2 
    return answer
  
  def solution(n):
    if n**(1/2) == int(n**(1/2)) :
        return 1
    else :
        return 2
      
제곱에 대한 표현
from math import sqrt

def solution(n: int) -> int:
    return 1 if sqrt(n) == int(sqrt(n)) else 2
