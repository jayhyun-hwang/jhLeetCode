/*
 * @lc app=leetcode id=326 lang=golang
 *
 * [326] Power of Three
 */

// @lc code=start
func isPowerOfThree(n int) bool {
	if n != 0 {
		return recLoop(n)
	}
	return false
}

func recLoop(n int) bool {
	if n == 1 {
		return true
	}
	if n%3 == 0 {
		return recLoop(n / 3)
	}
	return false
}

// @lc code=end

