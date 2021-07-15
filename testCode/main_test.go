package testCode

import (
	"fmt"
	"testing"
)

//main
func TestMain(t *testing.T) {
	obj := Constructor()
	param_1 := obj.Book(20, 29)
	fmt.Printf("param_1: %v\n", param_1)
	param_2 := obj.Book(14, 20)
	fmt.Printf("param_2: %v\n", param_2)
}

type MyCalendar struct {
	calMap map[int]bool
}

func Constructor() MyCalendar {
	obj := new(MyCalendar)
	obj.calMap = make(map[int]bool, 0)
	return *obj
}

func (this *MyCalendar) Book(start int, end int) bool {
	for i := start + 1; i < end; i++ {
		if this.calMap[i] {
			return false
		}
		this.calMap[i] = true
	}
	this.calMap[start] = true
	this.calMap[end] = true
	return true
}
