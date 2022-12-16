#https://school.programmers.co.kr/learn/courses/30/lessons/120905

def solution(n, numlist):
    answer = []
    return [int(x) for x in numlist if x % n == 0]
  
  def solution(n, numlist):
    return list(filter(lambda v: v%n==0, numlist))

  def solution(n, numlist):
    answer = [i for i in numlist if i%n==0]
    return answer
