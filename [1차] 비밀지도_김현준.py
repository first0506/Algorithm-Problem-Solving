def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        a, b = bin(arr1[i])[2:], bin(arr2[i])[2:]   # 지도 1, 지도 2 2진수로 변환
        if len(a) < n:
            a = "0"*(n-len(a))+a    # 2진수 길이가 n보다 짧으면 앞에 0채우기
        if len(b) < n:
            b = "0"*(n-len(b))+b
        result = ""
        for k in range(n):
            if a[k]=="1" or b[k]=="1":  # 같은 위치 둘 중에 하나라도 벽이면
                result = result+"#" # '#'
            else:
                result = result+" " # 아니면 빈칸
        answer.append(result)
    return answer