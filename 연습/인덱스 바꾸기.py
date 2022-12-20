#https://school.programmers.co.kr/learn/courses/30/lessons/120895

def solution(my_string, num1, num2):
    var1, var2 = my_string[num1], my_string[num2]
    string = list(my_string)
    string[num1], string[num2] = var2, var1

    return ''.join(string)

    s = list(my_string)
    s[num1],s[num2] = s[num2], s[num1]
    
    return ''.join(s)
