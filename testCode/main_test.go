package testCode

import (
	"sort"
	"testing"
)

//main
func TestMain(t *testing.T) {
	findMaxAverage([]int{1, 12, -5, -6, 50, 3}, 4)
}
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
		if idx+k > arrl {
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
func findMaxAverageNno(nums []int, k int) float64 {
	sort.Slice(nums, func(i, j int) bool {
		return nums[i] > nums[j]
	})
	if len(nums) > k {
		nums = nums[:k]
	}
	sum := 0
	for _, val := range nums {
		sum += val
	}
	res := float64(sum) / float64(k)
	return res
}
func isSubtree(root *TreeNode, subRoot *TreeNode) bool {
	// findSub := func(r *TreeNode, s *TreeNode) {}
	// findSub = func(r *TreeNode, s *TreeNode) {

	// 	res = true
	// }
	// findSub(root, subRoot)
	if isSame(root, subRoot) {
		if subRoot.Left != nil {
			isSame(root.Left, subRoot.Left)
		}
		if subRoot.Right != nil {
			isSame(root.Right, subRoot.Right)
		}
	}
	return false
}
func isSame(r *TreeNode, s *TreeNode) bool {
	if r.Val == s.Val {
		return true
	}
	return false
}

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func diameterOfBinaryTree(root *TreeNode) int {
	leftDepth := 0
	findDepth := func(node *TreeNode) {}
	findDepth = func(node *TreeNode) {
		if root.Left != nil {
			leftDepth++
		}

	}
	findDepth(root)
	return 0
}

// func findMedianSortedArrays(nums1 []int, nums2 []int) float64 {
// 	res := 0.0
// 	numsSum := append(nums1, nums2...)
// 	sort.Ints(numsSum)
// 	nlen := len(numsSum)
// 	median := int(nlen / 2)
// 	if nlen%2 != 0 {
// 		res = float64(numsSum[median])
// 	} else {
// 		res = float64(numsSum[median-1]+numsSum[median]) / 2
// 	}
// 	return res
// }

// func findMedianSortedArrays(nums1 []int, nums2 []int) float64 {
// 	mp := make(map[int]bool)
// 	numsSum := make([]int, 0)
// 	res := 0.0
// 	for _, val := range nums1 {
// 		if !mp[val] {
// 			numsSum = append(numsSum, val)
// 			mp[val] = true
// 		}
// 	}
// 	for _, val := range nums2 {
// 		if !mp[val] {
// 			numsSum = append(numsSum, val)
// 			mp[val] = true
// 		}
// 	}
// 	sort.Slice(numsSum, func(i, j int) bool {
// 		return numsSum[i] < numsSum[j]
// 	})
// 	nlen := len(numsSum)
// 	median := int(nlen / 2)
// 	if nlen%2 == 1 {
// 		res = float64(numsSum[median])
// 	} else {
// 		res = float64(numsSum[median-1]+numsSum[median]) / 2
// 	}
// 	return res
// }

// tf := "test param" //test function here
// tf := "ghdfasdf" //test function here
// bArr := []byte(tf)
// fmt.Println("value = ", bArr)
// s := string(bArr)
// fmt.Println("value = ", s)
// str := "abcabcabcd"
// sStr := strings.Split(str, str[:1])
// fmt.Println(sStr)
