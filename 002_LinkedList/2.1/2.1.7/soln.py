class node(object):
    def __init__(self,value):
        self.value = value
        self.nextNode = None

def constructList(N,L):
    head = node(None)
    currNode = head
    for i in range(0,N):
        currNode.nextNode = node(L[i])
        currNode = currNode.nextNode
    return head

def search(head,K):
    currNode = head.nextNode
    index = 0
    while currNode != None:
        if currNode.value == K:
            return index
        currNode = currNode.nextNode
        index += 1
    return -1

def solution(N,L,K):
    # Write your code here...
    if N==0:
        return -1
    head = constructList(N,L)
    return search(head,K)
    
N=int(input())
L=[]
n=0
for e in input().split():
    if(n<N):
        L.append(int (e))
        n+=1
K = int(input())
print(solution(N,L,K),end='')