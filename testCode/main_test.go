package testCode

import (
	"sort"
	"testing"
)

//main
func TestMain(t *testing.T) {
}

func findMaxAverage(nums []int, k int) float64 {
	sort.Slice(nums, func(i, j int) bool {
		return nums[i] > nums[j]
	})
	if len(nums) > k {
		nums = nums[:k]
	}

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
