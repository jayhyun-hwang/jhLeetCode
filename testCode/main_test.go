package testCode

import (
	"fmt"
	"strconv"
	"testing"
)

//main
func TestMain(t *testing.T) {
	fmt.Println(countOfAtoms("K4(ON(SO3)2)2"))
}

func countOfAtoms(formula string) string {
	//map
	//bracket
	//recursive function

	idx := 0
	res := ""
	ing := false
	depth := 0
	temp := ""
	//when depth is 0, add res
	tempMap := make(map[int]map[string]int)
	num := ""
	resMap := make(map[string]int)

	insertTemp := func() {
		if depth == 0 {
			if len(num) > 0 {
				resMap[temp], _ = strconv.Atoi(num)
			} else {
				resMap[temp] = 1
			}
		} else {
			tempMap[depth][temp], _ = strconv.Atoi(num)
		}

	}
	findSol := func() {}
	findSol = func() {
		if idx >= len(formula) {
			return
		}
		c := formula[idx]
		switch {
		case c >= 'A' && c <= 'Z': //Uppercase
			if len(temp) > 0 { //close temp, start
				insertTemp()
				// insertTemp(temp, num, depth)
				temp = string(c)
			} else { //start new atom with upper character
				temp = string(c)
			}
		case c >= 'a' && c <= 'z': //downcase
			temp += string(c)
		case c == '(': //bracket open
			// insertTemp(temp, num, depth)
			insertTemp()
			depth++
		case c == ')': //bracket close

		case c >= '0' && c <= '9': //number
			num += string(c)
		}
		idx++
		findSol()
	}
	findSol()

	return res
}
