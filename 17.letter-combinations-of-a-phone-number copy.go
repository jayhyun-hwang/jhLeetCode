/*
 * @lc app=leetcode id=17 lang=golang
 *
 * [17] Letter Combinations of a Phone Number
 */

// @lc code=start
func letterCombinations(digits string) []string {
	if digits == "" {
		return nil
	}
	nmap := map[byte][]byte{
		'2': []byte{'a', 'b', 'c'},
		'3': []byte{'d', 'e', 'f'},
		'4': []byte{'g', 'h', 'i'},
		'5': []byte{'j', 'k', 'l'},
		'6': []byte{'m', 'n', 'o'},
		'7': []byte{'p', 'q', 'r', 's'},
		'8': []byte{'t', 'u', 'v'},
		'9': []byte{'w', 'x', 'y', 'z'},
	}
	var resultArr []string
	oneStr := []byte{}

	return recString(nmap, digits, 0, oneStr, &resultArr)
}
func recString(nmap map[byte][]byte, digits string, idx int, oneStr []byte, resultArr *[]string) []string {
	if idx == len(digits) {
		return *resultArr
	}

	for _, valDigits := range nmap[digits[idx]] {
		oneStr = append(oneStr, valDigits)
		if idx == len(digits)-1 {
			*resultArr = append(*resultArr, string(oneStr))
		} else {
			*resultArr = recString(nmap, digits, idx+1, oneStr, resultArr)
		}
		oneStr = oneStr[:len(oneStr)-1]
	}
	return *resultArr
}

// @lc code=end