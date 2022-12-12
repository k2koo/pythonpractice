#https://school.programmers.co.kr/learn/courses/30/lessons/120836

def solution(n):
    answer = sum([1 for x in range(1, n+1) if n % x == 0])
    return answer
  
  def solution(n):
    return len(list(filter(lambda v: n % (v+1) == 0, range(n))))
  
  #람다 연습
