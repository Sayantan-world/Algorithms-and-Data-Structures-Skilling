class node(object):
    def __init__(self,value):
        self.value = value
        self.nextNode = None

def constructList(N,L,K):
    head = node(None)
    currNode = head
    for i in range(N):
        currNode.nextNode = node(L[i])
        currNode = currNode.nextNode
        if K != -1:
            if i == K:
                tempNode = currNode
    
    if K != -1:
        currNode.nextNode = tempNode
    return head

def detectLoop(head):
    currNode = head.nextNode
    ptr1,ptr2 = currNode,currNode
    while (ptr1 != None) and (ptr2 != None):
        ptr1 = ptr1.nextNode
        ptr2 = ptr2.nextNode.nextNode
        if ptr1 == ptr2:
            return ptr1

def removeLoop(head,ptr):
    ptr1,ptr2 = ptr,ptr.nextNode
    lenLoop = 1
    while ptr1 != ptr2:
        ptr2 = ptr2.nextNode
        lenLoop += 1
    ptr1 = head.nextNode
    ptr2 = head.nextNode
    for i in range(lenLoop):
        ptr2 = ptr2.nextNode
    while ptr1 != ptr2:
        ptr1 = ptr1.nextNode
        ptr2 = ptr2.nextNode
    loopHead = ptr1
    ptrNew = loopHead
    while loopHead != ptrNew.nextNode:
        ptrNew = ptrNew.nextNode
    ptrNew.nextNode = None
    return head

def printForward(head):
    currNode = head.nextNode
    while currNode != None:
        print(currNode.value, end = " ")
        currNode = currNode.nextNode
    return

def solution(N,L,K):
    # Write your code here...
    head = constructList(N,L,K)
    if K == -1:
        printForward(head)
        return
    ptr = detectLoop(head)
    head = removeLoop(head,ptr)
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