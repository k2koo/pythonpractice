#https://school.programmers.co.kr/learn/courses/30/lessons/120833?language=python3
#배열 자르기
def solution(numbers, num1, num2):
    answer = numbers[num1:num2+1]
    return answer

def solution(numbers, num1, num2):
    answer=[]
    for i in range(num1,num2+1):
        answer.append(numbers[i])
    return answer
