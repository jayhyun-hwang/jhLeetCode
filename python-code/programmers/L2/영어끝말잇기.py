def solution(n, words):
    cur_idx = 0
    last = words[0][0]
    visited = set()
    order = 1
    while True:
        for num in range(1, n + 1):
            if cur_idx >= len(words):
                return [0, 0]
            word = words[cur_idx]
            if last != word[0] or word in visited:
                return [num, order]
            last = word[-1]
            cur_idx += 1
            visited.add(word)
        order += 1


print(solution(3, ["tank", "kick", "know", "wheel",
      "land", "dream", "mother", "robot", "tank"]))  # [3,3]
print(solution(5,	["hello", "observe", "effect", "take", "either", "recognize", "encourage",
      "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))  # [0,0]
print(solution(2,	["hello", "one", "even",
      "never", "now", "world", "draw"]))  # [1,3]
