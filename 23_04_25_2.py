# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/12906

arr = [1, 1, 3, 3, 0, 1, 1]


#1
answer = []

for i in arr:
    if i not in answer:
        answer.append(i)

print(answer)


#2 
def solution(arr):
    answer = set(arr)
    print(answer)

solution(arr)


#3
# answer = [arr[0]]

# for i in arr:
#     if not i == answer[-1]:
#         answer.append(i)

# print(answer)


def solution(arr):
    answer = [arr[0]]
    for i in arr:
        if not i == answer[-1]:
            answer.append(i)
    print(answer)
        
solution(arr)