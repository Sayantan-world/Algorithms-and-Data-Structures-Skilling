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

def split(head):
    slow,fast = head,head
    while fast.nextNode and fast.nextNode.nextNode:
        slow = slow.nextNode
        fast = fast.nextNode.nextNode
    right = slow.nextNode
    slow.nextNode = None
    return right

def merge(left,right):
    if not left:
        return right
    if not right:
        return left
    if left.value < right.value:
        left.nextNode = merge(left.nextNode,right)
        left.nextNode.prevNode = left
        left.prevNode = None
        return left
    else:
        right.nextNode = merge(left,right.nextNode)
        right.nextNode.prevNode = right
        right.prevNode = None
        return right
    
def mergeSort(head):
    if not head or not head.nextNode:
        return head
    right = split(head)
    head = mergeSort(head)
    right = mergeSort(right)
    return merge(head,right)

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
    head = mergeSort(head)
    tail = findTail(head)
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