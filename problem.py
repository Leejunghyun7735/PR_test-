# T = int(input())
# A, B = map(int, input().split())

# for i in range(T):

#     print(A+B)

# price = ['20180728', 100, 130, 140, 150, 160, 170]

# del price[0]
# print(price)

# print(price[1::])


# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(nums[::-1])

# interest = ['삼성전자', 'LG전자', 'Naver']
# print('\n'.join(interest))


# string = "삼성전자/LG전자/Naver"

# interest = string.split("/")

# print(interest)
# b = 2
# print(id(2))

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # del nums[1:3]

# print(nums[0:2] + nums[4:6])

# num = 0

# while num <= 5:
#     print(num+1)
#     num = num + 1

# ##############################

# num = 0

# while num <= 5:
#     num = num + 1
#     print(num+1)


# def 별찍기():
#     print("*" * 30)
#     print(" ")
#     print("*" * 30)


# 별찍기()

###################################

T = int(input())

for i in range(T):
    a = input()
    print(a[0]+a[-1])

###################################

#1
arr = [1, 1, 3, 3, 0, 1, 1,5,5,3,1,6,9,7,7,7,7,7,7,7,7]
answer = [arr[0]]

for i in arr:
    if not i == answer[-1]:
        answer.append(i)

print(answer)

###################################

def solution(arr):
    answer = [arr[0]]
    for i in arr:
        if not i == answer[-1]:
            answer.append(i)
    print(answer)
        
solution(arr)


#######################################


arr = [1, 1, 3, 3, 0, 1, 1]
answer = [arr[0]]

for i in arr:
    if not i == answer[-1]:
        answer.append(i)

print(answer)



arr = [1, 1, 3, 3, 0, 1, 1]
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

