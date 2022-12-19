#https://school.programmers.co.kr/learn/courses/30/lessons/120844

def solution(numbers, direction):
    answer = []
    return numbers[1:] + [numbers[0]] if direction == 'left' else [numbers[-1]] + numbers[:-1]
