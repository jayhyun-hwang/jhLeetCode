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
	res        int
	bmap       map[byte]int
	minusCount int
}

func longestPalindrome(s string) int {
	bArr := []byte(s)
	bmap := make(map[byte]int)
	minusCount := 0
	for _, val := range bArr {
		bmap[val]++
	}
	for _, val := range bmap {
		if val%2 == 1 {
			minusCount++
		}
	}
	if minusCount > 1 {
		return len(s) - minusCount - 1
	}
	return len(s)
}
