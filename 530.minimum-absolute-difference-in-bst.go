/*
 * @lc app=leetcode id=530 lang=golang
 *
 * [530] Minimum Absolute Difference in BST
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
var Min = 1000000

func getMinimumDifference(root *TreeNode) int {
	min := math.MaxInt64
	preVal := math.MinInt32

	helper := func(n *TreeNode) {}
	helper = func(n *TreeNode) {
		if n == nil {
			return
		}

		helper(n.Left)
		if preVal != math.MinInt32 {
			d := n.Val - preVal
			if d < min {
				min = d
			}
		}

		preVal = n.Val
		helper(n.Right)
	}

	helper(root)
	return min
}

// func getMinimumDifference(root *TreeNode) int {
// 	if root.Right != nil {
// 		if root.Right.Val-root.Val < Min {
// 			Min = root.Right.Val - root.Val
// 		}
// 		Min = getMinimumDifference(root.Right)
// 	}
// 	if root.Left != nil {
// 		if root.Val-root.Left.Val < Min {
// 			Min = root.Val - root.Left.Val
// 		}
// 		Min = getMinimumDifference(root.Left)
// 	}
// 	return Min
// }

// @lc code=end

