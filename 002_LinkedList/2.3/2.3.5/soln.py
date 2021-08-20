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
    return head,tail


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

def solution(N,A):
    # Write your code here...
    head,tail = constructList(A,N)
    printBackward(tail)
    print()
    printForward(head)
    return

N = int(input())
if N == 0:
    print("No element present")
else:
    A = list(map(int,input().split()))
    solution(N,A)