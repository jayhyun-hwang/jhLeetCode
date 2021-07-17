/*
 * @lc app=leetcode id=731 lang=golang
 *
 * [731] My Calendar II
 */

// @lc code=start
type TreeNode struct {
	Start int
	End   int
	Max   int
	Left  *TreeNode
	Right *TreeNode
}

func (n *TreeNode) isOverlap(start, end int) bool {
	return n.Start < end && n.End > start
}

func (n *TreeNode) resetMax(end int) {
	if n.Max < end {
		n.Max = end
	}
}

func (n *TreeNode) intersect(start, end int) *TreeNode {
	out := TreeNode{
		Start: start,
		End:   end,
	}
	if n.Start > start {
		out.Start = n.Start
	}
	if n.End < end {
		out.End = n.End
	}
	return &out
}

type IntersectionList struct {
	l []*TreeNode
}

func (i *IntersectionList) isOverlap(node *TreeNode) bool {
	for _, v := range i.l {
		if v.isOverlap(node.Start, node.End) {
			return true
		}
	}
	return false
}

func (i *IntersectionList) add(node *TreeNode) {
	i.l = append(i.l, node)
}

type MyCalendarTwo struct {
	root *TreeNode
}

func Constructor() MyCalendarTwo {
	return MyCalendarTwo{}
}

func (m *MyCalendarTwo) insert(node *TreeNode) {
	n := m.root
	for n != nil {
		n.resetMax(node.End)
		if node.Start < node.Start {
			if n.Left != nil {
				n = n.Left
				continue
			}
			n.Left = node
			return
		}
		if n.Right != nil {
			n = n.Right
			continue
		}
		n.Right = node
		return
	}
	m.root = node
}

func (m *MyCalendarTwo) isTripleBooking(start, end int) bool {
	l := IntersectionList{}
	n := m.root
	for n != nil {
		if n.isOverlap(start, end) {
			in := n.intersect(start, end)
			if l.isOverlap(in) {
				return true
			}
			l.add(in)
		}
		if n.Left != nil && n.Max > end {
			n = n.Left
			continue
		}
		n = n.Right
	}
	return false
}

func (m *MyCalendarTwo) Book(start int, end int) bool {
	if m.isTripleBooking(start, end) {
		return false
	}
	m.insert(&TreeNode{
		Start: start,
		End:   end,
		Max:   end,
	})
	return true
}

/**
 * Your MyCalendarTwo object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Book(start,end);
 */
// @lc code=end

