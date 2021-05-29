/*
 * @lc app=leetcode id=459 lang=golang
 *
 * [459] Repeated Substring Pattern
 */

// @lc code=start

type Obj struct {
	paramStr string
	sLen     int
	idx      int
	res      bool
}

func repeatedSubstringPattern(s string) bool {
	obj := new(Obj)
	obj.sLen = len(s)
	obj.paramStr = s
	if obj.sLen == 1 {
		return true
	}

	return false
}
func (obj *Obj) recurFunc() {

}

// @lc code=end