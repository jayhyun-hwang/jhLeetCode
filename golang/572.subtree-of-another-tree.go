/*
 * @lc app=leetcode id=572 lang=golang
 *
 * [572] Subtree of Another Tree
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
func isSubtree(root *TreeNode, subRoot *TreeNode) bool {
	findSub := func() {}
	findSub = func(r *TreeNode, s *TreeNode) bool {
		if s == nil {
			
		}
		if r.Val == s.Val {
			r.
		}else {
		}
		return true
	}
}
// func isSubtree(s *TreeNode, t *TreeNode) bool {
//     if isSameTree(s, t) {
//         return true
//     }
//     if s == nil {
//         return false
//     }
//     if isSubtree(s.Left, t) || isSubtree(s.Right, t) {
//         return true
//     }
//     return false
// }

// func isSameTree(t1 *TreeNode, t2 *TreeNode) bool {
//     if t1 == nil && t2 == nil {
//         return true
//     }
//     if t1 == nil || t2 == nil {
//         return false
//     }
//     if t1.Val != t2.Val {
//         return false
//     }
//     return isSameTree(t1.Left, t2.Left) && isSameTree(t1.Right, t2.Right)
// }
// @lc code=end

