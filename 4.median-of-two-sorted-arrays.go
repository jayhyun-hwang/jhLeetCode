/*
 * @lc app=leetcode id=4 lang=golang
 *
 * [4] Median of Two Sorted Arrays
 */

@lc code=start
func findMedianSortedArrays(nums1 []int, nums2 []int) float64 {
	res := 0.0
	numsSum := append(nums1, nums2...)
	sort.Ints(numsSum)
	nlen := len(numsSum)
	median := int(nlen / 2)
	if nlen%2 != 0 {
		res = float64(numsSum[median])
	} else {
		res = float64(numsSum[median-1]+numsSum[median]) / 2
	}
	return res
}

// func findMedianSortedArrays(nums1 []int, nums2 []int) float64 {
// 	res := 0.0
// 	nums1 = append(nums1, nums2...)
// 	sort.Slice(nums1, func(i, j int) bool {
// 		return nums1[i] < nums1[j]
// 	})
// 	nlen := len(nums1)
// 	median := int(nlen / 2)
// 	if nlen%2 == 1 {
// 		res = float64(nums1[median])
// 	} else {
// 		res = float64(nums1[median-1]+nums1[median]) / 2
// 	}
// 	return res
// }

// @lc code=end

