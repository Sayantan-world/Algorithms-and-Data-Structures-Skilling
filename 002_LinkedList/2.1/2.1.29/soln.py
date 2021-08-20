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

def deleteRight(root):
    if not root or not root.next:
        return root
    newNode = deleteRight(root.next)
    if newNode.data > root.data:
        return newNode
    root.next = newNode
    return root

def printList(root):
    while root:
        print(root.data,end=' ')
        root = root.next

def solution(L):
    # Write your code here...
    root = construct(L)
    root = deleteRight(root)
    printList(root)
    
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