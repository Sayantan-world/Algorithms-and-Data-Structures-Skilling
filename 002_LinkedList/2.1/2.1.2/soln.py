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

def insertEnd(root,val):
    while root.next:
        root = root.next
    root.next = Node(val)

def printList(root):
    while root:
        print(root.data,end=' ')
        root = root.next

def solution(N,L,K):
    # Write your code here...
    root = construct(L)
    insertEnd(root, K)
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
    print(K)
else:
    solution(N,L,K)