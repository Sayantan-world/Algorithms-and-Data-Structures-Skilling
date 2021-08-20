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

def isPalindrome(root):
    stack = []
    curr = root
    while curr:
        stack.append(curr.data)
        curr = curr.next
    while root:
        if root.data != stack.pop():
            return 0
        root = root.next
    return 1

def solution(L):
    # Write your code here...
    root = construct(L)
    return isPalindrome(root)

try:
    N=int(input())
    L=[]
    n=0
    for e in input().split():
        if(n<N):
            L.append(int (e))
            n+=1
    print(solution(L),end='')
except:
    print(1)