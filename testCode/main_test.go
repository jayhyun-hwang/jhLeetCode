package main_test

import (
	"fmt"
	"strings"
	"testing"
)

func TestMain(t *testing.T) {

	//tf := "test param" //test function here
	tf := "ghdfasdf" //test function here
	bArr := []byte(tf)
	fmt.Println("value = ", bArr)
	s := string(bArr)
	fmt.Println("value = ", s)

	str := "abcabcabcd"
	sStr := strings.Split(str, str[:1])
	fmt.Println(sStr)
	//fmt.Println(summaryRanges([]int{-1})) //print testFunc return value
}

type Obj struct {
	grid    [][]int
	counted map[int]map[int]bool
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
	if c >= obj.rowLen {
		return
	}
	if r >= obj.colLen {
		return
	}
	if c < 0 {
		return
	}
	switch dir {
	case 1:
	case 2:
	case 3:
	case 4:
	}
	//if next value ==0 || len==idx { res++ }
	//do all direction except from direction
	//add counted
}
