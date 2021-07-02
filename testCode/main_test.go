package testCode

import (
	"testing"
)

//main
func TestMain(t *testing.T) {
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
