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

def merge(root1,root2):
    root = Node(None)
    curr = root
    while root1 and root2:
        curr.next = Node(root1.data)
        curr = curr.next
        curr.next = Node(root2.data)
        curr = curr.next
        root1 = root1.next
        root2 = root2.next
    while root1:
        curr.next = Node(root1.data)
        curr = curr.next
        root1 = root1.next
    while root2:
        curr.next = Node(root2.data)
        curr = curr.next
        root2 = root2.next
    return root.next

def printList(root):
    while root:
        print(root.data,end=' ')
        root = root.next

def solution(N1,L1,N2,L2):
    # Write your code here...
    root1 = construct(L1)
    root2 = construct(L2)
    root = merge(root1, root2)
    printList(root)
    
N1=int(input())
if N1 != 0:
    L1 = list(map(int,input().split()))
N2 = int(input())
if N2 != 0:
    L2 = list(map(int,input().split()))
if N1 == 0 and N2 == 0:
    print("no element present")
elif N1 != 0 and N2 == 0:
    print(*L1)
elif N1 == 0 and N2 != 0:
    print(*L2)
else:
    solution(N1,L1,N2,L2)