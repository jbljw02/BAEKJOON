#### 4단계 ####

# # 4-1
# N = int(input())
# a = list(map(int, input().split()))
# v = int(input())
# if v in a:
#     print(a.count(v))
# else:
#     print(a.count(v))

# 4-2
# N, X = map(int, input().split())
# A = list(map(int, input().split()))
# B = []
# for i in range(0, len(A)):
#     B.append(A[i])
#     if B[i] < X :
#         print(B[i], end=' ')

# 4-3
# N = int(input())
# A = list(map(int, input().split()))
# print(min(A), max(A))

# 4-4
# list = []
# for i in range(9):
#     a = int(input())
#     list.append(a)
# print(max(list))
# print(list.index(max(list))+1)

# 4-5
# N, M = map(int, input().split())
# basket = [0] * (N+1)
# for _ in range(M):
#     i,j,k = map(int, input().split())
#     for n in range(i, j+1):
#         basket[n] = k
# for i in range(1, N+1):
#     print(basket[i], end = ' ')

# 4-6
# N, M = map(int, input().split())
# basket = []
# for i in range(1, N+1):
#     basket.append(i)
# for _ in range(M):
#     i, j = map(int, input().split())
#     basket[i-1], basket[j-1] = basket[j-1], basket[i-1]
# for i in range(len(basket)):
#     print(basket[i], end = ' ')

# 4-7
# students = []
# for i in range(1,31):
#     students.append(i)
# students_report = []
# for i in range(28):
#     n = int(input())
#     students_report.append(n)
# students_report_not = list(set(students) - set(students_report))
# print(min(students_report_not))
# print(max(students_report_not))

# 4-8
# list = []
# count = {}
# for i in range(10):
#     n = int(input())
#     value = n % 42
#     list.append(value)
# list = set(list)
# print(len(list))

# 4-9
# N, M = map(int, input().split())
# basket = []
# for a in range(1, N+1):
#     basket.append(a)
# for b in range(M):
#     i, j = map(int, input().split())
#     temp = basket[i-1:j]
#     temp.reverse()
#     basket[i-1:j] = temp
# for c in range(N):
#     print(basket[c], end=' ')

# 4-10
# N = int(input())
# score = list(map(int, input().split()))
# maxScore = max(score)
# update_score = []
# for i in range(len(score)):
#     update_score.append(score[i] / maxScore * 100)
# print(sum(update_score)/len(update_score))



