inputs = [
    '2',
    '1',
    '2 0',
    '1',
    '1 0'
]


def input():
    return inputs.pop(0)


N = int(input())
evidence_groups = []

for _ in range(N):
    times = int(input())
    evidences = []
    for __ in range(times):
        evidences.append(list(map(int, input().split(' '))))
    evidence_groups.append(evidences)



result = 0
for i in range(2 ** N):
    honests = []
    for j in range(N):
        this_people_honest = ((i >> j) & 1)
        honests.append(this_people_honest)

    flag = False
    for j in range(N):
        talker = honests[j]
        if not talker:
            continue
        for evidence in evidence_groups[j]:
            people = evidence[0] - 1
            is_honest = evidence[1] == 1
            is_honest = is_honest if talker else (not is_honest)
            if honests[people] != is_honest:
                flag = True
                break
    if not flag:
        result = max(result, honests.count(True))
print(result)



