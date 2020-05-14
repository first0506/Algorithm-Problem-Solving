def check(player, n):
    if player[n]>=3 or (n>1 and 0 not in player[n-2:n+1]) or (0<n<9 and 0 not in player[n-1:n+2]) or (n<8 and 0 not in player[n:n+3]):
        return True
    return False

T = int(input())
for test_case in range(1, T+1):
    player1 = [0]*10
    player2 = [0]*10
    ans = 0
    nums = list(map(int, input().split()))
    for i in range(0, 12, 2):
        player1[nums[i]] += 1
        if check(player1, nums[i]):
            ans = 1
            break
        player2[nums[i+1]] += 1
        if check(player2, nums[i+1]):
            ans = 2
            break
    print('#{} {}'.format(test_case, ans))