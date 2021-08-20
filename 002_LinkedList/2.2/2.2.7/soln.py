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

def split(head):
    if head.next.next == head:
        root = head.next
        root.next = root
        head.next = head
        return head,root
    slow = head
    fast = head.next
    while fast != head and fast.next != head:
        slow = slow.next
        fast = fast.next.next
    prev_mid = slow
    mid = slow.next
    end = mid
    while end.next != head:
        end = end.next
    prev_mid.next = head
    end.next = mid
    return head,mid

def printList(head):
    if not head:
        print("no element present")
        return
    if head.next == head:
        print(head.data)
        return
    print(head.data,end=' ')
    curr = head.next
    while curr != head:
        if curr.next == head:
            print(curr.data)
        else:
            print(curr.data,end=' ')
        curr = curr.next

def solution(L):
    # Write your code here...
    root = construct(L)
    if root.next == root:
        printList(root)
        return
    root1,root2 = split(root)
    printList(root1)
    printList(root2)
    
N = int(input())
if N == 0:
    print("no element present")
else:
    L = list(map(int,input().split()))
    solution(L)