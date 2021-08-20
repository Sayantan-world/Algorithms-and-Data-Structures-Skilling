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

def swapNode(root):
    currNode = root
    while currNode and currNode.next:
        if currNode.data != currNode.next.data:
            currNode.data,currNode.next.data = currNode.next.data,currNode.data
        currNode = currNode.next.next

def printList(root):
    while root:
        print(root.data,end=' ')
        root = root.next

def solution(N,L):
    # Write your code here...
    root = construct(L)
    swapNode(root)
    printList(root)
    
try:
    N = int(input())
    L = list(map(int,input().split()))
    solution(N, L)
except:
    print("no element present")