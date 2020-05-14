T = int(input())
for test_case in range(1, T+1):
    word = list(input())
    N = len(word)
    flag = True
    for i in range(N//2):
        if word[i]=="?" or word[N-i-1]=="?" or word[i]==word[N-i-1]:
            continue
        else:
            flag = False
            break
    if flag:
        print("#{} Exist".format(test_case))
    else:
        print("#{} Not exist".format(test_case))