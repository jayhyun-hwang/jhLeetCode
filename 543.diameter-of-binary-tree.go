/*
 * @lc app=leetcode id=543 lang=golang
 *
 * [543] Diameter of Binary Tree
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
type DiamHeight struct {
	diam, height int
}

func diameterOfBinaryTree(root *TreeNode) int {
	dh := diamHeight(root)
	return dh.diam
}
func diamHeight(root *TreeNode) DiamHeight {
	dh := DiamHeight{0, -1}
	if root == nil {
		return dh
	}
	dhl := diamHeight(root.Left)
	dhr := diamHeight(root.Right)
	diameterWithRoot := 0
	if root.Left != nil {
		diameterWithRoot += 1 + dhl.height // only required if left node is present
	}
	if root.Right != nil {
		diameterWithRoot += 1 + dhr.height // only required if right node is present
	}
	dh.diam = maxOf3(dhl.diam, dhr.diam, diameterWithRoot)
	dh.height = 1 + maxOf2(dhl.height, dhr.height)
	return dh
}
func maxOf3(a, b, c int) int {
	if a > b && a > c {
		return a
	}
	if b > c {
		return b
	}
	return c
}
func maxOf2(a, b int) int {
	if a > b {
		return a
	}
	return b
}

// @lc code=end

