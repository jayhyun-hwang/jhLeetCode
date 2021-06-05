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

type Obj2 struct {
	res           float64
	res2          float64
	monthSave     float64
	seed          float64
	monthInterest float64
	months        float64
}

func (obj *Obj2) calcul() {

	for i := 0; i < int(obj.months); i++ {
		obj.seed += obj.monthSave
		obj.seed *= obj.monthInterest
	}
	obj.res = obj.seed
}
func (obj *Obj2) calcul2() {

	for i := 0; i < int(obj.months); i++ {
		obj.seed += obj.monthSave
		obj.res += obj.seed*obj.monthInterest - obj.seed
	}
	obj.res += obj.seed
}
func TestMain(t *testing.T) {

	obj := new(Obj2)
	obj.monthSave = 500000
	obj.seed = 0.0
	obj.monthInterest = 1.02
	obj.months = 360
	obj.calcul()
	fmt.Printf("복리결과= %f\n", obj.res)
	obj2 := new(Obj2)
	obj2.monthSave = 500000
	obj2.seed = 0.0
	obj2.monthInterest = 1.02
	obj2.months = 360
	obj2.calcul2()
	fmt.Printf("단리결과= %f\n", obj2.res)
}

//매달 50만원
//수익률 10프로
//연수

//tf := "test param" //test function here
// tf := "ghdfasdf" //test function here
// bArr := []byte(tf)
// fmt.Println("value = ", bArr)
// s := string(bArr)
// fmt.Println("value = ", s)

// str := "abcabcabcd"
// sStr := strings.Split(str, str[:1])
// fmt.Println(sStr)
