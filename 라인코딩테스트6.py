def solution(directory, command):
    answer = []
    for c in command:
        c1 = c.split()
        if c1[0]=='mkdir':
            directory.append(c1[1])
        elif c1[0] == 'rm':
            for i in range(len(directory)-1, -1, -1):
                if c1[1] == directory[i][:len(c1[1])]:
                    directory.remove(directory[i])
        elif c1[0] == 'cp':
            for i in range(len(directory)):
                if directory[i][:len(c1[1])] == c1[1]:
                    low = directory[i][len(c1[1])-len(c1[1].split('/')[-1])-1:]
                    if c1[2]=='/':
                        directory.append(low)
                    else:
                        directory.append(c1[2]+low)
    return sorted(directory)

directory = [
"/",
"/hello",
"/hello/tmp",
"/root",
"/root/abcd",
"/root/abcd/etc",
"/root/abcd/hello"
]
command = [
"mkdir /root/tmp",
"cp /hello /root/tmp",
"rm /hello"
]

# directory = [
# "/"
# ]
# command = [
# "mkdir /a",
# "mkdir /a/b",
# "mkdir /a/b/c",
# "cp /a/b /",
# "rm /a/b/c"
# ]
print(solution(directory, command))