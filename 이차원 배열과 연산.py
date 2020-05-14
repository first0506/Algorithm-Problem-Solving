def order(arr):
    if 0<= r-1 <len(arr) and 0<= c-1 <len(arr[0]) and arr[r-1][c-1] == k:
        return 0
    count = 1
    ans = -1
    while 1:
        flag = False
        if len(arr) < len(arr[0]):
            arr = rotate(arr)
            flag = True
        max_length = 0
        for i in range(len(arr)):
            v = [0]*101
            for m in arr[i]:
                v[m] += 1
            s = []
            for w in range(1, 101):
                if v[w]:
                    s.append([w, v[w]])
            j = []
            for idx in range(len(s)-1):
                idx1 = s[idx][0]
                cnt = s[idx][1]
                d = idx
                for n in range(idx+1, len(s)):
                    if s[n][1] < cnt:
                        idx1 = s[n][0]
                        cnt = s[n][1]
                        d = n
                    elif s[n][1] == cnt and s[n][0] < idx1:
                        idx1 = s[n][0]
                        cnt = s[n][1]
                        d = n
                s[idx], s[d] = s[d], s[idx]
                j.append(idx1)
                j.append(cnt)
            j.append(s[-1][0])
            j.append(s[-1][1])
            if len(j) > 100:
                j = j[:100]
                max_length = 100
            elif len(j) > max_length:
                max_length = len(j)
            arr[i] = j
        for i in arr:
            for _ in range(max_length-len(i)):
                i.append(0)
        if flag:
            arr = rotate(arr)
            arr = flip(arr)
        if 0<= r-1 <len(arr) and 0<= c-1 <len(arr[0]):
            if arr[r-1][c-1] == k:
                ans = count
                break
        if count >= 100:
            break
        count += 1
    return ans

def rotate(arr):
    arr1 = [[0]*len(arr) for _ in range(len(arr[0]))]
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            arr1[j][len(arr)-i-1] = arr[i][j]
    return arr1

def flip(arr):
    arr1 = [[0]*len(arr[0]) for _ in range(len(arr))]
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            arr1[i][len(arr[0])-1-j] = arr[i][j]
    return arr1

r, c, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(3)]
print(order(arr))