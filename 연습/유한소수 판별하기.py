#https://school.programmers.co.kr/learn/courses/30/lessons/120878
from math import gcd
def solution(a, b): #int -> int
    b //= gcd(a,b)
    while b%2==0:
        b//=2
    while b%5==0:
        b//=5
    return 1 if b==1 else 2
 ########################################################################################
  def gcd(a, b): #최대공약수(유클리드 호제법)
    if a % b == 0:
        return b
    else:
        return gcd(b, a%b)

def factorization(x): #소인수분해
    d = 2
    output = []
    
    while d <= x:
        if x % d == 0:
            output.append(d)
            x /= d
        else:
            d += 1
            
    return output
    
def solution(a, b):
    divide_num = gcd(b, a)
    result = b // divide_num
    
    for num in factorization(result):
        if num not in [2, 5]:
            return 2
    return 1
