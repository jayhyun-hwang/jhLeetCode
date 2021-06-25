/*
 * @lc app=leetcode id=520 lang=golang
 *
 * [520] Detect Capital
 */

// @lc code=start
type Obj struct {
	word        string
	idx         int
	shouldUpper bool
}

func detectCapitalUse(word string) bool {
	if len(word) == 1 {
		return true
	}
	var firstIsUp bool
	if word[0] < 91 {
		firstIsUp = true
	} else {
		firstIsUp = false
	}
	obj := new(Obj)
	obj.word = word
	if word[1] < 91 {
		obj.shouldUpper = true
	} else {
		obj.shouldUpper = false
	}
	if !firstIsUp && obj.shouldUpper {
		return false
	}
	var piv byte
	if obj.shouldUpper {
		piv = 64
	} else {
		piv = 96
	}
	obj.idx = 2
	return obj.findSol(piv)
}
func (obj *Obj) findSol(piv byte) bool {
	if obj.idx >= len(obj.word) {
		return true
	}
	if obj.word[obj.idx] > piv && obj.word[obj.idx] < piv+27 {
		obj.idx++
		return obj.findSol(piv)
	}
	return false
}

// @lc code=end

