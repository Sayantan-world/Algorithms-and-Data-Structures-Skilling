class Node:
    def __init__(self,val):
        self.data = val
        self.next = None

def construct(L):
    head = Node(L[0])
    curr = head
    for i in range(1,len(L)):
        curr.next = Node(L[i])
        curr = curr.next
    curr.next = head
    return head

def insertEnd(head,K):
    curr = head
    while curr.next != head:
        curr = curr.next
    newNode = Node(K)
    curr.next = newNode
    newNode.next = head
    return head

def printList(head):
    print(head.data,end=' ')
    curr = head.next
    while curr != head:
        print(curr.data,end=' ')
        curr = curr.next

def solution(N,L,K):
    # Write your code here...
    root = construct(L)
    root = insertEnd(root, K)
    printList(root)
    
N = int(input())
L = list(map(int,input().split()))
K = int(input())
if N == 0:
    print(K)
else:
    solution(N,L,K)