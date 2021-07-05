/*
 * @lc app=leetcode id=551 lang=golang
 *
 * [551] Student Attendance Record I
 */

// @lc code=start
func checkRecord(s string) bool {
	absentCount := 0
	consecutiveLate := 0
	for _, val := range s {
		switch val {
		case 'L':
			consecutiveLate++
			if consecutiveLate > 2 {
				return false
			}
		case 'A':
			absentCount++
			if absentCount > 1 {
				return false
			}
			fallthrough
		default:
			consecutiveLate = 0
		}
	}
	return true
}

// 113/113 cases passed (0 ms)
// Your runtime beats 100 % of golang submissions
// Your memory usage beats 22.73 % of golang submissions (2 MB)

// @lc code=end

