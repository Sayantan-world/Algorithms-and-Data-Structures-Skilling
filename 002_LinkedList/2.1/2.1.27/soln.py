class Node:
    def __init__(self,val):
        self.data = val
        self.next = None

def construct(L):
    root = Node(L[0])
    curr = root
    for i in range(1,len(L)):
        curr.next = Node(L[i])
        curr = curr.next
    return root

def isIdentical(root1,root2):
    while root1 and root2:
        if root1.data != root2.data:
            return 0
        root1 = root1.next
        root2 = root2.next
    if root1 or root2:
        return 0
    return 1

def solution(N1,L1,N2,L2):
    # Write your code here...
    root1 = construct(L1)
    root2 = construct(L2)
    return isIdentical(root1, root2)

try:
    N1=int(input())
    L1 = list(map(int,input().split()))
    N2 = int(input())
    L2 = list(map(int,input().split()))
    print(solution(N1,L1,N2,L2),end='')
except:
    print(0)