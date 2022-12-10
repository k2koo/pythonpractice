#https://school.programmers.co.kr/learn/courses/30/lessons/120816

def solution(slice, n):
    answer = 0
    if n % slice == 0 :
        answer = n // slice
    else :
        answer = n // slice + 1
    
    return answer
  
def solution(slice, n):
    return ((n - 1) // slice) + 1
