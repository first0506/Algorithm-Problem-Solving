def perm():
    global tmp, ans
    if len(road)==len(customers):
        if ans > tmp + abs(home[0]-customers[road[-1]][0])+abs(home[1]-customers[road[-1]][1]):
            ans = tmp + abs(home[0]-customers[road[-1]][0])+abs(home[1]-customers[road[-1]][1])
    elif tmp < ans:
        for i in range(len(customers)):
            if i not in road:
                if len(road):
                    tmp += abs(customers[i][0]-customers[road[-1]][0])+abs(customers[i][1]-customers[road[-1]][1])
                else:
                    tmp += abs(customers[i][0]-company[0])+abs(customers[i][1]-company[1])
                road.append(i)
                perm()
                road.pop()
                if len(road):
                    tmp -= abs(customers[i][0]-customers[road[-1]][0])+abs(customers[i][1]-customers[road[-1]][1])
                else:
                    tmp -= abs(customers[i][0]-company[0])+abs(customers[i][1]-company[1])
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    a = list(map(int, input().split()))
    company = (a[0], a[1])
    home = (a[2], a[3])
    customers = []
    for i in range(4, len(a), 2):
        customers.append((a[i], a[i+1]))
    ans = 2**31-1
    road = []
    tmp = 0
    perm()
    print('#{} {}'.format(test_case, ans))