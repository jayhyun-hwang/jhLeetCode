package main_test

import (
	"testing"
)

type Obj struct {
	maxNum int
}

func (obj *Obj) compare(n int) {
	if n > obj.maxNum {
		obj.maxNum = n
	}
}
func findMaxConsecutiveOnes(nums []int) int {
	obj := new(Obj)
	count := 0
	nums = append(nums, 0)
	for _, num := range nums {
		if num == 1 {
			count++
		} else {
			obj.compare(count)
			count = 0
		}
	}
	return obj.maxNum
}

//main
func TestMain(t *testing.T) {

}

// tf := "test param" //test function here
// tf := "ghdfasdf" //test function here
// bArr := []byte(tf)
// fmt.Println("value = ", bArr)
// s := string(bArr)
// fmt.Println("value = ", s)
// str := "abcabcabcd"
// sStr := strings.Split(str, str[:1])
// fmt.Println(sStr)
