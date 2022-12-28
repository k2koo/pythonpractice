#https://school.programmers.co.kr/learn/courses/30/lessons/120913

def solution(my_str, n):
    return [my_str[x:x+n] for x in range(0, len(my_str), n)]
  
  answer = [my_str[i*n:(i+1)*n] for i in range((len(my_str)-1)//n+1)]
    return answer
  
    answer = []

    temp, idx = '', 0
    for c in my_str:
        temp += c
        idx += 1

        if idx % n == 0:
            answer.append(temp)
            temp = ''

    if temp:
        answer.append(temp)

    return answer
