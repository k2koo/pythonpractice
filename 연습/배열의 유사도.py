#https://school.programmers.co.kr/learn/courses/30/lessons/120903

def solution(s1, s2):
    answer = len(list(set(s1) & set(s2)))
    return answer
  
  리스트를 집합화 하고 교집합을 구하고 다시 리스트화 그리고 길이 구하기 
