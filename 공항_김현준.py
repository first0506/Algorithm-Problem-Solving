def addplane(g):
    global ans
    if g in gates:
        i = gates[g]
        while i in gates:
            i = gates[i]
        gates[i] = i-1
        if not i:   # 다음 가능 게이트가 0이면 더이상 불가능하므로  return False
            return False
        j = i-1
        i = g
        while gates[i]!=j:      # 나머지는 호텔방 배정과 동일
            k = gates[i]
            gates[i] = j
            i = k
    else:
        gates[g] = g-1
    ans += 1
    return True


G = int(input())
P = int(input())
ans = 0
gates = {}  # 공항 게이트:다음 공항 게이트
for i in range(P):
    g = int(input())
    if not addplane(g):
        break
print(ans)