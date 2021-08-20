class node(object):
    def __init__(self,value):
        self.value = value
        self.nextNode = None
        self.prevNode = None

def constructList(N,A):
    head = node(A[0])
    currNode = head
    for i in range(1,N):
        temp = node(A[i])
        currNode.nextNode = temp
        temp.prevNode = currNode
        currNode = temp
    return head

def findTail(head):
    curr = head
    while curr.nextNode:
        curr = curr.nextNode
    return curr

def partition(head,tail):
    pivot = tail.value
    curr = head.prevNode
    iter = head
    while iter != tail:
        if iter.value <= pivot:
            if not curr:
                curr = head
            else:
                curr = curr.nextNode
            iter.value,curr.value = curr.value,iter.value
        iter = iter.nextNode
    if not curr:
        curr = head
    else:
        curr = curr.nextNode
    curr.value,tail.value = tail.value,curr.value
    return curr
    

def quickSort(head,tail):
    if tail and head != tail and head != tail.nextNode:
        mid = partition(head,tail)
        quickSort(head, mid.prevNode)
        quickSort(mid.nextNode, tail)

def printForward(head):
    currNode = head
    while currNode != None:
        print(currNode.value,end=" ")
        currNode = currNode.nextNode
    return

def printBackward(tail):
    currNode = tail
    while currNode != None:
        print(currNode.value,end=" ")
        currNode = currNode.prevNode
    return

def solution(N,A):
    # Write your code here...
    head = constructList(N,A)
    tail = findTail(head)
    quickSort(head, tail)
    printForward(head)
    print("")
    printBackward(tail)
    return

N = int(input())
if N == 0:
    print("No element present")
else:
    A = list(map(int,input().split()))
    solution(N,A)