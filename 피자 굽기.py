def wheel(i):
    cheese = pizza[i]
    if cheese >= 16:
        return 5
    elif cheese >= 8:
        return 4
    elif cheese >= 4:
        return 3
    elif cheese >= 2:
        return 2
    else:
        return 1

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    pizza = [0]+list(map(int, input().split()))
    for i in range(1, M+1):
        pizza[i] = wheel(i)
    pan = [0]*N
    position = -1
    for i in range(1, M+1):
        while 1:
            position = (position+1) % N
            if not pan[position]:
                pan[position] = i
                break
            else:
                pizza[pan[position]] -= 1
                if not pizza[pan[position]]:
                    pan[position] = i
                    break
    max_wheel = max(pizza)
    for i in range(N):
        if pizza[pan[(position-i)%N]] == max_wheel:
            print('#{} {}'.format(test_case, pan[(position-i)%N]))
            break