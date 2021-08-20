class node(object):
    def __init__(self,value):
        self.value = value
        self.nextNode = None

def constructList(L,N):
    head = node(None)
    currNode = head
    for i in range(0,N):
        currNode.nextNode = node(L[i])
        currNode = currNode.nextNode
    return head

def deleteTail(head):
    ptr1 = head.nextNode
    ptr2 = head.nextNode.nextNode
    while ptr2.nextNode != None:
        ptr1 = ptr1.nextNode
        ptr2 = ptr2.nextNode
    ptr1.nextNode = None
    return head

def printForward(head):
    currNode = head.nextNode
    while currNode != None:
        print(currNode.value,end=" ")
        currNode = currNode.nextNode
    return

def solution(N,L):
    # Write your code here...
    if N==0 or N==1:
        print("no element present")
        return
    head = constructList(L,N)
    head = deleteTail(head)
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