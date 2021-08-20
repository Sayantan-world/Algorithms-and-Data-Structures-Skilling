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

def deleteOccur(head,K):
    if head.next == head:
        if head.data == K:
            return None
        else:
            return head
    if head.data == K:
        curr = head.next
        while curr.next != head:
            curr = curr.next
        curr.next = head.next
        return head.next
    prev,curr = head,head.next
    while curr != head:
        if curr.data == K:
            prev.next = curr.next
            break
        curr = curr.next
        prev = prev.next
    return head

def printList(head):
    if not head:
        print("no element present")
        return
    print(head.data,end=' ')
    curr = head.next
    while curr != head:
        print(curr.data,end=' ')
        curr = curr.next

def solution(N,L,K):
    # Write your code here...
    root = construct(L)
    root = deleteOccur(root, K)
    printList(root)
    
N = int(input())
if N == 0:
    print("no element present")
else:
    L = list(map(int,input().split()))
    K = int(input())
    solution(N,L,K)