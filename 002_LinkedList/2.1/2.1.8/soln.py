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

def find(head,K):
    currNode = head.nextNode
    ind = 0
    while currNode != None:
        if currNode.value == K:
            return ind
        ind += 1
        currNode = currNode.nextNode
    return -1

def solution(N,L,K):
    # Write your code here...
    if N==0:
        return -1
    head = constructList(L,N)
    ind = find(head,K)
    return ind
   
N=int(input())
L=[]
n=0
for e in input().split():
    if(n<N):
        L.append(int (e))
        n+=1
K = int(input())
print(solution(N,L,K), end="")