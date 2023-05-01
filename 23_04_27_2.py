# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/12950

arr1 = [[1, 2], [2, 3]]
arr2 = [[3, 4], [5, 6]]
# arr3 = [[arr1[0][0]+arr2[0][0], arr1[0][1]+arr2[0][1]],
#         [arr1[1][0]+arr2[1][0], arr1[1][1]+arr2[1][1]]]

# arr1 = [[1], [2]]
# arr2 = [[3], [4]]
# arr3 = [[arr1[0][0]+arr2[0][0]],[arr1[1][0]+arr2[1][0]]]

def solution(arr1, arr2):
    answer = []    
    for i in range(len(arr1)):
        arr3 = []
        for j in range(len(arr1[i])):
            arr3.append(arr1[i][j]+arr2[i][j])
        answer.append(arr3)
    return(answer)
solution(arr1, arr2)
