#https://school.programmers.co.kr/learn/courses/30/lessons/120891

def solution(order):
    answer = 0
    return sum([1 for x in str(order) if x in ['3','6','9']] )
  
  return sum(map(lambda x: str(order).count(str(x)), [3, 6, 9]))

 answer = 0
    order = str(order)
    return order.count('3') + order.count('6') + order.count('9')
  
  return len(list(filter(lambda v: int(v) in [3, 6, 9], [int(n) for n in str(order)])))
