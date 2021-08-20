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

def delPos(root,pos):
    if pos == 1:
        return root.next
    count = 2
    curr = root
    prevPtr,ptr,nextPtr = None,None,None
    while curr:
        if count == pos:
            if not curr.next:
                return root
            prevPtr = curr
            ptr = curr.next
            nextPtr = curr.next.next
            break
        curr = curr.next
        count += 1
    if ptr:
        prevPtr.next = nextPtr
    return root

def printList(root):
    if not root:
        print("no element present")
        return
    while root:
        print(root.data,end=' ')
        root = root.next

def solution(N,L,pos):
    # Write your code here...
    root = construct(L)
    root = delPos(root, pos)
    printList(root)
    
N=int(input())
L=[]
n=0
for e in input().split():
    if(n<N):
        L.append(int (e))
        n+=1
pos = int(input())
if N == 0:
    print("")
else:
    solution(N,L,pos)