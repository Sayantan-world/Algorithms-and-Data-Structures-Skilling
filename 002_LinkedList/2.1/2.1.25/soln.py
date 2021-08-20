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

def moveNode(root):
    if not root.next:
        return root
    curr = root
    while curr.next.next:
        curr = curr.next
    lastNode = curr.next
    curr.next = None
    newNode = lastNode
    newNode.next = root
    return newNode

def printList(root):
    while root:
        print(root.data,end=' ')
        root = root.next

def solution(L):
    # Write your code here...
    root = construct(L)
    root = moveNode(root)
    printList(root)
 
N=int(input())
L=[]
n=0
for e in input().split():
    if(n<N):
        L.append(int (e))
        n+=1
solution(L)