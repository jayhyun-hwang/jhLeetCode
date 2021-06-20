package testCode

import "math"

type ListNode struct {
	Val  int
	Next *ListNode
}

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	var l1res int
	l1idx := 0
	l1res += l1.Val * int(math.Pow10(l1idx))
	l1idx++
}

func l1Int()
