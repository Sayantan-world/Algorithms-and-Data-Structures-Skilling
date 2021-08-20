class node(object):
    def __init__(self,value):
        self.value = value
        self.nextNode = None

def constructList(N,L):
    head = node(None)
    currNode = head
    for i in range(N):
        currNode.nextNode = node(L[i])
        currNode = currNode.nextNode
    return head

def find(head,K):
    currNode = head.nextNode
    count = 1
    while currNode != None:
        if count == K:
            return currNode.value
        currNode = currNode.nextNode
        count += 1

def solution(N,L,K):
    # Write your code here...
    if N == 0 or K < 0:
        return -1
    if N < K :
        return -1
    head = constructList(N,L)
    return find(head,K)
    
N=int(input())
L=[]
n=0
for e in input().split():
    if(n<N):
        L.append(int (e))
        n+=1
K = int(input())
print(solution(N,L,K),end='')