/*
 * @lc app=leetcode id=20 lang=golang
 *
 * [20] Valid Parentheses
 */

// @lc code=start
func isValid(s string) bool {

	dept := 0
	dmap := make(map[int]byte)
	checkBrackets := map[byte]byte{
		'{': '}',
		'(': ')',
		'[': ']',
	}
	for i := 0; i < len(s); i++ {
		switch s[i] {
		case '[', '{', '(':
			dept++
			dmap[dept] = checkBrackets[s[i]]
		case ']', '}', ')':
			if s[i] == dmap[dept] {
				delete(dmap, dept)
				dept--
			} else {
				return false
			}
		}
	}
	if dept != 0 {
		return false
	}
	return true
}

// @lc code=end