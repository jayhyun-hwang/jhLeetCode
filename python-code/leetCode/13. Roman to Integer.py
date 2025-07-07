class Solution:
    def romanToInt(self, s: str) -> int:
        value_map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        current = 0
        pre = ""
        for ele in s:
            if pre == "I":
                if ele == "V" or ele == "X":
                    current -= 2*value_map[pre]
            if pre == "X":
                if ele == "L" or ele == "C":
                    current -= 2*value_map[pre]
            if pre == "C":
                if ele == "D" or ele == "M":
                    current -= 2*value_map[pre]
            current += value_map[ele]
            pre = ele
        return current
