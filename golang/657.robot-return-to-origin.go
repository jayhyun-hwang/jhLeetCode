/*
 * @lc app=leetcode id=657 lang=golang
 *
 * [657] Robot Return to Origin
 */

// @lc code=start
func judgeCircle(moves string) bool {
	rl := 0
	ud := 0
	for _, val := range moves {
		switch val {
		case 'L':
			rl--
		case 'R':
			rl++
		case 'U':
			ud++
		case 'D':
			ud--
		}
	}
	res := false
	if rl == 0 && ud == 0 {
		res = true
	}
	return res
}

// @lc code=end