def solution(answer_sheet, sheets):
    answer = 0
    check = [[0]*len(answer_sheet) for _ in range(len(sheets))]
    for i in range(len(answer_sheet)):
        for j in range(len(sheets)):
            if answer_sheet[i]!=sheets[j][i]:
                check[j][i] = sheets[j][i]
    print(check)
    for i in range(len(sheets)-1):
        for j in range(i+1, len(sheets)):
            a, b, max_b = 0, 0, 0
            for k in range(len(answer_sheet)):
                if 0!=check[i][k]==check[j][k]:
                    a += 1
                    b += 1
                else:
                    if b > max_b:
                        max_b = b
                    b = 0
            if b > max_b:
                max_b = b
            if answer < a + max_b**2:
                print(i, j, a, max_b**2)
                answer = a + max_b**2
    return answer

answer_sheet = "4132315142"
sheets = ["3241523133","4121314445","3243523133","4433325251","2412313253"]

# answer_sheet = "24551"
# sheets = ["24553", "24553", "24553", "24553"]

# answer_sheet = "53241"
# sheets = ["53241", "42133", "53241", "14354"]
print(solution(answer_sheet, sheets))