#https://school.programmers.co.kr/learn/courses/30/lessons/120845

def solution(box, n):
    answer = (box[0] // n) * (box[1] // n) * (box[2] // n)
    return answer
  
  def solution(box, n):
    answer = 1
    for b in box:
        answer *= b // n
    return answer
