/*
 * @lc app=leetcode id=485 lang=golang
 *
 * [485] Max Consecutive Ones
 */

// @lc code=start
type Obj struct {
	maxNum int
}

func (obj *Obj) compare(n int) {
	if n > obj.maxNum {
		obj.maxNum = n
	}
}
func findMaxConsecutiveOnes(nums []int) int {
	obj := new(Obj)
	count := 0
	nums = append(nums, 0)
	for _, num := range nums {
		if num == 1 {
			count++
		} else {
			obj.compare(count)
			count = 0
		}
	}
	return obj.maxNum
}

// 42/42 cases passed (36 ms)
// Your runtime beats 91.69 % of golang submissions
// Your memory usage beats 7.05 % of golang submissions (6.7 MB)

// func findMaxConsecutiveOnes(nums []int) int {
//     var maxNum int
// 	count := 0
// 	nums = append(nums, 0)
// 	for _, num := range nums {
// 		if num == 1 {
// 			count++
// 		} else {
//             if count > maxNum {
//                 maxNum = count
//             }
// 			count = 0
// 		}

// 	}
// 	return maxNum
// }

// @lc code=end