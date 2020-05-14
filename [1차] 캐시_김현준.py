def solution(cacheSize, cities):
    answer = 0
    cache = ['' for _ in range(cacheSize)]  # 캐시메모리 리스트
    if not cacheSize:   # 캐시사이즈가 0이면
        answer = len(cities)*5  # cache miss * 도시 개수
    else:
        for city in cities:
            city = city.lower() # 대소문자 구분 안하므로 소문자로 변환
            if city in cache:   # cache hit 일 때
                answer += 1
                cache.remove(city)
                cache.append(city)  # 도시 캐시 메모리 내 맨 뒤로 이동
            else:
                answer += 5     # cache miss일 때
                cache.pop(0)
                cache.append(city)  # 맨 앞에꺼 빼고 도시 추가
    return answer