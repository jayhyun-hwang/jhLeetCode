/*
 * @lc app=leetcode id=643 lang=golang
 *
 * [643] Maximum Average Subarray I
 */

// @lc code=start
func findMaxAverage(nums []int, k int) float64 {
	idx := 0
	arrl := len(nums)
	maxSum := 0
	for i := 0; i < k; i++ {
		maxSum += nums[i]
	}
	tempSum := maxSum
	recFind := func() {}
	recFind = func() {
		if idx+k+1 > arrl {
			return
		}
		tempSum -= nums[idx]
		tempSum += nums[idx+k]
		if tempSum > maxSum {
			maxSum = tempSum
		}
		idx++
		recFind()
	}
	recFind()
	return float64(maxSum) / float64(k)
}

// func findMaxAverageNo(nums []int, k int) float64 {
// 	sort.Slice(nums, func(i, j int) bool {
// 		return nums[i] > nums[j]
// 	})
// 	if len(nums) > k {
// 		nums = nums[:k]
// 	}
// 	sum := 0
// 	for _, val := range nums {
// 		sum += val
// 	}
// 	res := float64(sum) / float64(k)
// 	return res
// }

// @lc code=end

// func findMaxAverage(nums []int, k int) float64 {
// 	sum := 0
// 	// sum up to first k
// 	for i := 0; i < k; i++ {
// 		sum += nums[i]
// 	}

// 	max := sum
// 	pointer := k

// 	for pointer < len(nums) {
// 		sum = sum - nums[pointer-k] + nums[pointer]
// 		if sum > max {
// 			max = sum
// 		}
// 		pointer++
// 	}

// 	return float64(max) / float64(k)
// }