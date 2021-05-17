package main_test

import (
	"fmt"
	"testing"
)

func TestMain(t *testing.T) {

	//tf := "test param" //test function here
	tf := "23" //test function here

	fmt.Println("tf = ", tf)
	fmt.Println(letterCombinations(tf)) //print testFunc return value
}

type MinStack struct {
	stack []int
	min   int
}

/** initialize your data structure here. */
func Constructor() MinStack {
	return new(MinStack)
}

func (this *MinStack) Push(val int) {
	if len(this.stack) < 1 {
		this.stack = append(this.stack, val)
		return
	}
}

func (this *MinStack) Pop() {
	if len(this.stack) < 1 {
		return
	}
	this.stack = this.stack[:len(this.stack)-1]
}

func (this *MinStack) Top() int {
	return this.stack[len(this.stack)-1]
}

func (this *MinStack) GetMin() int {
	if len(this.stack) < 1 {
		return nil
	}
	this.min = this.stack[0]
	forGetMin(0)
}
func (this *MinStack) forGetMin(i int) int {
	if len(this.stack) == i {
		return this.min
	}
	compareIdx := this.stack[i]
	if this.min > compareIdx {
		this.min = compareIdx
	}
	i++
	return forGetMin(i)
}

//s := string([]rune{'\u0041', '\u0042', '\u0043', '\u20AC', -1})
