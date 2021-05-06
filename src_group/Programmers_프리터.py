# priorities = [2,1,3,2]
# location = 2
priorities = [1, 1, 9, 1, 1, 1]
location = 0


queue = [(i,p) for i,p in enumerate(priorities)]
print(queue)
answer = 0

while True:
    cur = queue.pop(0)
    if any(cur[1]<q[1] for q in queue):
        queue.append(cur)
    else:
        answer += 1
        if cur[0] == location:
            break

print(answer)