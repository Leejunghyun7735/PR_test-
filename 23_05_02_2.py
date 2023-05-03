# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/181841

str_list = ["abc", "def", "ghi"]
ex = "ef"

# str_list =["abc", "bbc", "cbc"]
# ex ="c"

def solution(str_list, ex):
    answer = []
    for i in str_list:
        if ex not in i:
            answer.append(i)
    print(answer)
    print("".join(answer))

solution(str_list, ex)



