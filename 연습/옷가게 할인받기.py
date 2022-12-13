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
  
    def solution(price):
    discount_rates = {500000: 0.8, 300000: 0.9, 100000: 0.95, 0: 1}
    for discount_price, discount_rate in discount_rates.items():
        if price >= discount_price:
            return int(price * discount_rate)
  
