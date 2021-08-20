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

def insertLast(head,K):
    currNode = head.nextNode
    while currNode.nextNode != None:
        currNode = currNode.nextNode
    tail = currNode
    inNode = node(K)
    preInNode = tail.prevNode
    tail.prevNode = inNode
    preInNode.nextNode = inNode
    inNode.prevNode = preInNode
    inNode.nextNode = tail
    return tail

def printForward(head):
    currNode = head.nextNode
    while currNode.nextNode != None:
        print(currNode.value,end=" ")
        currNode = currNode.nextNode
    return

def printBackward(tail):
    currNode = tail.prevNode
    while currNode.prevNode != None:
        print(currNode.value,end=" ")
        currNode = currNode.prevNode
    return

def solution(N,A,K):
    # Write your code here...
    head = constructList(A,N)
    tail = insertLast(head,K)
    printForward(head)
    print("")
    printBackward(tail)
    return

N = int(input())
A = list(map(int,input().split()))
K = int(input())
solution(N,A,K)