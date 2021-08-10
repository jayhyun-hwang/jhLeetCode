package testCode

import (
	"testing"
)

//main
func TestMain(t *testing.T) {
	countOfAtoms("kkk")
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
func countOfAtoms(formula string) string {
	//map
	//bracket
	//recursive function

	idx := 0

	dynaFunc := func() {}
	dynaFunc = func() {

	}
	dynaFunc()

	return ""
}
