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
	_ = findDisappearedNumbers([]int{4, 3, 2, 7, 8, 2, 3, 1})
	//fmt.Println(summaryRanges([]int{-1})) //print testFunc return value
}

func findDisappearedNumbers(nums []int) []int {
	iArr := make([]bool, len(nums))
	for i := 0; i < len(nums); i++ {
		iArr[nums[i]-1] = true
	}
	res := []int{}
	for i := 0; i < len(iArr); i++ {
		if !iArr[i] {
			res = append(res, i+1)
		}
	}
	return res
}
