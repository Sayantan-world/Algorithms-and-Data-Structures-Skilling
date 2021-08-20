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

def length(root):
    if not root:
        return 0
    else:
        return 1 + length(root.next)

def solution(L):
    # Write your code here...
    if len(L) == 0:
        return 0
    root = construct(L)
    return length(root)
    
N=int(input())
L=[]
n=0
for e in input().split():
    if(n<N):
        L.append(int (e))
        n+=1
print(solution(L),end='')