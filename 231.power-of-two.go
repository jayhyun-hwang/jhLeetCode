/*
 * @lc app=leetcode id=231 lang=golang
 *
 * [231] Power of Two
 */

// @lc code=start
func isPowerOfTwo(n int) bool {
	if n != 0 {
		return recLoop(n)
	}
	return false
}

func recLoop(n int) bool {
	if n == 1 {
		return true
	}
	if n%2 == 0 {
		return recLoop(n / 2)
	} else {
		return false
	}
}

// @lc code=end

