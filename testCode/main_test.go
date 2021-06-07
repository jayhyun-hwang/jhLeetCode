package main_test

import (
	"fmt"
	"testing"
)

type Obj struct {
	grid    [][]int
	counted map[int]map[int]bool
	next    [][]int
	rowLen  int
	colLen  int
	res     int
}

func islandPerimeter(grid [][]int) int {
	obj := new(Obj)
	obj.grid = grid
	obj.rowLen = len(grid)
	obj.colLen = len(grid[0])

	//direction == {up:1, right:2, down:3, left:4}
	obj.findPerimeter(0, 0, 2)
	return obj.res
}

func (obj *Obj) findPerimeter(r int, c int, dir int) {
	if r < 0 {
		return
	}
	if c < 0 {
		return
	}
	if r >= obj.rowLen {
		return
	}
	if c >= obj.colLen {
		return
	}
	switch dir {
	case 1:
	case 2:
		if obj.grid[r][c] == 1 {

		}
	case 3:
	case 4:
	}
	//if next value ==0 || len==idx { res++ }
	//do all direction except from direction
	//add counted
}
func TestMain(t *testing.T) {
	// tf := "test param" //test function here
	// tf := "ghdfasdf" //test function here
	// bArr := []byte(tf)
	// fmt.Println("value = ", bArr)
	// s := string(bArr)
	// fmt.Println("value = ", s)
	// str := "abcabcabcd"
	// sStr := strings.Split(str, str[:1])
	// fmt.Println(sStr)
	arr1 := [][]int{
		{0, 1, 0},
		{1, 1, 1},
		{0, 1, 0},
		{1, 1, 0},
	}
	fmt.Println(arr1)
	fmt.Println(len(arr1))
	fmt.Println(len(arr1[0]))
}

// func islandPerimeter(grid [][]int) int {
//     var(
//         res int
//         l = len(grid[0])
//     )
//     for i := 0; i < len(grid); i++ {
//         for j := 0; j < l; j++ {
//             if grid[i][j] == 1 {
//                 res += 4
//                 if i > 0 && grid[i-1][j] == 1 {
//                     res -= 2
//                 }
//                 if j > 0 && grid[i][j-1] == 1 {
//                     res -= 2
//                 }
//             }
//         }
//     }
//     return res
// }
