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

def printReverse(root):
    if root:
        printReverse(root.next)
        print(root.data,end=' ')
    else:
        return

def solution(L):
    # Write your code here...
    root = construct(L)
    printReverse(root)
    
try:    
    N=int(input())
    L=[]
    n=0
    for e in input().split():
        if(n<N):
            L.append(int (e))
            n+=1
    solution(L)
except:
    print("no element present")