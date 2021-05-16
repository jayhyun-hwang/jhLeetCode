/*
 * @lc app=leetcode id=155 lang=golang
 *
 * [155] Min Stack
 */

// @lc code=start
type MinStack struct {
    stack []int
}


/** initialize your data structure here. */
func Constructor() MinStack {
    return new MinStack()
}


func (this *MinStack) Push(val int)  {
	if len(this.stack) < 1 {
		this.stack = append(this.stack, val)
		return
	}
	if val 
}


func (this *MinStack) Pop()  {
	if len(this.stack) < 1 {
		return
	}
    this.stack = this.stack[:len(this.stack)-1]
}


func (this *MinStack) Top() int {
    
}


func (this *MinStack) GetMin() int {
    
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

