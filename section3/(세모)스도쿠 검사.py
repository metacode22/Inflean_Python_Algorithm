import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

x = [list(map(int, input().split())) for _ in range(9)]

def check(a):
    for i in range(9):
        ch1 = [0] * 10
        ch2 = [0] * 10
        for j in range(9):
            ch1[a[i][j]] = 1
            ch2[a[j][i]] = 1

        if sum(ch1) != 9 or sum(ch2) != 9:
            return False

    for k in range(3):
        for l in range(3):
            ch3 = [0] * 10
            for m in range(3):
                for n in range(3):
                    ch3[a[k*3 + m][l*3 + n]] = 1

            if sum(ch3) != 9:
                return False

    return True

if check(x):
    print('YES')
else:
    print('NO')