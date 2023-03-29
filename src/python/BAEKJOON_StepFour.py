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
# i, j, k = map(int, input().split())
#
# a = 0
# one = []
# two = []
# three = []
# four = []
# five = []
#
# for a in range(1, M+1):




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
# list_remain = []
# for i in range(10):
#     n = int(input())
#     list.append(n)
#
#     remain = n % 42
#     list_remain.append(remain)
#
# result = 0
# j = 0
# for i in range(list_remain):
#     for k in i:
#         if list_remain[j] == k:
#             result += 1
#         j += 1
#
# print(result)

list = [1,2,3,4]
for i in list:
    print(i)
