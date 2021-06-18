package testCode

import "math"

type Obj struct {
	num      int
	res      int
	stack    []int
	stackIdx int
}

func reverseInt(num int) int {
	obj := new(Obj)
	obj.num = num
	obj.findReverse()
	obj.makeRes()
	return obj.res
}
func (obj *Obj) findReverse() {
	if obj.num < 1 {
		return
	}
	obj.stack = append(obj.stack, obj.num%10)
	obj.num /= 10
	obj.findReverse()
}
func (obj *Obj) makeRes() {
	if len(obj.stack) <= obj.stackIdx {
		return
	}
	obj.res += int(math.Pow10(obj.stackIdx)) * obj.stack[len(obj.stack)-1-obj.stackIdx]
	obj.stackIdx++
	obj.makeRes()
}
