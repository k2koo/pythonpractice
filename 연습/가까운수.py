#https://school.programmers.co.kr/learn/courses/30/lessons/120890


array.sort()
    temp = []

    for i in array :
        temp.append( abs(n-i) )

    return array[temp.index(min(temp))]
  
  solution=lambda a,n:sorted(a,key=lambda x:(abs(x-n),x))[0]


 answer = 0
    return array[sorted([[index, abs(n-num), num] for index, num in enumerate(array)], key=lambda x: (x[1], x[-1]))[0][0]]
