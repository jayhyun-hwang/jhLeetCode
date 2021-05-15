/*
 * @lc app=leetcode id=17 lang=golang
 *
 * [17] Letter Combinations of a Phone Number
 */

// @lc code=start
var nmap = map[byte][]rune{
	'2': {'a', 'b', 'c'},
	'3': {'d', 'e', 'f'},
	'4': {'g', 'h', 'i'},
	'5': {'j', 'k', 'l'},
	'6': {'m', 'n', 'o'},
	'7': {'p', 'q', 'r', 's'},
	'8': {'t', 'u', 'v'},
	'9': {'w', 'x', 'y', 'z'},
}
var resString = []string{}

func letterCombinations(digits string) []string {
	oneStr := []rune{}

	resString = recString(digits, 0, oneStr)
	return resString
}
func recString(digits string, idx int, oneStr []rune) []string {
	if idx == len(digits) {
		return resString
	}
	for _, valDigits := range nmap[digits[idx]] {
		oneStr = append(oneStr, valDigits)
		if idx == len(digits)-1 {
			resString = append(resString, string(oneStr))
		} else {
			resString = recString(digits, idx+1, oneStr)
		}
		oneStr = oneStr[:len(oneStr)-1]
	}
	return resString
}

// @lc code=end

