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

def duplicate(head):
    currNode = head.nextNode
    h = set()
    h.add(currNode.value)
    while currNode.nextNode != None:
        if currNode.nextNode.value in h:
            currNode.nextNode = currNode.nextNode.nextNode
        else:
            h.add(currNode.nextNode.value)
            currNode = currNode.nextNode
    return head

def printForward(head):
    currNode = head.nextNode
    while currNode != None:
        print(currNode.value,end=" ")
        currNode = currNode.nextNode
    return

def solution(N,L):
    # Write your code here...
    head = constructList(L,N)
    if N == 1:
        printForward(head)
        return
    head = duplicate(head)
    printForward(head)
    return

N=int(input())
try:
    L=[]
    n=0
    for e in input().split():
        if(n<N):
            L.append(int (e))
            n+=1
    solution(N,L)
except:
    print("no element present")