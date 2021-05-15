package main_test

import (
	"fmt"
	"testing"
)

func TestMain(t *testing.T) {

	//tf := "test param" //test function here
	tf := "" //test function here

	fmt.Println("tf = ", tf)
	fmt.Println(letterCombinations(tf)) //print testFunc return value
}

var length int
var nmap = map[byte][]rune{
	'2': {'a', 'b', 'c'},
	'3': {'d', 'e', 'f'},
	'4': {'g', 'h', 'i'},
	'5': {'j', 'k', 'l'},
	'6': {'m', 'n', 'o'},
	'7': {'p', 'q', 'r', 's'},
	'8': {'t', 'u', 'v'},
	'9': {'w', 'x', 'y', 'z'},
}
var resString = []string{}

func letterCombinations(digits string) []string {
	oneStr := []rune{}

	resString = recString(digits, 0, oneStr)
	return resString
}
func recString(digits string, idx int, oneStr []rune) []string {
	if idx == len(digits) {
		return resString
	}
	for _, valDigits := range nmap[digits[idx]] {
		oneStr = append(oneStr, valDigits)
		if idx == len(digits)-1 {
			resString = append(resString, string(oneStr))
		} else {
			resString = recString(digits, idx+1, oneStr)
		}
		oneStr = oneStr[:len(oneStr)-1]
	}
	return resString
}

//s := string([]rune{'\u0041', '\u0042', '\u0043', '\u20AC', -1})
