# 아마존 인터뷰
# <처음 나의 풀이>
# import sys
# sys.stdin = open('input.txt')
# input = sys.stdin.readline

# n = int(input())
# a = list(map(int, input().split()))
# check_list = [0] * n
# res = 'NO'

# def DFS(level):
#     global res
    
#     if level == n:
#         tmp1 = []
#         tmp2 = []
        
#         for i in range(0, len(check_list)):
#             if check_list[i] == 1:
#                 tmp1.append(a[i])
#             else:
#                 tmp2.append(a[i])
        
#         if sum(tmp1) == sum(tmp2):
#             res = 'YES'

#         return
        
#     else:
#         check_list[level] = 1
#         DFS(level + 1)
#         check_list[level] = 0
#         DFS(level + 1)
    
# DFS(0)
# print(res)



# <강의 풀이>
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
tot = sum(a)
check_list = [0] * n    # 내가 여기 썼다는 표시

def DFS(level, sum):
    if sum > tot//2:    # sum이 tot의 절반을 넘으면 이때부터는 더 들어가도 tot과 같아질 수 없다.
        print('NO')
        sys.exit(0)
    
    if level == n:
        if sum == (tot - sum):
            print('YES')
            sys.exit(0)     # 파이썬 실행 프로그램 전체를 아예 종료시킨다.
    
    else:
        DFS(level + 1, sum + a[level])      # 이번 원소값을 사용하겠다. 다음 sum으로 넘기겠다.
        DFS(level + 1, sum)                 # 이번 원소값을 사용하지 않겠다. 다음 sum으로 넘기지 않겠다.
        
DFS(0, 0)
print('NO')
        