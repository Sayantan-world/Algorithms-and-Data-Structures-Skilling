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
        if i == K:
            tempNode = currNode
    
    currNode.nextNode = tempNode
    return head

def loop(head):
    currNode = head.nextNode
    ptr1,ptr2 = currNode,currNode
    while (ptr1 != None) and (ptr2 != None):
        ptr1 = ptr1.nextNode
        ptr2 = ptr2.nextNode.nextNode
        if ptr1 == ptr2:
            return 1
    return 0

def solution(N,L,K):
    # Write your code here...
    if K == -1:
        return 0
    head = constructList(N,L,K)
    return loop(head)
    
N=int(input())
L=[]
n=0
for e in input().split():
    if(n<N):
        L.append(int (e))
        n+=1
K = int(input())
print(solution(N,L,K),end='')