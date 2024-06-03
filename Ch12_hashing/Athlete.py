def solution(participant, completion):
    hash_table = {}

    for person in participant:
        if person in hash_table:
            hash_table[person] += 1
        else:
            hash_table[person] = 1

    for person in completion:
        if person in hash_table:
            hash_table[person] -= 1

    for person in hash_table:
        if hash_table[person] == 1:
            return person


# 예제 입력
participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]
print(solution(participant, completion))  # 출력: "leo"

participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
completion = ["josipa", "filipa", "marina", "nikola"]
print(solution(participant, completion))  # 출력: "vinko"

participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]
print(solution(participant, completion))  # 출력: "mislav"
