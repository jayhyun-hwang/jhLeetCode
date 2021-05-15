package main_test

import (
	"fmt"
	"testing"
)

func TestMain(t *testing.T) {

	//tf := "test param" //test function here
	tf := "23" //test function here

	fmt.Println("tf = ", tf)
	fmt.Println(letterCombinations(tf)) //print testFunc return value
}

type conValue struct {
	nmap      map[byte][]rune
	resString []string
}

func letterCombinations(digits string) []string {
	var conVal conValue
	conVal.nmap = map[byte][]rune{
		'2': {'a', 'b', 'c'},
		'3': {'d', 'e', 'f'},
		'4': {'g', 'h', 'i'},
		'5': {'j', 'k', 'l'},
		'6': {'m', 'n', 'o'},
		'7': {'p', 'q', 'r', 's'},
		'8': {'t', 'u', 'v'},
		'9': {'w', 'x', 'y', 'z'},
	}
	oneStr := []rune{}

	conVal.resString = conVal.recString(digits, 0, oneStr)
	return conVal.resString
}
func (conVal *conValue) recString(digits string, idx int, oneStr []rune) []string {
	if idx == len(digits) {
		return conVal.resString
	}
	for _, valDigits := range conVal.nmap[digits[idx]] {
		oneStr = append(oneStr, valDigits)
		if idx == len(digits)-1 {
			conVal.resString = append(conVal.resString, string(oneStr))
		} else {
			conVal.resString = conVal.recString(digits, idx+1, oneStr)
		}
		oneStr = oneStr[:len(oneStr)-1]
	}
	return conVal.resString
}

//s := string([]rune{'\u0041', '\u0042', '\u0043', '\u20AC', -1})
