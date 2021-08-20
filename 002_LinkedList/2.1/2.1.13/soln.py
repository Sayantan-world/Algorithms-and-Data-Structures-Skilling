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

def deleteNode(root,val):
    curr = root
    ptr = None
    prevPtr = None
    while curr.next:
        if curr.next.data == val:
            ptr = curr.next
            prevPtr = curr
        curr = curr.next
    if not ptr:
        if root.data == val:
            root = root.next
            return root
    elif ptr and not ptr.next:
        prevPtr.next = None
    elif ptr and ptr.next:
        prevPtr.next = ptr.next
    return root

def printList(root):
    if not root:
        print("no element present")
    else:
        while root:
            print(root.data,end=' ')
            root = root.next

def solution(L,K):
    # Write your code here...
    root = construct(L)
    root = deleteNode(root, K)
    printList(root)
    
N=int(input())
L=[]
n=0
for e in input().split():
    if(n<N):
        L.append(int (e))
        n+=1
K = int(input())
if N == 0:
    print("no element present")
else:
    solution(L,K)