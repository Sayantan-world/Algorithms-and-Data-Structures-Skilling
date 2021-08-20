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

def removeNode(root,N1,N2):
    if N2 == 0:
        return root
    curr = root
    count = 1
    prevNode,nextNode = None,None
    while curr:
        if count == N1:
            prevNode = curr
            curr = curr.next
            count += 1
        elif count == N1 + N2:
            nextNode = curr.next
            curr = curr.next
            prevNode.next = nextNode
            count = 1
            prevNode = None
        else:
            curr = curr.next
            count += 1
    if prevNode:
        prevNode.next = None
    return root

def printList(root):
    while root:
        print(root.data,end=' ')
        root = root.next

def solution(N,L,N1,N2):
    # Write your code here...
    root = construct(L)
    root = removeNode(root, N1, N2)
    printList(root)
    
try:
    N=int(input())
    L=[]
    n=0
    for e in input().split():
        if(n<N):
            L.append(int (e))
            n+=1
    N1 = int(input())
    N2 = int(input())
    solution(N,L,N1,N2)
except:
    print("no element present")
