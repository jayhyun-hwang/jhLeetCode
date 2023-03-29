import unittest

def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    b_idx = 0
    for a in A:
        if b_idx >= len(B):
            break
        while True:
            if b_idx >= len(B):
                break
            if B[b_idx] > a:
                answer += 1
                b_idx += 1
                break
            b_idx += 1
    return answer


print(solution([5, 1, 3, 7], [2, 2, 6, 8]))  # 3
print(solution([2, 2, 2, 2], [1, 1, 1, 1]))  # 0
print(solution([2, 4, 6, 8], [1, 3, 5, 7]))  # 3

class TestSolution(unittest.TestCase):
    def test_solution_1(self):
        A = [1, 3, 5, 7]
        B = [2, 4, 6, 8]
        self.assertEqual(solution(A, B), 4)
    
    def test_solution_2(self):
        A = [2, 4, 6, 8]
        B = [1, 3, 5, 7]
        self.assertEqual(solution(A, B), 3)

if __name__ == '__main__':
    unittest.main()
