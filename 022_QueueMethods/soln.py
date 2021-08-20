def dequeue(queue,res):
    if len(queue) != 0:
        item = queue.pop(0)
        res.append(item)

def enqueue(queue,val):
    queue.append(val)

def maxEle(queue,res):
    res.append(max(queue))

def solution(N,data,op):
    # Write your code here...
    queue = []
    res = []
    for i in range(N):
        if op[i] == 0:
            dequeue(queue,res)
        elif op[i] == 1:
            enqueue(queue,data[i])
        else:
            maxEle(queue,res)
    res.extend(queue)
    print(*res)
    
N = int(input())
data = list(map(int,input().split()))
op = list(map(int,input().split()))
solution(N,data,op)
