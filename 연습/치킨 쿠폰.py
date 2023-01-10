#https://school.programmers.co.kr/learn/courses/30/lessons/120884

def solution(chicken):
    answer = 0
    if len(str(chicken)) == 7:
        answer = 111111
    elif len(str(chicken)) == 6:
        answer = (chicken // 10) + (chicken // 10) // 10 + (chicken // 10) // 10 // 10 + (chicken // 10) // 10 // 10 // 10 + (chicken // 10) // 10 //10 // 10 // 10 + sum([int(x) for x in str(chicken)]) // 10 + (sum([int(x) for x in str(chicken)]) % 10 + sum([int(x) for x in str(chicken)]) // 10) // 10
    elif len(str(chicken)) == 5:
        answer = (chicken // 10) + (chicken // 10) // 10 + (chicken // 10) // 10 // 10 + (chicken // 10) // 10 // 10 // 10 + sum([int(x) for x in str(chicken)]) // 10 + (sum([int(x) for x in str(chicken)]) % 10 + sum([int(x) for x in str(chicken)]) // 10) // 10
    elif len(str(chicken)) == 4:
        answer = (chicken // 10) + (chicken // 10) // 10 + (chicken // 10) // 10 // 10 + sum([int(x) for x in str(chicken)]) // 10 + (sum([int(x) for x in str(chicken)]) % 10 + sum([int(x) for x in str(chicken)]) // 10) // 10
    elif len(str(chicken)) == 3:
        answer = (chicken // 10) + (chicken // 10) // 10+ sum([int(x) for x in str(chicken)]) // 10 + (sum([int(x) for x in str(chicken)]) % 10 + sum([int(x) for x in str(chicken)]) // 10) // 10
    elif len(str(chicken)) == 2:
        answer = chicken // 10 + sum([int(x) for x in str(chicken)]) // 10 + (sum([int(x) for x in str(chicken)]) % 10 + sum([int(x) for x in str(chicken)]) // 10) // 10
    else:
        answer = 0
    return answer 
    
def solution(chicken: int) -> int:
    answer = 0
    coupon = chicken

    while coupon >= 10:
        eaten = coupon // 10
        answer += eaten
        coupon = coupon % 10 + eaten

    return answer
    
    def solution(chicken):
    answer = 0
    while chicken >= 10:
        chicken, mod = divmod(chicken,10)
        answer += chicken
        chicken += mod
    return answer
