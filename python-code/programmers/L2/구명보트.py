def solution(people, limit):
    sorted_people = sorted(people)
    l_idx = 0
    r_idx = len(sorted_people) - 1
    count = 0
    while l_idx <= r_idx:
        left = sorted_people[l_idx]
        right = sorted_people[r_idx]
        count += 1
        if right + left > limit:
            r_idx -= 1
            continue
        l_idx += 1
        r_idx -= 1
    return count


print(solution([70, 50, 80, 50],	100))  # 3
print(solution([70, 80, 50],	100))  # 3
