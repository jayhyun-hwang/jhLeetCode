/*
 * @lc app=leetcode id=459 lang=golang
 *
 * [459] Repeated Substring Pattern
 */

// @lc code=start
type Obj struct {
	strLen int
}

func repeatedSubstringPattern(s string) bool {
	obj := new(Obj)
	obj.strLen = 1
	return obj.recurFunc(s)
}
func (obj *Obj) recurFunc(s string) bool {
	if len(s)%obj.strLen != 0 {
		obj.strLen++
		return obj.recurFunc(s)
	}
	if obj.strLen >= len(s)/2+1 {
		return false
	}
	for i := 1; obj.strLen*i < len(s); i++ {
		if s[:obj.strLen] != s[obj.strLen*i:obj.strLen*(i+1)] {
			obj.strLen++
			return obj.recurFunc(s)
		}
	}
	return true
}

// @lc code=end