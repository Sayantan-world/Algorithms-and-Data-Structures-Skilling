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
    ptr1,ptr2 = currNode,currNode
    count = 0
    while ptr2 != None:
        if count >= K:
            ptr1 = ptr1.nextNode
            ptr2 = ptr2.nextNode
            count += 1
        else:
            ptr2 = ptr2.nextNode
            count += 1
    return ptr1.value

def solution(N,L,K):
    # Write your code here...
    if N == 0:
        return -1
    if N < K :
        return -1
    head = constructList(N,L)
    return find(head,K)
    
N=int(input())
L=[]
n=0
try:
    for e in input().split():
        if(n<N):
            L.append(int (e))
            n+=1
    K = int(input())
    print(solution(N,L,K),end='')
except:
    print(-1)