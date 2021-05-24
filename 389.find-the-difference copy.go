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

	m := make(map[byte]int)
	for i := range s {
		m[s[i]]++
		// m[s[i]] |= 1
	}

	for i := range t {
		m[t[i]]--

		if m[t[i]] == -1 {
			return t[i]
		}
	}

	return t[0]
}

// @lc code=end