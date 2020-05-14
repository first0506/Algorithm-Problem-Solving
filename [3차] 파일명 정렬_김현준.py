def solution(files):
    answer = []
    splits = []
    for i in files:
        a, b = 0, len(i)    # a = head와 number 경계 인덱스, b = number와 tail 경계
        for k in range(len(i)-1):   #각각의 파일 앞 철자부터 검사
            if not i[k].isdecimal() and i[k+1].isdecimal(): # 현재 인덱스 숫자아니고, 다음 인덱스 숫자이면,
                a = k
            elif i[k].isdecimal() and not i[k+1].isdecimal():   # 현재 인덱스 숫자고, 다음 인덱스 숫자아니면,
                b = k
                break   # b까지 찾으면 break
        splits.append([i[0:a+1], i[a+1:b+1], i[b+1::]]) # head number tail 쪼개서 리스트 형식으로 저장
    splits = sorted(splits, key = lambda x : (x[0].lower(), int(x[1]))) # 다중 정렬 조건 (대소문자 구분 없으므로 소문자로 만든다음 정렬)
    for i in splits:
        answer.append(i[0]+i[1]+i[2])   #쪼갠거 다시 합치기
    return answer

files = ['img12.png', 'img10.png', 'img02.png', 'img1.png', 'IMG01.GIF', 'img2.JPG']    # ['img1.png', 'IMG01.GIF', 'img02.png', 'img2.JPG', 'img10.png', 'img12.png']
# files = ['F-5 Freedom Fighter', 'B-50 Superfortress', 'A-10 Thunderbolt II', 'F-14 Tomcat'] # ['A-10 Thunderbolt II', 'B-50 Superfortress', 'F-5 Freedom Fighter', 'F-14 Tomcat']

print(solution(files))