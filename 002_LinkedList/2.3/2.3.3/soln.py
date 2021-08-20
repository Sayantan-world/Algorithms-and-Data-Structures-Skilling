class node(object):
    def __init__(self,value):
        self.value = value
        self.nextNode = None
        self.prevNode = None

def constructList(A,N):
    head = node(None)
    currNode = head
    for i in range(N):
        temp = node(A[i])
        currNode.nextNode = temp
        temp.prevNode = currNode
        currNode = temp
    tail = node(None)
    currNode.nextNode = tail
    tail.prevNode = currNode
    return head

def deleteFirst(head):
    delNode = head.nextNode
    postDelNode = delNode.nextNode
    head.nextNode = postDelNode
    postDelNode.prevNode = head
    return

def printForward(head):
    currNode = head.nextNode
    while currNode.nextNode != None:
        print(currNode.value,end=" ")
        currNode = currNode.nextNode
    return

def printBackward(head):
    currNode = head.nextNode
    while currNode.nextNode != None:
        currNode = currNode.nextNode
    tail = currNode
    currNode = tail.prevNode
    while currNode.prevNode != None:
        print(currNode.value,end=" ")
        currNode = currNode.prevNode
    return

def solution(N,A):
    # Write your code here...
    if N==0 or N==1:
        print("No element present")
        return
    head = constructList(A,N)
    deleteFirst(head)
    printForward(head)
    print("")
    printBackward(head)
    return

N = int(input())
A = list(map(int,input().split()))
solution(N,A)