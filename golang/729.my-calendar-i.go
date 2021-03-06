/*
 * @lc app=leetcode id=729 lang=golang
 *
 * [729] My Calendar I
 *
 * https://leetcode.com/problems/my-calendar-i/description/
 *
 * algorithms
 * Medium (54.08%)
 * Likes:    1459
 * Dislikes: 50
 * Total Accepted:    117.3K
 * Total Submissions: 216.8K
 * Testcase Example:  '["MyCalendar","book","book","book"]\n[[],[10,20],[15,25],[20,30]]'
 *
 * You are implementing a program to use as your calendar. We can add a new
 * event if adding the event will not cause a double booking.
 *
 * A double booking happens when two events have some non-empty intersection
 * (i.e., some moment is common to both events.).
 *
 * The event can be represented as a pair of integers start and end that
 * represents a booking on the half-open interval [start, end), the range of
 * real numbers x such that start <= x < end.
 *
 * Implement the MyCalendar class:
 *
 *
 * MyCalendar() Initializes the calendar object.
 * boolean book(int start, int end) Returns true if the event can be added to
 * the calendar successfully without causing a double booking. Otherwise,
 * return false and do not add the event to the calendar.
 *
 *
 *
 * Example 1:
 *
 *
 * Input
 * ["MyCalendar", "book", "book", "book"]
 * [[], [10, 20], [15, 25], [20, 30]]
 * Output
 * [null, true, false, true]
 *
 * Explanation
 * MyCalendar myCalendar = new MyCalendar();
 * myCalendar.book(10, 20); // return True
 * myCalendar.book(15, 25); // return False, It can not be booked because time
 * 15 is already booked by another event.
 * myCalendar.book(20, 30); // return True, The event can be booked, as the
 * first event takes every time less than 20, but not including 20.
 *
 *
 * Constraints:
 *
 *
 * 0 <= start < end <= 10^9
 * At most 1000 calls will be made to book.
 *
 *
 */

// @lc code=start
// type MyCalendar struct {
// 	calMap  map[int]bool
// 	tempMap map[int]bool
// }

// func Constructor() MyCalendar {
// 	obj := new(MyCalendar)
// 	obj.calMap = make(map[int]bool, 0)
// 	return *obj
// }

// func (this *MyCalendar) Book(start int, end int) bool {
// 	this.tempMap = this.calMap
// 	for i := start + 1; i < end; i++ {
// 		if this.tempMap[i] {
// 			return false
// 		}
// 		this.tempMap[i] = true
// 	}
// 	this.tempMap[start] = true
// 	this.tempMap[end] = true
// 	this.calMap = this.tempMap
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

/**
 * Your MyCalendar object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Book(start,end);
 */
// @lc code=end

