# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/87389

def solution(n):
    x = 2
    while n % x != 1:
        x += 1
    return x

solution(10)

# def solution(n):
#     for x in range(1,n):
#         if n%x==1:
#             return x

# print(solution(13))