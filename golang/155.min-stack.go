/*
 * @lc app=leetcode id=155 lang=golang
 *
 * [155] Min Stack
 */

// @lc code=start
type MinStack struct {
	stack []int
	min   int
}

/** initialize your data structure here. */
func Constructor() MinStack {
	con := new(MinStack)
	return *con
}

func (this *MinStack) Push(val int) {
	this.stack = append(this.stack, val)
	return
}

func (this *MinStack) Pop() {
	if len(this.stack) < 1 {
		return
	}
	this.stack = this.stack[:len(this.stack)-1]
}

func (this *MinStack) Top() int {
	if len(this.stack) < 1 {
		return 0
	}
	return this.stack[len(this.stack)-1]
}

func (this *MinStack) GetMin() int {
	if len(this.stack) < 1 {
		return 0
	}
	this.min = this.stack[0]
	return this.forGetMin(0)
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
	return this.forGetMin(i)
}

/**
 * Your MinStack object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(val);
 * obj.Pop();
 * param_3 := obj.Top();
 * param_4 := obj.GetMin();
 */
// @lc code=end

