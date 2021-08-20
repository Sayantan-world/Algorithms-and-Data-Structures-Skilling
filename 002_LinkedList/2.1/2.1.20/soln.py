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

def intersection(root1,root2):
    root = Node(None)
    ret = root
    while root1 and root2:
        if root1.data == root2.data:
            root.next = Node(root1.data)
            root = root.next
            root1 = root1.next
            root2 = root2.next
        elif root1.data < root2.data:
            root1 = root1.next
        else:
            root2 = root2.next
    return ret.next

def printList(root):
    if not root:
        print("no intersection element present")
        return
    while root:
        print(root.data,end=' ')
        root = root.next

def solution(N1,L1,N2,L2):
    # Write your code here...
    root1 = construct(L1)
    root2 = construct(L2)
    root = intersection(root1, root2)
    printList(root)
    
N1 = int(input())
L1 = list(map(int,input().split()))
N2 = int(input())
if N2 != 0:
    L2 = list(map(int,input().split()))
if N1 == 0 or N2 == 0:
    print("no intersection element present")
else:
    solution(N1, L1, N2, L2)