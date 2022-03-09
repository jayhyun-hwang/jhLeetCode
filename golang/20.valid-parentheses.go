/*
 * @lc app=leetcode id=20 lang=golang
 *
 * [20] Valid Parentheses
 */

// @lc code=start
func isValid(s string) bool {
	bmap := map[rune]rune{
		'{': '}',
		'[': ']',
		'(': ')',
	}
	sslice := make([]rune, 0)

	for _, val := range s {
		if mval, ok := bmap[val]; ok {
			sslice = append(sslice, mval)
		} else {
			if len(sslice) > 0 && val == sslice[len(sslice)-1] {
				sslice = sslice[:len(sslice)-1]
			} else {
				return false
			}
		}
	}
	if len(sslice) > 0 {
		return false
	}
	return true
}

// @lc code=end