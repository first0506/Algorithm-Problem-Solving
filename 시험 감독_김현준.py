N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())
ppl = N     # 필요한 감독관 수 = ppl (반에 한명의 총 감독관이 필요하므로 N으로 초기화)
for student in A:
    if student-B > 0:   #총감독관이 감시할 수 있는 응시자들의 빼고도 감시할 학생이 남아 있으면
        if (student-B)%C > 0:   # 부감독관 모두 C명씩 감시할 수 없으면 한 명은 C명보다 적은 응시자를 감시한다.
            ppl += ((student-B)//C)+1
        else:
            ppl +=  (student-B)//C  # 모든 부감독관이 C명씩 감시할 수 있을 때
print(ppl)