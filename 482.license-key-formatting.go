/*
 * @lc app=leetcode id=482 lang=golang
 *
 * [482] License Key Formatting
 */

// @lc code=start
func licenseKeyFormatting(s string, k int) string {
	s = strings.Replace(s, "-", "", -1)
	s = strings.ToUpper(s)
	mod := len(s) % k

	if mod == 0 {
		mod += k
	}
	for mod < len(s) {
		s = s[:mod] + "-" + s[mod:]
		mod += k + 1
	}
	return s
}

// func licenseKeyFormatting(s string, k int) string {
// 	idx := k
// 	needDash := true
// 	resR := make([]byte, 0)
// 	for i := 0; i < k; i++ {
// 		resR = append(resR, s[i])
// 		if s[i] == '-' {
// 			needDash = false
// 			idx = i
// 			break
// 		}
// 	}
// 	if needDash {
// 		resR = append(resR, '-')
// 	}
// 	count := 0
// 	for i := idx; i < len(s); i++ {
// 		switch {
// 		case s[i] == '-':
// 			continue
// 		case s[i] < 123 && s[i] > 96:
// 			resR = append(resR, s[i]-32)
// 			count++
// 		default:
// 			resR = append(resR, s[i])
// 			count++
// 		}
// 		if count == k {
// 			resR = append(resR, '-')
// 			count = 0
// 		}
// 	}
// 	if resR[len(resR)-1] == '-' {
// 		resR = resR[:len(resR)-1]
// 	}
// 	return string(resR)
// }

// @lc code=end

