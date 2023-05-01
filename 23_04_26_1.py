# # 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/86491

sizes = [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]

# 1
def solution(sizes):
    answer = [] # 작은 값만 모아서 리스트를 새로 생성
    for w, h in sizes:
        if w < h:
            answer.append(w)
        else:
            answer.append(h)

    a = max(sum(sizes, [])) # sum(sizes, []) 리스트 안에 리스트를 풀어서 한 리스트 생성 / 가장 큰 값을 뽑아내겠다.
    b = max(answer) # 작은 값 중에 큰 값을 뽑아내겠다.
    return a*b

print(solution(sizes))


#3
def solution(sizes):
    answer = max(max(x) for x in sizes) * max(min(x) for x in sizes)
    return answer

print(solution(sizes))


# 2
def solution(sizes):
    answer = 0
    w = 0
    h = 0
    for i in sizes:
        w = max(w, max(i))
        h = max(h, min(i))
    answer = w * h
    return answer

print(solution(sizes))

