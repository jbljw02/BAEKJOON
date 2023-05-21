#### 5단계 ####

# 5-1
# S = list(input())
# i = int(input())
# print(S[i-1])

# 5-2
# S = list(input())
# print(len(S))

# 5-3
# T = int(input())
# S1 = list(input())
# S2 = list(input())
# S3 = list(input())
# for i in range(T):
#     print(S1[0] + S1[len(S1)-1])
#     print(S2[0] + S2[len(S2)-1])
#     print(S3[0] + S3[len(S3)-1])

# 5-4
# S = input()
# print(ord(S))

# 5-5
# N = int(input())
# a = list(map(int, input()))
# result = 0
# for i in range(N):
#     result += a[i]
# print(result)

# 5-6
# from string import ascii_lowercase
# alphabet = ascii_lowercase
# S = list(input())
# for i in alphabet:
#     if i in S:
#         print(S.index(i), end=' ')
#     else:
#         print(-1, end=' ')

# 5-7
# T = int(input())
# for i in range(T):
#     R, S = input().split()
#     list_s = list(S)
#     int_r = int(R)
#     result = ''
#     for i in range(len(list_s)):
#         result = list_s[i] * int_r
#         print(result, end='')
#     print()
