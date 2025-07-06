import collections


class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        if k < 1:
            return False
        temp_deque = collections.deque()
        temp_set = set()
        temp_k = 0
        for n in nums:
            # print(f"n: {n}, temp_k: {temp_k}, temp_set: {temp_set}, temp_deque: {temp_deque}")
            temp_k += 1
            if temp_k > k+1:
                poped = temp_deque.popleft()
                temp_set.remove(poped)
                temp_k -= 1
            if n in temp_set:
                return True
            temp_set.add(n)
            temp_deque.append(n)
            
        return False


s = Solution()
print(s.containsNearbyDuplicate([1, 2, 3, 1], 3))  # True
