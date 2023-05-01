# 문제 : https://www.acmicpc.net/problem/2908

a, b = input().split()
a = int(a[::-1])
b = int(b[::-1])

# 1
print(max(a, b))

# 2
if a > b:
    print(a)
else:
    print(b)