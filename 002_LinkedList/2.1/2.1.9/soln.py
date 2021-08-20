class node(object):
    def __init__(self,value):
        self.value = value
        self.nextNode = None

def constructList(N,L):
    head = node(None)
    currNode = head
    for i in range(N):
        tempNode = node(L[i])
        currNode.nextNode = node(L[i])
        currNode = currNode.nextNode
    return head

def swap(N,L,K1,K2,head):
    if K1 == K2:
        return
    node1,node2 = None,None
    currNode = head
    while currNode.nextNode != None:
        if currNode.nextNode.value == K1:
            node1 = currNode
        elif currNode.nextNode.value == K2:
            node2 = currNode
        currNode = currNode.nextNode
    if node1 != None and node2 != None:
        tempNode = node1.nextNode
        node1.nextNode = node2.nextNode
        node2.nextNode = tempNode
        tempNode = node1.nextNode.nextNode
        node1.nextNode.nextNode = node2.nextNode.nextNode
        node2.nextNode.nextNode = tempNode
    return

def printForward(head):
    currNode = head.nextNode
    while currNode != None:
        print(currNode.value,end=" ")
        currNode = currNode.nextNode
    return

def solution(N,L,K1,K2):
    # Write your code here...
    head = constructList(N,L)
    swap(N,L,K1,K2,head)
    printForward(head)
    return
    
N=int(input())
L=[]
n=0
for e in input().split():
    if(n<N):
        L.append(int (e))
        n+=1
K1 = int(input())
K2 = int(input())
solution(N,L,K1,K2)