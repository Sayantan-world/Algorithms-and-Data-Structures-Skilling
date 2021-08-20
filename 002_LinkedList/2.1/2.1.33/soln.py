class node(object):
    def __init__(self,value):
        self.value = value
        self.nextNode = None

def constructList(L,N):
    head = node(None)
    currNode = head
    for i in range(N):
        currNode.nextNode = node(L[i])
        currNode = currNode.nextNode
    return head

def rotate(head,K):
    currNode = head.nextNode
    count = 1
    while currNode.nextNode != None:
        if count == K:
            rotateNode = currNode
        currNode = currNode.nextNode
        count += 1
    tailNode = currNode
    rotateNext = rotateNode.nextNode
    tailNode.nextNode = head.nextNode
    head.nextNode = rotateNext
    rotateNode.nextNode = None
    return head

def printForward(head):
    currNode = head.nextNode
    while currNode != None:
        print(currNode.value,end=" ")
        currNode = currNode.nextNode
    return

def solution(N,L,K):
    # Write your code here...
    if N == 0:
        print('no element present')
        return
    K = K % N
    head = constructList(L,N)
    if K == 0:
        printForward(head)
        return
    head = rotate(head,K)
    printForward(head)
    return

N=int(input())
L=[]
n=0
for e in input().split():
    if(n<N):
        L.append(int (e))
        n+=1
K = int(input())
solution(N,L,K)