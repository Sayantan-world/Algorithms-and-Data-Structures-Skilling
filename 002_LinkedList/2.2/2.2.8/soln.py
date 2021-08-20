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

def insertNode(head,K):
    if head.next == head:
        if head.data > K:
            node = Node(K)
            node.next = head
            head.next = node
            return node
        else:
            node = Node(K)
            head.next = node
            node.next = head
            return head
    curr = head
    while curr.next != head:
        if curr.data <= K <= curr.next.data:
            node = curr
            break
        curr = curr.next
    if head.data >= K:
        node = Node(K)
        curr.next = node
        node.next = head
        return node
    newNode = Node(K)
    nextNode = curr.next
    curr.next = newNode
    newNode.next = nextNode
        
    return head

def printList(head):
    if not head:
        print("no element present")
        return
    print(head.data,end=' ')
    curr = head.next
    while curr != head:
        if curr.next == head:
            print(curr.data)
        else:
            print(curr.data,end=' ')
        curr = curr.next

def solution(N,L,K):
    # Write your code here...
    root = construct(L)
    root = insertNode(root, K)
    printList(root)
    
N = int(input())
if N == 0:
    L = input()
    K = int(input())
    print(K)
else:
    L = list(map(int,input().split()))
    K = int(input())
    solution(N,L,K)