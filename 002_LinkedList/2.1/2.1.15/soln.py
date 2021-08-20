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

def occurence(head,K):
    currNode = head
    count = 0
    while currNode != None:
        if currNode.value == K:
            count += 1
        currNode = currNode.nextNode
    return count

def solution(N,L,K):
    # Write your code here...
    head = constructList(L,N)
    count = occurence(head,K)
    return count
    
N=int(input())
L=[]
n=0
for e in input().split():
    if(n<N):
        L.append(int (e))
        n+=1
K = int(input())
print(solution(N,L,K),end='')