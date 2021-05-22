package main_test

import (
	"fmt"
	"testing"
)

func TestMain(t *testing.T) {

	//tf := "test param" //test function here
	tf := "ghdfasdf" //test function here
	bArr := []byte(tf)
	fmt.Println("value = ", bArr)
	s := string(bArr)
	fmt.Println("value = ", s)

	//fmt.Println(summaryRanges([]int{-1})) //print testFunc return value
}

type Obj struct {
	vmap     map[byte]bool
	str      []byte
	idxArr   []int
	vowstack []byte
	idx      int
}

func reverseVowels(s string) string {
	obj := new(Obj)
	//make stack and put vowels: stack
	//store vowels' index: idxArr
	//leetcode
	//01234567

	obj.vmap = map[byte]bool{
		'a': true,
		'e': true,
		'i': true,
		'o': true,
		'u': true,
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
