/*
 * @lc app=leetcode id=541 lang=golang
 *
 * [541] Reverse String II
 */

// @lc code=start
func reverseStr(s string, k int) string {
	asc := false
	var res string
	findStr := func() {}
	findStr = func() {
		if len(s) <= k {
			if asc {
				res += s
			} else {
				for i, j := 0, len([]rune(s))-1; i < j; i, j = i+1, j-1 {
					[]rune(s)[i], []rune(s)[j] = []rune(s)[j], []rune(s)[i]
				}
				res += s
			}
			return
		}
		temp := s[:k]
		if asc {
			res += temp
		} else {
			for i, j := 0, len([]rune(temp))-1; i < j; i, j = i+1, j-1 {
				[]rune(temp)[i], []rune(temp)[j] = []rune(temp)[j], []rune(temp)[i]
			}
			res += temp
		}
		s = s[k:]
		findStr()
	}
	return res
}

// @lc code=end

