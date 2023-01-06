#https://school.programmers.co.kr/learn/courses/30/lessons/120860

def solution(dots: list) -> int:
    sorted_dots = sorted(dots, key=lambda x: (x[0], x[1]))
    x_length = sorted_dots[2][0] - sorted_dots[0][0]
    y_length = sorted_dots[1][1] - sorted_dots[0][1]

    return x_length * y_length

if __name__ == '__main__':
    print(solution([[1, 1], [2, 1], [2, 2], [1, 2]]))  # 1
    print(solution([[-1, -1], [1, 1], [1, -1], [-1, 1]]))  # 4
    
    def solution(dots):
    x_dot = [dot[0] for dot in dots]
    y_dot = [dot[1] for dot in dots]
    answer = (max(x_dot) - min(x_dot)) * (max(y_dot) - min(y_dot))
    
    return answer
  
  
def solution(dots):
    return (max(dots)[0] - min(dots[0])) * (max(dots)[1] - min(dots)[1])
