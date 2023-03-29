#### 3단계 ####

# 3-1
# N = int(input())
# for i in range(1,10):
#     print(str(N) + " * " + str(i) + " = " + str(N * i))

# 3-2
# T = int(input())
# i = 1
# C = []
# while i <= T:
#     A, B = map(int, input().split())
#     C.append(A+B)
#     print(C[i-1])
#     i += 1

# 3-2
# n = int(input())
# i = 1
# a = 0
# while i <= n:
#     a += i
#     i += 1
# print(a)

# 3-3
# X = int(input())
# N = int(input())
# result = 0
# result_sum = 0
# for i in range(1, N+1):
#     a, b = map(int, input().split())
#     result = a * b
#     result_sum += result
# if result_sum == X:
#     print("Yes")
# else:
#     print("No")

# 3-4
# N = int(input())
# for i in range(1, N+1):
#     if i % 4 == 0:
#         print("long", end=" ")
# print("int")

# 3-5
# import sys
# T = int(input())
# result = 0
# for i in range(1, T+1):
#     A,B = map(int, sys.stdin.readline().split())
#     result = A + B
#     print(result)

# 3-6
# T = int(input())
# result = 0
# for i in range(1, T+1):
#     A,B = map(int, input().split())
#     result = A + B
#     print("Case #" + str(i) + ": " + str(result))

# 3-7
# T = int(input())
# result = 0
# for i in range(1, T+1):
#     A,B = map(int, input().split())
#     result = A + B
#     print("Case #" + str(i) + ": " + str(A) + " + " + str(B) + " = " + str(result))

# 3-8
# N = int(input())
# for i in range(1, N+1):
#     for k in range(1, i+1):
#         print('*', end="")
#     print('')

# 3-9


# 3-8
# while True:
#     A, B = map(int, input().split())
#     if A == 0 and B == 0:
#         break
#     C = A + B
#     print(C)

# 3-9
# while True:
#     try:
#         A, B = map(int, input().split())
#         C = A + B
#         print(C)
#     except EOFError:
#         break






