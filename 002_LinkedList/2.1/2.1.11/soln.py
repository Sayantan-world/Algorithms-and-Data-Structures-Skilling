class node(object):
    def __init__(self,value):
        self.value = value
        self.nextNode = None

def constructList(L,N):
    head = node(L[0])
    currNode = head
    for i in range(1,N):
        currNode.nextNode = node(L[i])
        currNode = currNode.nextNode
    return head

def middleElement(head):
    ptr1,ptr2 = head,head
    while True:
        if ptr2 == None or ptr2.nextNode == None:
            return ptr1.value
        ptr2 = ptr2.nextNode.nextNode
        ptr1 = ptr1.nextNode

def solution(N,L):
    # Write your code here...
    if N==0:
        return -1
    head = constructList(L,N)
    val = middleElement(head)
    return val
    
N=int(input())
L=[]
n=0
for e in input().split():
    if(n<N):
        L.append(int (e))
        n+=1
print(solution(N,L),end='')