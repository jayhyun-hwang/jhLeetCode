package main_test

import (
	"fmt"
	"strings"
	"testing"
)

func TestMain(t *testing.T) {

	//tf := "test param" //test function here
	tf := "ghdfasdf" //test function here
	bArr := []byte(tf)
	fmt.Println("value = ", bArr)
	s := string(bArr)
	fmt.Println("value = ", s)

	str := "abcabcabcd"
	sStr := strings.Split(str, str[:1])
	fmt.Println(sStr)
	b := repeatedSubstringPattern("ababab")
	_ = b
	//fmt.Println(summaryRanges([]int{-1})) //print testFunc return value
}

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
