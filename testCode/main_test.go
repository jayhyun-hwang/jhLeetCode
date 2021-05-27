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

	imap := make(map[int]bool, len(nums))
	for _, val := range nums {
		imap[val] = true
	}
	res := make([]int, 0, len(nums))
	for i := 1; i <= len(nums); i++ {
		if !imap[i] {
			res = append(res, i)
		}
	}
	return res
}
