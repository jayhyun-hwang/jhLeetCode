/*
 * @lc app=leetcode id=66 lang=golang
 *
 * [66] Plus One
 */

// @lc code=start
func plusOne(digits []int) []int {
	return isNine(digits, len(digits)-1)
}

func isNine(nlist []int, idx int) []int {
	if nlist[idx]+1 > 9 {
		nlist[idx] = 0
		if idx < 1 {
			nlist = append([]int{1}, nlist...)
		} else {
			return isNine(nlist, idx-1)
		}
	} else {
		nlist[idx] += 1
	}
	return nlist
}

// @lc code=end