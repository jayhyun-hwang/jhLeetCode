/*
 * @lc app=leetcode id=448 lang=golang
 *
 * [448] Find All Numbers Disappeared in an Array
 */

// @lc code=start

func findDisappearedNumbers(nums []int) []int {
	iArr := make([]bool, len(nums))
	for i := 0; i < len(nums); i++ {
		iArr[nums[i]-1] = true
	}
	res := []int{}
	for i := 0; i < len(iArr); i++ {
		if !iArr[i] {
			res = append(res, i+1)
		}
	}
	return res
}

/*
func findDisappearedNumbers(nums []int) []int {

	imap := make(map[int]bool, len(nums))
	for _, val := range nums {
		imap[val] = true
	}
	res := []int{}
	for i := 1; i <= len(nums); i++ {
		if !imap[i] {
			res = append(res, i)
		}
	}
	return res
}
*/
// @lc code=end

