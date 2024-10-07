#
# @lc app=leetcode id=869 lang=python3
#
# [869] Reordered Power of 2
#

# @lc code=start
class Solution:
    def get_number_dict(self, num):
        ele_dict = dict()
        digit = 0
        while num > 0:
            r = num % 10
            if r not in ele_dict:
                ele_dict[r] = 0
            ele_dict[r] += 1
            digit += 1
            num = num // 10
        return [ele_dict, digit]

    def reorderedPowerOf2(self, n: int) -> bool:
        org_dict, org_digit = self.get_number_dict(n)

        temp_bin = 1
        while True:
            temp_dict, temp_digit = self.get_number_dict(temp_bin)
            temp_bin *= 2
            if org_digit > temp_digit:
                continue
            if org_digit < temp_digit:
                break

            early_return = False
            for k in temp_dict:
                if k not in org_dict or org_dict[k] != temp_dict[k]:
                    early_return = True
                    break
            if early_return == False:
                return True

        return False

# @lc code=end
