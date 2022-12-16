#https://school.programmers.co.kr/learn/courses/30/lessons/120823
n = int(input())
for i in range(n) :
    for j in range(n):
        if(j<=i):
            print("*", end="")
    print()

    n = int(input())
for i in range(n):
    print('*'*(i+1))
    
    n = int(input())
for i in range(n):
    print("*" * (i + 1))
