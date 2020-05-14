def solution(N, stages):
    cnt = [0]*(N+2) # 스테이지별 멈춰있는 사용자 수 리스트
    for i in stages:
        cnt[i] += 1
    dodal = cnt[-1] # 스테이지에 도달한 사용자 수
    for i in range(N, 0, -1):   # 마지막 스테이지부터 거꾸로 멈춰있는 사용자 수를 더하면 그 때 스테이지에 도달한 사용자 수가 된다.
        dodal += cnt[i]
        if dodal:   # 도달한 사용자가 있으면 cnt를 실패율로 저장
            cnt[i] = cnt[i]/dodal
    answer = [i[0]+1 for i in sorted(enumerate(cnt[1:N+1]), key=lambda x: -x[1])]   # 실패율순 정렬
    return answer

# N = 5
# stages = [2, 1, 2, 6, 2, 4, 3, 3]   # [3,4,2,1,5]
N = 4
stages = 	[4,4,4,4,4]     # [4,1,2,3]

print(solution(N, stages))