/*
 * @lc app=leetcode id=459 lang=golang
 *
 * [459] Repeated Substring Pattern
 */

// @lc code=start

type Obj struct {
	paramStr string
	end      int
	idx      int
}

func repeatedSubstringPattern(s string) bool {
	obj := new(Obj)
	obj.end = len(s)/2 + 1
	obj.paramStr = s
	obj.idx = 1

	return obj.recurFunc()
}
func (obj *Obj) recurFunc() bool {
	if obj.end == obj.idx {
		return false
	}
	for _, ele := range strings.Split(obj.paramStr, obj.paramStr[:obj.idx]) {
		if ele != "" {
			obj.idx++
			return obj.recurFunc()
		}
	}
	return true
}

// @lc code=end