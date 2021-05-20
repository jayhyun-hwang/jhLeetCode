/*
 * @lc app=leetcode id=326 lang=golang
 *
 * [326] Power of Three
 */

// @lc code=start
func isPowerOfThree(n int) bool {
	if n != 0 {
		for {
			if n == 1 {
				return true
			}
			if n%3 == 0 {
				n /= 3
				continue
			}
			return false
		}
	}
	return false
}

// @lc code=end

