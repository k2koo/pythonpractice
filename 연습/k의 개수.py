#https://school.programmers.co.kr/learn/courses/30/lessons/120887

#def solution(i, j, k):
    answer = 0
    
    for x in range(i, j+1):
        answer += sum([1 for x in list(str(x)) if x == str(k)])
        
    return answer
  
  answer = sum([str(i).count(str(k)) for i in range(i,j+1)])
  
  return sum(map(lambda v: str(v).count(str(k)), range(i,j+1)))
