/*
 * @lc app=leetcode id=20 lang=golang
 *
 * [20] Valid Parentheses
 */

// @lc code=start
func isValid(s string) bool {

	dept := 0
	dmap := make(map[int]string)
	for i := 0; i < len(s); i++ {
		switch string(s[i]) {
		case "[", "{", "(":
			dept++
			dmap[dept] = checkBrackets(string(s[i]))
		case "]", "}", ")":
			if string(s[i]) != dmap[dept] {
				return false
			} else {
				delete(dmap, dept)
				dept--
			}
		}
	}
	return true
	/*dept := 0
	expectedValue := ""
	dmap := make(map[int]string)
	for i := 0; i < len(s); i++ {
		switch string(s[i]) {
		case "[", "{", "(":
			dept++
			expectedValue = checkBrackets(string(s[i]))
			dmap[dept] = expectedValue
		case "]", "}", ")":
			if string(s[i]) != expectedValue {
				return false
			} else {
				delete(dmap, dept)
				dept--
				expectedValue = dmap[dept]
			}
		}
	}
	return true*/
}

func checkBrackets(start string) string {
	var end string
	switch start {
	case "(":
		end = ")"
	case "[":
		end = "]"
	case "{":
		end = "}"
	}
	return end
}

// @lc code=end


