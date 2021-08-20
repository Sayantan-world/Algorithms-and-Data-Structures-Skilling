def enqueue(queue,value):
    queue.append(value)
    #print("enqueue")

def dequeue(queue):
    if len(queue) != 0:
        item = queue.pop(0)
        #print(item)

def size(queue):
    print("Queue size is {0}".format(len(queue)))

def search(queue,item):
    flag = False
    for i in queue:
        if i == item:
            flag = True
            print("{0} is found".format(item))
            break
    if not flag:
        print("{0} is not found".format(item))

def display(queue):
    if not len(queue):
        print("Queue is empty")
    else:
        for i in queue:
            print(i,end = ' ')
        print()

def solution(N,val,op):
    # Write your code here...
    queue = []
    for i in range(N):
        if op[i] == 0:
            dequeue(queue)
        elif op[i] == 1:
            enqueue(queue,val[i])
        elif op[i] == 2:
            size(queue)
        elif op[i] == 3:
            search(queue,val[i])
        else:
            display(queue)
        #print(queue)
    
N = int(input())
val = list(map(int,input().split()))
op = list(map(int,input().split()))
solution(N,val,op)
