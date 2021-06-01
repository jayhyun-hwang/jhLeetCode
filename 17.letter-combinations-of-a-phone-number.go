/*
 * @lc app=leetcode id=17 lang=golang
 *
 * [17] Letter Combinations of a Phone Number
 */

// @lc code=start
type constValue struct {
	//dial map
	nmap map[byte][]byte
	//res
	resultArr []string
	//1 string to check
	oneStr []byte
}

func letterCombinations(digits string) []string {
	if digits == "" {
		return nil
	}

	var constVal constValue
	//make dial map
	constVal.nmap = map[byte][]byte{
		'2': []byte{'a', 'b', 'c'},
		'3': []byte{'d', 'e', 'f'},
		'4': []byte{'g', 'h', 'i'},
		'5': []byte{'j', 'k', 'l'},
		'6': []byte{'m', 'n', 'o'},
		'7': []byte{'p', 'q', 'r', 's'},
		'8': []byte{'t', 'u', 'v'},
		'9': []byte{'w', 'x', 'y', 'z'},
	}

	constVal.resultArr = constVal.recString(digits, 0)
	return constVal.resultArr
}

func (constVal *constValue) recString(digits string, idx int) []string {
	if idx == len(digits) {
		return constVal.resultArr
	}
	for _, valDigits := range constVal.nmap[digits[idx]] {
		constVal.oneStr = append(constVal.oneStr, valDigits)
		if idx == len(digits)-1 {
			constVal.resultArr = append(constVal.resultArr, string(constVal.oneStr))
		} else {
			constVal.resultArr = constVal.recString(digits, idx+1)
		}
		constVal.oneStr = constVal.oneStr[:len(constVal.oneStr)-1]
	}
	return constVal.resultArr
}

// @lc code=end