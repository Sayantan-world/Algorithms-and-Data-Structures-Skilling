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

def length(head):
    currNode = head.nextNode
    l = 0
    while currNode != None:
        l += 1
        currNode = currNode.nextNode
    return l

def solution(N,L):
    # Write your code here...
    head = constructList(L,N)
    l = length(head)
    return l
    
N=int(input())
L=[]
n=0
for e in input().split():
    if(n<N):
        L.append(int (e))
        n+=1
print(solution(N,L),end='')