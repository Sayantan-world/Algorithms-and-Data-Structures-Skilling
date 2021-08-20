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

def mergeList(root1,root2):
    root = Node(None)
    ret = root
    while root1 and root2:
        if root1.data < root2.data:
            root.next = Node(root1.data)
            root1 = root1.next
        else:
            root.next = Node(root2.data)
            root2 = root2.next
        root = root.next
    while root1:
        root.next = Node(root1.data)
        root1 = root1.next
        root = root.next
    while root2:
        root.next = Node(root2.data)
        root2 = root2.next
        root = root.next
        
    return ret.next

def printList(root):
    while root:
        print(root.data,end=' ')
        root = root.next

def solution(N1,L1,N2,L2):
    # Write your code here...
    if N1 != 0:
        root1 = construct(L1)
    else:
        root1 = None
    root2 = construct(L2)
    root = mergeList(root1, root2)
    printList(root)

def solution2(N1,L1):
    root1 = construct(L1)
    root2 = None
    root = mergeList(root1, root2)
    printList(root)

N1 = int(input())
if N1 != 0:
    L1 = list(map(int,input().split()))
else:
    L1 = []
N2 = int(input())
if N2 != 0:
    L2 = list(map(int,input().split()))
if N1 == 0 and N2 == 0:
    print("no element present")
elif N2 != 0:
    solution(N1,L1,N2,L2)
else:
    solution2(N1, L1)