import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = 4

def preorder(v, level):
    if level == n - 1:
        return
        
    print(v, end = '')
    preorder(2*v, level + 1)
    preorder(2*v + 1, level + 1)
    
def inorder(v, level):
    if level == n - 1:
        return
        
    inorder(2*v, level + 1)
    print(v, end = '')
    inorder(2*v + 1, level + 1)
    
def postorder(v, level):
    if level == n - 1:
        return
        
    postorder(2*v, level + 1)
    postorder(2*v + 1, level + 1)
    print(v, end = '')
    
preorder(1, 0)
print()
inorder(1, 0)
print()
postorder(1, 0)