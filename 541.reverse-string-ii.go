/*
 * @lc app=leetcode id=541 lang=golang
 *
 * [541] Reverse String II
 */

// @lc code=start
func reverseStr(s string, k int) string {
	asc := false
	var res []rune
	temp := make([]rune, k)
	findStr := func() {}
	findStr = func() {
		if len(s) <= k {
			if asc {
				res = append(res, []rune(s)...)
			} else {
				temp = []rune(s)
				for i, j := 0, len(temp)-1; i < j; i, j = i+1, j-1 {
					temp[i], temp[j] = temp[j], temp[i]
				}
				res = append(res, temp...)
			}
			return
		}
		temp = []rune(s[:k])
		if asc {
			res = append(res, temp...)
		} else {
			for i, j := 0, len(temp)-1; i < j; i, j = i+1, j-1 {
				temp[i], temp[j] = temp[j], temp[i]
			}
			res = append(res, temp...)
		}
		s = s[k:]
		asc = !asc
		findStr()
	}
	findStr()
	return string(res)
}

// func reverseStr(s string, k int) string {
// 	res := []byte(s)
// 	for i := 0; i < len(res); i = i + 2*k {
// 		if i+k < len(res) {
// 			reverseK(res[i : i+k])
// 		} else {
// 			reverseK(res[i:])
// 		}
// 	}
// 	return string(res)
// }

// // reverse slice
// func reverseK(b []byte) {
// 	left, right := 0, len(b)-1
// 	for left < right {
// 		b[left], b[right] = b[right], b[left]
// 		left, right = left+1, right-1
// 	}
// }

// @lc code=end

