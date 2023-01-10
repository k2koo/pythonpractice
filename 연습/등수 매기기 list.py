#https://school.programmers.co.kr/learn/courses/30/lessons/120882
def solution(score: list) -> list:
    dict, avg_list = {}, [sum(num) / 2 for num in score]

    for index, avg in enumerate(sorted(avg_list, reverse=True), start=1):
        if avg not in dict:
            dict[avg] = index

    return [dict[avg] for avg in avg_list]
  
  # 등수 계산 함수
    def rank(x, avg):
        return len([v for v in avg if v > x])+1

    # 평균 리스트
    avg = [sum(student)/len(student) for student in score]
    # 등수로 매핑
    return list(map(lambda x: rank(x, avg), avg))
