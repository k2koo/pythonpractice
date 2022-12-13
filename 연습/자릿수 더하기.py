#https://school.programmers.co.kr/learn/courses/30/lessons/120906
def solution(n):
    answer = 0
    return sum([int(x) for x in str(n)])
  
  def solution(n):
    answer = 0
    while n:
        answer += n%10
        n //= 10
    return answer
  
  answer = 0
    while n:
        n, r = divmod(n, 10)
        answer += r
    return answer
