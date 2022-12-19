#https://school.programmers.co.kr/learn/courses/30/lessons/120815

def solution(n):
    a = 1 
    while (a*6) % n != 0 :
        a += 1
    return a
  
  import math

def solution(n):
    return (n * 6) // math.gcd(n, 6) // 6
  
  def solution(n):
    i=1
    while(1):
        if (6*i)%n==0:
            return i
        i+=1
  
