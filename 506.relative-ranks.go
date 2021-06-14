/*
 * @lc app=leetcode id=506 lang=golang
 *
 * [506] Relative Ranks
 */

// @lc code=start
func findRelativeRanks(score []int) []string {
	mp := make(map[int]string)
	res := make([]string, 0)
	scoreCopy := make([]int, len(score))
	copy(scoreCopy, score)
	sort.Slice(scoreCopy, func(i, j int) bool {
		return scoreCopy[i] > scoreCopy[j]
	})
	for idx, val := range scoreCopy {
		var ele string
		switch idx {
		case 0:
			ele = "Gold Medal"
		case 1:
			ele = "Silver Medal"
		case 2:
			ele = "Bronze Medal"
		default:
			ele = strconv.Itoa(idx + 1)
		}
		mp[val] = ele
	}
	for _, val := range score {
		res = append(res, mp[val])
	}
	return res
}

// @lc code=end

