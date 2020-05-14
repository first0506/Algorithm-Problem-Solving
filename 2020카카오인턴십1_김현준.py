def solution(numbers, hand):
    answer = ''
    curleft = [3, 0]
    curright = [3, 2]
    for num in numbers:
        if not num:
            num = 11
        num -= 1
        if not num%3:
            answer += 'L'
            curleft = [num//3, num%3]
        elif num%3==2:
            answer += 'R'
            curright = [num//3, num%3]
        else:
            if abs(curleft[0]-num//3)+abs(curleft[1]-num%3) > abs(curright[0]-num//3)+abs(curright[1]-num%3):
                answer += 'R'
                curright = [num//3, num%3]
            elif abs(curleft[0]-num//3)+abs(curleft[1]-num%3) < abs(curright[0]-num//3)+abs(curright[1]-num%3):
                answer += 'L'
                curleft = [num//3, num%3]
            else:
                if hand=='left':
                    answer += 'L'
                    curleft = [num//3, num%3]
                else:
                    answer += 'R'
                    curright = [num//3, num%3]
    return answer

numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"
# result = "LRLLLRLLRRL"

# numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
# hand = "left"
# # result = "LRLLRRLLLRR"
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# hand = "right"
# # result = "LLRLLRLLRL"

print(solution(numbers, hand))