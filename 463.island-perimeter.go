/*
 * @lc app=leetcode id=463 lang=golang
 *
 * [463] Island Perimeter
 */

// @lc code=start
type Obj struct {
	grid   [][]int
	rowLen int
	colLen int
	res    int
}

func islandPerimeter(grid [][]int) int {
	obj := new(Obj)
	obj.grid = grid
	obj.rowLen = len(grid)
	obj.colLen = len(grid[0])

	obj.recCol(0, 0)
	return obj.res
}

func (obj *Obj) recCol(r int, c int) {
	if r >= obj.rowLen {
		return
	}
	obj.recRow(r, c)
	obj.recCol(r+1, c)
}
func (obj *Obj) recRow(r int, c int) {
	if c >= obj.colLen {
		return
	}
	if obj.grid[r][c] == 1 {
		obj.res += 4
		if r > 0 && obj.grid[r-1][c] == 1 {
			obj.res -= 2
		}
		if c > 0 && obj.grid[r][c-1] == 1 {
			obj.res -= 2
		}
	}
	obj.recRow(r, c+1)
}

// @lc code=end

