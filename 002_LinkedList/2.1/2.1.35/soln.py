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

def partition(head,tail):
    if head == tail or not head or not tail:
        return head
    pivot,curr,pivot_data = head,head,tail.data
    while head != tail:
        if head.data < pivot_data:
            pivot = curr
            curr_data = curr.data
            curr.data = head.data
            head.data = curr_data
            curr = curr.next
        head = head.next
    
    curr_data = curr.data
    curr.data = pivot_data
    tail.data = curr_data
    return pivot

def quickSort(head,tail):
    if not head or head == tail or head == tail.next:
        return
    pivot = partition(head,tail)
    quickSort(head, pivot)
    
    if pivot and pivot == head:
        quickSort(pivot.next, tail)
    elif pivot and pivot.next:
        quickSort(pivot.next.next, tail)

def printList(root):
    while root:
        print(root.data,end=' ')
        root = root.next

def solution(L):
    # Write your code here...
    head = construct(L)
    tail = head
    while tail.next:
        tail = tail.next
    quickSort(head, tail)
    printList(head)
    
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