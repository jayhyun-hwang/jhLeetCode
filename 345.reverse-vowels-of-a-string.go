/*
 * @lc app=leetcode id=345 lang=golang
 *
 * [345] Reverse Vowels of a String
 */

// @lc code=start

type Obj struct {
	vmap     map[byte]bool
	str      []byte
	idxArr   []int
	vowstack []byte
	idx      int
}

func reverseVowels(s string) string {
	obj := new(Obj)

	obj.vmap = map[byte]bool{
		'a': true,
		'e': true,
		'i': true,
		'o': true,
		'u': true,
		'A': true,
		'E': true,
		'I': true,
		'O': true,
		'U': true,
	}
	obj.str = []byte(s)
	obj.idx = 0
	obj.getRes()

	if len(obj.vowstack) > 0 {
		for _, value := range obj.idxArr {
			obj.str[value] = obj.vowstack[len(obj.vowstack)-1]
			obj.vowstack = obj.vowstack[:len(obj.vowstack)-1]
		}
	}

	return string(obj.str)
}

func (obj *Obj) getRes() {
	if len(obj.str)-1 < obj.idx {
		return
	}
	if obj.vmap[obj.str[obj.idx]] {
		obj.idxArr = append(obj.idxArr, obj.idx)
		obj.vowstack = append(obj.vowstack, obj.str[obj.idx])
	}
	obj.idx++
	obj.getRes()
}

// @lc code=end

