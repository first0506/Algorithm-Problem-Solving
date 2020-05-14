T = int(input())
for test_case in range(1, T+1):
    N, num = input().split()
    a = str(bin(int('0x'+num, 16))[2::])
    a = '0'*(int(N)*4-len(a))+a
    print('#{} {}'.format(test_case, a))

# 3
# 4 47FE
# 5 79E12
# 8 41DA16CD

# T = int(input())
# for test_case in range(1, T+1):
#     N, num = input().split()
#     N=int(N)
#     change = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
#     result = 0
#     ans=''
#     for i in range(N):
#         for j in range(16):
#             if change[j]==num[i]:
#                 break
#         tmp=''
#         for k in range(4):
#             if j&(1<<k):
#                 tmp = '1'+tmp
#             else:
#                 tmp = '0'+tmp
#         ans += tmp
#     print('#{} {}'.format(test_case, ans))