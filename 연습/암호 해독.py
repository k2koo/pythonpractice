https://school.programmers.co.kr/learn/courses/30/lessons/120892

def solution(cipher, code):
    answer = cipher[code-1::code]
    return answer
  
  def solution(cipher, code):
    return ''.join(map(str, [x for index, x in enumerate(cipher, start=1) if index % code == 0]))
