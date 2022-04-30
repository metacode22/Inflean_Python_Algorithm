cnt = 5

def DFS0():
    print(cnt)

def DFS1():
    cnt = 3
    print(cnt)
    
def DFS2():
    global cnt
    if cnt == 5:
        cnt = cnt + 1
        print(cnt)
        
DFS2()
print(cnt)