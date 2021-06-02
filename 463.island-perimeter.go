/*
 * @lc app=leetcode id=463 lang=golang
 *
 * [463] Island Perimeter
 */

// @lc code=start
type Obj struct {
	
	before []int
	visited map[[][]int]bool
	rowLen int
	colLen int
	res int
}
func islandPerimeter(grid [][]int) int {
    obj := new(Obj)
	obj.
}

func findPer() {
	//up, right, down, left Traversal
	//if value == 1, check the sides. 
	//if side == 0, res++
	//when checked, insert visited map
	//move next island. if visited, find not visited, 
}
// @lc code=end

