def solution(k, room_number):
    answer = []
    rooms = {}      # key: 배정받은 room 번호, value: key와 같은 room을 원할 때 다음 room 번호
    def addroom(room):
        if room in rooms:   # 이미 배정이 되어 있으면
            i = rooms[room]
            while i in rooms:   # 다음 배정 가능 방 찾기
                i = rooms[i]
            rooms[i] = i+1  # 배정가능방에 배정하고, 다음 배정방 저장
            j = i+1
            i = room    # 다시 처음으로 돌아가서
            while rooms[i]!=j:  # 지나온 방들마다 다음 배정방 바꿔주기
                k = rooms[i]
                rooms[i] = j
                i = k
        else:
            rooms[room] = room+1    # 배정이 안되어 있으면 배정
    for i in room_number:
        addroom(i)
    for key in rooms.keys():    # 딕셔너리 순서대로 key값 받기
        answer.append(key)
    return answer

# def solution(k, room_number):
#     answer = []
#     rooms = {}
#     class node:
#         def __init__(self, next):
#             self.next = next
#     def addroom(room):
#         if room in rooms:
#             i = rooms[room].next
#             while i in rooms:
#                 i = rooms[i].next
#             rooms[i] = node(i+1)
#             j = i+1
#             i = room
#             while rooms[i].next!=j:
#                 k = rooms[i].next
#                 rooms[i].next = j
#                 i = k
#         else:
#             rooms[room] = node(room+1)
#     for i in room_number:
#         addroom(i)
#     for key in rooms.keys():
#         answer.append(key)
#     return answer

k = 10
room_number = [1,3,4,1,3,1]     # 	[1,3,4,2,5,6]

print(solution(k, room_number))