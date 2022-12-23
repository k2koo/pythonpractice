#https://school.programmers.co.kr/learn/courses/30/lessons/120842

def solution(num_list, n):
    answer = [[]]
    return [num_list[x:x+n] for x in range(0, len(num_list), n)]
  
  def solution(num_list, n):
    return [num_list[ix-n:ix] for ix in range(n, len(num_list)+1, n)]
  
  
