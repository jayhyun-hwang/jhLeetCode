package main_test

import (
	"fmt"
	"testing"
)

func TestMain(t *testing.T) {
	tf := plusOne([]int{1, 2, 3})
	fmt.Println("tf = ", tf)
}
func plusOne(digits []int) []int {
	return isNine(digits, len(digits)-1)
}

func isNine(nlist []int, idx int) []int {
	if nlist[idx]+1 > 9 {
		nlist[idx] = 0
		if idx < 1 {
			nlist = append([]int{1}, nlist...)
		} else {
			return isNine(nlist, idx-1)
		}
	} else {
		nlist[idx] += 1
		return nlist
	}
	return nil
}
