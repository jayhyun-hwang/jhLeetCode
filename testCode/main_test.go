package testCode

import (
	"fmt"
	"testing"
)

//main
func TestMain(t *testing.T) {
	obj := Constructor()
	param := obj.Book(48, 50)
	fmt.Printf("param: %v\n", param)
	param = obj.Book(0, 6)
	fmt.Printf("param2: %v\n", param)
	param = obj.Book(6, 13)
	fmt.Printf("param3: %v\n", param)
	param = obj.Book(8, 13)
	fmt.Printf("param4: %v\n", param)
	param = obj.Book(15, 23)
	fmt.Printf("param5: %v\n", param)
	param = obj.Book(49, 50)
	fmt.Printf("param6: %v\n", param)
	param = obj.Book(45, 50)
	fmt.Printf("param6: %v\n", param)
}

//[null,true,false,true,true,false,false,false,true,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false]
//[null,true,false,true,true,false,true,false,true,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false]
// type MyCalendar struct {
// 	calMap map[int]int
// }

// func Constructor() MyCalendar {
// 	obj := new(MyCalendar)
// 	obj.calMap = make(map[int]int, 0)
// 	return *obj
// }

// func (this *MyCalendar) Book(start int, end int) bool {
// 	if this.calMap[start] == 2 || this.calMap[start] == 1 {
// 		return false
// 	}
// 	if this.calMap[end] == 2 || this.calMap[end] == 3 {
// 		return false
// 	}
// 	for i := start + 1; i < end; i++ {
// 		if this.calMap[i] != 0 {
// 			return false
// 		}
// 	}
// 	this.calMap[start] = 1
// 	this.calMap[end] = 3
// 	for i := start + 1; i < end; i++ {
// 		this.calMap[i] = 2
// 	}
// 	return true
// }
type MyCalendar struct {
	root *treeNode
}

type treeNode struct {
	start, end  int
	left, right *treeNode
}

func Constructor() MyCalendar {
	return MyCalendar{
		root: nil,
	}
}

func (this *MyCalendar) Book(start int, end int) bool {
	if end < start || start < 0 {
		return false
	}

	return insert(&this.root, start, end)
}

func insert(root **treeNode, start, end int) bool {
	if *root == nil {
		*root = &treeNode{
			start: start,
			end:   end,
			left:  nil,
			right: nil,
		}
		return true
	}

	if (*root).start >= end {
		return insert(&(*root).left, start, end)
	} else if (*root).end <= start {
		return insert(&(*root).right, start, end)
	}
	return false
}
