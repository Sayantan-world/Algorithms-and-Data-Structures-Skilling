# Write your code here...
N = int(input())
data = list(map(int,input().split()))
priority = list(map(int,input().split()))
op = list(map(int,input().split()))

queue,priority_list = [],[]
for i in range(N):
    if op[i] == 1:
        queue.append(data[i])
        priority_list.append(priority[i])
    else:
        if len(queue) != 0:
            mi = min(priority_list)
            i = 0
            while priority_list[i] != mi:
                i += 1
            queue.pop(i)
            priority_list.pop(i)
zipped = zip(priority_list,queue)
sorted_queue = [val for p,val in sorted(zipped)]
print(*sorted_queue)
