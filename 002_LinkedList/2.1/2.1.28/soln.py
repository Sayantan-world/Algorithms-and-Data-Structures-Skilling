class Node:
    def __init__(self,val):
        self.data = val
        self.next = None

def construct(L):
    root = Node(L[0])
    curr = root
    for i in range(1,len(L)):
        curr.next = Node(L[i])
        curr = curr.next
    return root

def merge(root1,root2):
    res = None
    if not root1:
        return root2
    if not root2:
        return root1
    if root1.data < root2.data:
        res = root1
        res.next = merge(root1.next,root2)
    else:
        res = root2
        res.next = merge(root1,root2.next)
    return res

def middle(root):
    if not root:
        return root
    slow,fast = root,root
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    return slow

def mergeSort(root):
    if not root or not root.next:
        return root
    mid = middle(root)
    afterMid = mid.next
    mid.next = None
    left = mergeSort(root)
    right = mergeSort(afterMid)
    ret = merge(left,right)
    return ret

def printList(root):
    while root:
        print(root.data,end=' ')
        root = root.next

def solution(L):
    # Write your code here...
    root = construct(L)
    root = mergeSort(root)
    printList(root)

try:
    N=int(input())
    L=[]
    n=0
    for e in input().split():
        if(n<N):
            L.append(int (e))
            n+=1
    solution(L)
except:
    print("no element present")