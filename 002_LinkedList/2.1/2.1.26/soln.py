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

def delEven(root):
    count = 0
    curr = root
    while curr and curr.next:
        if count % 2 == 0:
            curr.next = curr.next.next
            count += 2
        else:
            count += 1
        curr = curr.next
    return root

def printList(root):
    while root:
        print(root.data,end = " ")
        root = root.next

def solution(L):
    # Write your code here...
    root = construct(L)
    root = delEven(root)
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