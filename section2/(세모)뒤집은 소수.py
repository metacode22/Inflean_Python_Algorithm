import sys, math

def reverse(x):
    x_list = list(str(x))
    x_list.reverse()
    x_reversed = ''.join(x_list)

    return int(x_reversed)

def is_prime(x):
    if x <= 1:
        return False

    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False

    return True

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

for i in arr:
    i_reversed = reverse(i)

    if is_prime(i_reversed) == True:
        print(i_reversed, end = '')