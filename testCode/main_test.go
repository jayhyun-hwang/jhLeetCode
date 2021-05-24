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

	findTheDifference("", "y")

	//fmt.Println(summaryRanges([]int{-1})) //print testFunc return value
}

type Obj struct {
}

func findTheDifference(s string, t string) byte {
	tbarr := []byte(t)
	bmap := make(map[byte]int)

	for _, val := range tbarr {
		/*if _, ok := bmap[val]; ok {
		bmap[val] += 1
		} else {
			bmap[val] = 0
		}*/
		bmap[val] += 1

	}

	sbarr := []byte(s)
	for _, val := range sbarr {
		/*if _, ok := bmap[val]; ok {
		bmap[val] += 1
		} else {
			bmap[val] = 0
		}*/
		bmap[val] += 1
	}
	for i, mval := range bmap {
		fmt.Println("value= ", mval)
		fmt.Println("key= ", i)

		if mval%2 == 1 {

			return i
		}
	}
	return 0
}
