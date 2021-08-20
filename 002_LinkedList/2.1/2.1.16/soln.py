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

def reverse(head):
    prev,curr,nxt = None,head,None
    while curr != None:
        nxt = curr.nextNode
        curr.nextNode = prev
        prev = curr
        curr = nxt
    head = prev
    return head

def printForward(head):
    currNode = head
    while currNode != None:
        print(currNode.value,end=" ")
        currNode = currNode.nextNode
    return

def solution(N,L):
    # Write your code here...
    if N == 0:
        print("no element present")
        return
    head = constructList(L,N)
    head = reverse(head)
    printForward(head)
    return

N=int(input())
L=[]
n=0
for e in input().split():
    if(n<N):
        L.append(int (e))
        n+=1
solution(N,L)