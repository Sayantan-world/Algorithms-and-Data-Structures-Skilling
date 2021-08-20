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

def deleteFirst(head):
    curr = head
    while curr.next != head:
        curr = curr.next
    curr.next = head.next
    return head.next

def printList(head):
    print(head.data,end=' ')
    curr = head.next
    while curr != head:
        print(curr.data,end=' ')
        curr = curr.next

def solution(L):
    # Write your code here...
    root = construct(L)
    root = deleteFirst(root)
    printList(root)
    
N = int(input())
if N == 0:
    print("no element present")
else:
    L = list(map(int,input().split()))
    solution(L)
