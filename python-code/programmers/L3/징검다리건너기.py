def solution(stones, k):
    if len(stones) == 1 or len(stones) == k:
        return min(stones)
    answer = 0
    left = 0
    min_current_max = 200_000_001
    def get_max(start_idx, end_idx, cur_max):
        if stones[start_idx-1] != cur_max:
            return max(cur_max, stones[end_idx - 1])
        cur_max = 0
        for idx in range(start_idx, end_idx):
            if stones[idx] > cur_max:
                cur_max = stones[idx]
        return cur_max
    current_max = max(stones[left:left + k])
    while True:
        left += 1
        right = left + k
        if right > len(stones):
            break
        current_max = get_max(left, right, current_max)
        if current_max < min_current_max:
            min_current_max = current_max
    answer = min_current_max
    return answer