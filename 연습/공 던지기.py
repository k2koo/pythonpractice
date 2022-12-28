#https://school.programmers.co.kr/learn/courses/30/lessons/120843

def solution(numbers, k):
     return numbers[(k-1) * 2 % len(numbers)]
  
  
