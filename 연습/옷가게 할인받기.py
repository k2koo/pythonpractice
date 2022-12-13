#https://school.programmers.co.kr/learn/courses/30/lessons/120818

def solution(price):
    answer = 0
    if price >= 500000 :
        answer = int(price * 0.8)
    elif price >= 300000 :
        answer = int(price * 0.9)
    elif price >= 100000 :
        answer = int(price * 0.95 )
    else :
        answer = price
    return answer
  
  
