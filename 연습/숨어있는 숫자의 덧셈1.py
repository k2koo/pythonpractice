#https://school.programmers.co.kr/learn/courses/30/lessons/120851
def solution(my_string):
    answer = 0
    return sum([int(x) for x in my_string if x.isdigit()])

  def solution(my_string):
    answer = 0
    for c in my_string:
        if c.isnumeric():
            answer += int(c)
    return answer

  def solution(my_string):
    return sum(map(int, filter(lambda x: x.isdigit(), my_string)))
