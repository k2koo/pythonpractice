#https://school.programmers.co.kr/learn/courses/30/lessons/120846

def solution(n):
    result = 0

    for x in range(4, n+1):
        num = 0
        for y in range(1, x+1):
            if num == 2:
                result += 1
                break
            if x % y == 0:
                num += 1

    return result
  
  def solution(n):
    output = 0
    for i in range(4, n + 1):
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                output += 1
                break
    return output

  def get_divisors(n):
    return list(filter(lambda v: n % v ==0, range(1, n+1)))

def solution(n):
    return len(list(filter(lambda v: len(get_divisors(v)) >= 3, range(1, n+1))))

  def solution(n):
    answer = 0
    for i in range(3,n+1) :
        temp = 1
        for j in range(1,i) :
            if i % j == 0 :
                temp += 1

        if temp > 2 :
            answer += 1
    return answer
