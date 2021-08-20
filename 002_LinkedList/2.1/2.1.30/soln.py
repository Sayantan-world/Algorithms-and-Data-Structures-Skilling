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

def segregate(root):
    root1,root2 = Node(None),Node(None)
    curr1,curr2 = root1,root2
    while root:
        if root.data % 2 == 0:
            curr1.next = Node(root.data)
            curr1 = curr1.next
        else:
            curr2.next = Node(root.data)
            curr2 = curr2.next
        root = root.next
    curr1.next = root2.next
    return root1.next

def printList(root):
    while root:
        print(root.data,end=' ')
        root = root.next

def solution(L):
    # Write your code here...
    root = construct(L)
    root = segregate(root)
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