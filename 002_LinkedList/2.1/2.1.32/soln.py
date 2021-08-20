class Node:
    def __init__(self,val):
        self.data = val
        self.next = None

def construct(L1,L2,M):
    root1 = Node(L1[0])
    root2 = Node(L2[0])
    intersect = None
    curr1 = root1
    for i in range(1,len(L1)):
        if i == M:
            intersect = curr1
        curr1.next = Node(L1[i])
        curr1 = curr1.next
    curr2 = root2
    curr2.next = intersect
    return root1,root2

def length(root):
    count = 0
    while root:
        count += 1
        root = root.next
    return count

def intersection(root1,root2,l):
    for i in range(l):
        root1 = root1.next
    while root1 and root2:
        if root1 == root2:
            return root1.data
        root1 = root1.next
        root2 = root2.next
    return -1

def solution(N1,L1,N2,L2,M):
    # Write your code here...
    root1,root2 = construct(L1,L2,M)
    l1 = length(root1)
    l2 = length(root2)
    if l1 > l2:
        ret = intersection(root1,root2,l1-l2)
    else:
        ret = intersection(root2,root1,l2-l1)
    return ret
    
M = int(input())
N1=int(input())
L1 = list(map(int,input().split()))
N2 = int(input())
L2 = list(map(int,input().split()))
if N1 > N2:
    print(solution(N1,L1,N2,L2,M),end='')
else:
    print(solution(N2,L2,N1,L1,M),end='')