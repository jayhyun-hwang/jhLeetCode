/*
 * @lc app=leetcode id=409 lang=golang
 *
 * [409] Longest Palindrome
 */

// @lc code=start
func longestPalindrome(s string) int {
	bArr := []byte(s)
	bmap := make(map[byte]int)
	minusCount := 0
	for _, val := range bArr {
		bmap[val]++
	}
	for _, val := range bmap {
		if val%2 == 1 {
			minusCount++
		}
	}
	if minusCount > 1 {
		return len(s) - minusCount + 1
	}
	return len(s)
}

// @lc code=end

