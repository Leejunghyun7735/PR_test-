# 문제 : https://www.acmicpc.net/problem/25305

# # N, k = input().split()
# x = map(int,input().split())

# print(x)

n,k = map(int,input().split())
x = list(map(int,input().split()))
x.sort()
a=x[-k]
print(a)