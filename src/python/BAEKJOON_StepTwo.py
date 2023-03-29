#### 2단계 ####

# 2-1
# A, B = map(int, input().split())
# if A > B:
#     print(">")
# if A < B:
#     print("<")
# if A == B:
#     print("==")

# 2-2
# a = int(input())
# if 90 <= a <= 100:
#     print("A")
# elif 80 <= a <= 89:
#     print("B")
# elif 70 <= a <= 79:
#     print("C")
# elif 60 <= a <= 69:
#     print("D")
# else:
#     print("F")

# 2-3
# a = int(input())
# if (a % 4 == 0 and a % 400 == 0) or (a % 4 == 0 and a % 100 != 0):
#     print(1)
# else:
#     print(0)

# 2-4
# x = int(input())
# y = int(input())
# if x > 0 and y > 0:
#     print(1)
# elif x < 0 and y > 0:
#     print(2)
# elif x < 0 and y < 0:
#     print(3)
# elif x > 0 and y < 0:
#     print(4)

# 2-5
# H, M = map(int, input().split())
# M = M - 45
# if M > 59:
#     H += 1
#     M = M - 60
# elif M < 0:
#     H -= 1
#     M = 60 + M
# if H > 23:
#     H = 0 + (H-24)
# elif H < 0:
#     H = 0 + (24+H)
# print(str(H) + " " + str(M))


# 2-6
# A, B = map(int, input().split())
# C = int(input())
# B = B + C
# A = A + B // 60
# B = B % 60
# if A > 23:
#     A = 0 + (A - 24)
# elif A < 0:
#     A = 0 + (24 + A)
# print(str(A) + " " + str(B))


# 2-7
# dice = list(map(int, input().split()))
# if dice.count(dice[0]) == 3:
#     prize = 10000 + dice[0] * 1000
# elif dice.count(dice[0]) == 2 or dice.count(dice[1]) == 2:
#     if dice.count(dice[0]) == 2:
#         prize = 1000 + dice[0] * 100
#     else:
#         prize = 1000 + dice[1] * 100
# else:
#     prize = max(dice) * 100
# print(prize)
