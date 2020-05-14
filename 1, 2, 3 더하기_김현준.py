def f(n):
    if n==1:
        return 1    # 1 만드는 방법 수
    elif n==2:
        return 2    # 2 만드는 방법 수
    elif n==3:
        return 4    # 3 만드는 방법 수
    else:
        return f(n-1)+f(n-2)+f(n-3)

T = int(input())
for _ in range(T):
    n = int(input())
    print(f(n))