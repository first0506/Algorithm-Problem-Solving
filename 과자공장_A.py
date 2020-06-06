N, K = map(int, input().split())
snacks = []
for _ in range(N):
    snacks.append(float(input()))
start = 0
end = sum(snacks)/K
while start<=end:
    mid = (start+end)/2
    tmp = 0
    for s in snacks:
        tmp += s//mid
    if tmp >= K:
        start = mid+0.001
    else:
        end = mid-0.001
print('%.2f' %round(mid,2))

input =
2 3
6.3
4.3
result =
3.15

input =
18 300
51.28
96.87
96.86
48.63
87.83
51.29
56.72
38.05
3.88
79.40
33.43
30.75
13.12
67.80
20.15
96.71
95.93
10.91
result =
3.20