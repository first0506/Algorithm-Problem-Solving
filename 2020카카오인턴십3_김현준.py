def solution(gems):
    answer = []
    gems_set = list(set(gems))
    start = len(gems_set)
    end = len(gems)
    while start <= end:
        middle = (start+end)//2
        for i in range(0, len(gems)-middle+1):
            if set(gems[i:i+middle])==set(gems_set):
                answer = [i + 1, i + middle]
                end = middle-1
                break
        else:
            start = middle+1
    return answer

gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
# result = [3, 7]

# gems = ["AA", "AB", "AC", "AA", "AC"]
# # result = [1, 3]

# gems = ["XYZ", "XYZ", "XYZ"]
# # result = [1, 1]

# gems = ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]
# # result = [1, 5]

print(solution(gems))