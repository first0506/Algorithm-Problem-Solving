user_input = input()
# user_input = 'adfkdncjdk'
# # result = 'LEVEL2'
# user_input = 'Aei0#'
# # result = 'LEVEL4'
# user_input = 'aq%~9P2!@@s!v#&&KM^lFf'
# # result = 'LEVEL5'
level = [0]*5
for i in user_input:
    if 97<=ord(i)<=122:
        level[0] = 1
    elif 65<=ord(i)<=90:
        level[1] = 1
    elif i.isdigit():
        level[2] = 1
    else:
        level[3] = 1
if len(user_input) >= 10:
    level[4] = 1
print('LEVEL{}'.format(int(sum(level))))

