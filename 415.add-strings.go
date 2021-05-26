/*
 * @lc app=leetcode id=415 lang=golang
 *
 * [415] Add Strings
 */

// @lc code=start
func addStrings(num1 string, num2 string) string {
	conNum1, _ := strconv.ParseFloat(num1, 64)
	conNum2, _ := strconv.ParseFloat(num2, 64)
	res := fmt.Sprintf("%f", conNum1+conNum2)
	return res[:len(res)-7]
}

// @lc code=end

