N = int(input())
house = []
for i in range(N):
    R, G, B = map(int, input().split())
    house.append([R, G, B])
for i in range(1, N):
    house[i][0] += min(house[i-1][1],house[i-1][2])
    house[i][1] += min(house[i-1][0], house[i-1][2])
    house[i][2] += min(house[i-1][0], house[i-1][1])
print(min(house[N-1][0], house[N-1][1], house[N-1][2]))