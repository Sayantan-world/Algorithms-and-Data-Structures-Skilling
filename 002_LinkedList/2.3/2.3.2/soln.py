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

def insertFront(head,K):
    temp = head.nextNode
    new_node = node(K)
    new_node.prevNode = head
    head.nextNode = new_node
    new_node.nextNode = temp
    temp.prevNode = new_node
    return head

def printForward(head):
    currNode = head.nextNode
    while currNode.nextNode != None:
        print(currNode.value,end=" ")
        currNode = currNode.nextNode
    return currNode

def printBackward(tail):
    currNode = tail.prevNode
    while currNode.prevNode != None:
        print(currNode.value,end=" ")
        currNode = currNode.prevNode
    return

def solution(N,A,K):
    # Write your code here...
    head = constructList(A,N)
    head = insertFront(head,K)
    tail = printForward(head)
    print("")
    printBackward(tail)
    return

N = int(input())
A = list(map(int,input().split()))
K = int(input())
solution(N,A,K)