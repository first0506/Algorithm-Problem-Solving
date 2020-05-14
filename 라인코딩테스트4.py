def solution(snapshots, transactions):
    answer = []
    snaps = {}
    v = [0]*len(transactions)
    for snap in snapshots:
        snaps[snap[0]] = int(snap[1])
    for trans in transactions:
        if not v[int(trans[0])]:
            v[int(trans[0])] = 1
            if trans[2] not in snaps:
                snaps[trans[2]] = 0
            if trans[1]=='SAVE':
                snaps[trans[2]] += int(trans[3])
            else:
                snaps[trans[2]] -= int(trans[3])
    for key, val in snaps.items():
        answer.append([key, str(val)])
    answer.sort()
    return answer

snapshots = [
["ACCOUNT3", "150"],
  ["ACCOUNT1", "100"],
  ["ACCOUNT2", "150"]
]
transactions = [
  ["1", "SAVE", "ACCOUNT2", "100"],
  ["2", "WITHDRAW", "ACCOUNT1", "50"],
  ["1", "SAVE", "ACCOUNT2", "100"],
  ["4", "SAVE", "ACCOUNT3", "500"],
  ["3", "WITHDRAW", "ACCOUNT2", "30"]
]
print(solution(snapshots, transactions))