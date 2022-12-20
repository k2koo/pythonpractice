#https://school.programmers.co.kr/learn/courses/30/lessons/120862

def solution(numbers):
    answer = 0
    nums_sort = sorted(numbers)
    
    return max(nums_sort[-1] * nums_sort[-2], nums_sort[0] * nums_sort[1])
  #절댓값이 안되니 앞에랑 뒤에중 뭐가 더 큰건지 비교
