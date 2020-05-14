N = int(input())
stairs = []
for _ in range(N):
    stairs.append([int(input())]*2) # stairs[바로 전 계단을 밟고 왔았을 때 최댓값, 전 전 계단을 밟고 왔을 떄 최댓값]
if N!=1:
    stairs[1][0] += max(stairs[0])  # 2번째 계단 예외처리
for i in range(2, N):
    stairs[i][0] += stairs[i-1][1]  # 바로 전 계단을 밟고 올 땐, 바로 전 계단의 전 전 계단을 밟고 왔을 때 최댓값을 더함
    stairs[i][1] += max(stairs[i-2])    # 전전계단을 발고 올 땐, 둘 중 큰 값을 더함
print(max(stairs[-1]))