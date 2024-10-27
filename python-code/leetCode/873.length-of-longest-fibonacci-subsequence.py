#
# @lc app=leetcode id=873 lang=python3
#
# [873] Length of Longest Fibonacci Subsequence
#

class Solution:
    def lenLongestFibSubseq(self, arr):
        arr_set = set(arr)
        # visited = set()
        max_count = 0
        arr_len = len(arr)
        for idx, val in enumerate(arr):
            # if val in visited or idx + 1 >= arr_len - 1:
            if idx + 1 >= arr_len - 1:
                continue
            for j in range(idx + 1, arr_len):
                val2 = arr[j]
                # if val2 in visited:
                #     continue
                a, b = val, val2
                tmp_pb = [a, b]
                while True:
                    if a + b not in arr_set:
                        break
                    a, b = b, a + b
                    # visited.add(b)
                    tmp_pb.append(b)
                if len(tmp_pb) > 2:
                    # print(tmp_pb)
                    max_count = max(len(tmp_pb), max_count)
        return max_count


print(Solution().lenLongestFibSubseq([2, 5, 6, 7, 8, 10, 12, 17, 24, 41, 65]))
