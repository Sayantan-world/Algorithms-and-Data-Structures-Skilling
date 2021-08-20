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
    
def swapNodes(head,tail,K):
    node1,node2 = None,None
    count = 1
    curr = head
    while head != None:
        if count == K:
            node1 = curr
            break
        count += 1
        curr = curr.nextNode
    count = 1
    curr = tail
    while tail != None:
        if count == K:
            node2 = curr
            break
        count += 1
        curr = curr.prevNode
    if not node1 or not node2:
        return
    node1.value,node2.value = node2.value,node1.value

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

def solution(N,A,K):
    # Write your code here...
    head = constructList(N,A)
    tail = findTail(head)
    swapNodes(head, tail, K)
    printForward(head)
    print("")
    printBackward(tail)
    return

N = int(input())
if N == 0:
    print("No element present")
else:
    A = list(map(int,input().split()))
    K = int(input())
    solution(N,A,K)