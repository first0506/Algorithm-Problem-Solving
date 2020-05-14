def f(n):
    a = b = 2**31-1
    if not n%3:
        a = v[n//3]
    if not n%2:
        b = v[n//2]
    c = v[n-1]
    v[n] = min(a, b, c) + 1     # a: 3으로 나눠떨어질 때, b: 2로 나눠떨어질때, c: 1 뺄 때 - 셋 중 최소값 + 1

N = int(input())
v = [0]*(N+1)   # 정수 X별 연산을 사용하는 최소 횟수 저장
for i in range(2, N+1):
    f(i)    # 2부터 N까지 최소 횟수 계산 후 저장
print(v[N])