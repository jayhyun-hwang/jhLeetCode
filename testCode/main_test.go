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
	if digits == "" {
		return nil
	}
	nmap := map[byte][]byte{
		'2': {'a', 'b', 'c'},
		'3': {'d', 'e', 'f'},
		'4': {'g', 'h', 'i'},
		'5': {'j', 'k', 'l'},
		'6': {'m', 'n', 'o'},
		'7': {'p', 'q', 'r', 's'},
		'8': {'t', 'u', 'v'},
		'9': {'w', 'x', 'y', 'z'},
	}
	var resultArr []string
	oneStr := []byte{}

	return recString(nmap, digits, 0, oneStr, &resultArr)
}
func recString(nmap map[byte][]byte, digits string, idx int, oneStr []byte, resultArr *[]string) []string {
	if idx == len(digits) {
		return *resultArr
	}
	for _, valDigits := range nmap[digits[idx]] {
		oneStr = append(oneStr, valDigits)
		if idx == len(digits)-1 {
			*resultArr = append(*resultArr, string(oneStr))
		} else {
			*resultArr = recString(nmap, digits, idx+1, oneStr, resultArr)
		}
		oneStr = oneStr[:len(oneStr)-1]
	}
	return *resultArr
}

//s := string([]rune{'\u0041', '\u0042', '\u0043', '\u20AC', -1})
