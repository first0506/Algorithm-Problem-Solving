def perm(i, v):
    global min_val, max_val
    if i == N-1:
        val = cal(s)
        if min_val > val:
            min_val = val
        if max_val < val:
            max_val = val
    else:
        for m in range(N-1):
            if not v[m] and (m==0 or buho[m-1] != buho[m] or v[m-1]):
                s[i] = buho[m]
                v[m] = 1
                perm(i+1, v)
                v[m] = 0

def cal(s):
    result = nums[0]
    for i in range(N-1):
        if s[i] == 0:
            result += nums[i+1]
        elif s[i] == 1:
            result -= nums[i+1]
        elif s[i] == 2:
            result *= nums[i+1]
        elif s[i] == 3:
            if result >= 0:
                result = result//nums[i+1]
            else:
                result = -((-result)//nums[i+1])
    return result

N = int(input())
nums = list(map(int, input().split()))
buhos = list(map(int, input().split()))
buho = []
min_val = 1000000000
max_val = -1000000000
for i in range(4):
    for _ in range(buhos[i]):
        buho.append(i)
v = [0]*(N-1)
s = [0]*(N-1)
perm(0, v)
print(max_val)
print(min_val)