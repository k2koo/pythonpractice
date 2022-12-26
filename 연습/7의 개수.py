#https://school.programmers.co.kr/learn/courses/30/lessons/120912

def solution(array):
    answer = ""
    for i in array : #배열로 된 array의 값을 str(문자열)로 가져와 answer에 추가
        answer +=str(i)
    
    return answer.count("7") #그중에 7의 개수를 구함
  
  return "".join(map(str, array)).count('7')
        #map함수로 배열로 받은 array를 str로 변환
  
  return str(array).count('7')

#map(function, iterable)
