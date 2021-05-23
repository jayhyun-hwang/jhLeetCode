/*
 * @lc app=leetcode id=389 lang=golang
 *
 * [389] Find the Difference
 */

// @lc code=start
func findTheDifference(s string, t string) byte {
	if len(s) == 0 {
		return t[0]
	}
	for i := 0; i < len(s); i++ {
		if s[i] != t[i] {
			return t[i]
		}
	}
	return t[len(s)]
}

// @lc code=end

