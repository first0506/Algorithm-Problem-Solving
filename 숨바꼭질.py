def find():
    queue = [[N, 0]]
    v = [0]*100001
    v[N] = 1
    while queue:
        position, time = queue.pop(0)
        if position == K:
            return time
        if 0<=position+1<=100000 and not v[position+1]:
            queue.append([position+1, time+1])
            v[position+1] = 1
        if 0<=position-1<=100000 and not v[position-1]:
            queue.append([position-1, time+1])
            v[position-1] = 1
        if 0<=position*2<=100000 and not v[position*2]:
            queue.append([position*2, time+1])
            v[position*2] = 1

N, K = map(int, input().split())
print(find())