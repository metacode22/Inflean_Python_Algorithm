# 부분집합은 썼냐 안썼냐로 구분한다.
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
check_list = [0] * (n + 1)

def DFS(v):
    if v == n + 1:
        for i in range(1, n + 1):
            if check_list[i] == 1:
                print(i, end ='')
        print()
                
    else:
        check_list[v] = 1
        DFS(v + 1)
        check_list[v] = 0
        DFS(v + 1)

DFS(1)
        
        
