# def solution(k, room_number):
#     answer = [0]*len(room_number)
#     used = [0]*(k+1)
#     for i in range(len(room_number)):
#         if not used[room_number[i]]:
#             answer[i] = room_number[i]
#             used[room_number[i]] = 1
#         else:
#             for j in range(room_number[i]+1, k+1):
#                 if not used[j]:
#                     answer[i] = j
#                     used[j] = 1
#                     break
#     return answer

def solution(k, room_number):
    answer = [0]*len(room_number)
    rooms = [0]*(k+1)
    for i in range(len(room_number)):
        a = room_number[i]
        if rooms[a]:
            answer[i] = rooms[a]
        else:
            answer[i] = a
        b = answer[i]
        while 1:
            if not rooms[b]:
                rooms[b] = b+1
                break
            else:
                b = rooms[b]
        print(i, rooms)
    return answer

k = 10
room_number = [1,3,4,1,3,1]
print(solution(k, room_number))