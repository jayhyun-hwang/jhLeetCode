package testCode

import (
	"fmt"
	"strconv"
	"testing"
)

//main
func TestMain(t *testing.T) {
	//fmt.Println(countOfAtoms("K4(ON(SO3)2)2"))
	fmt.Println(sol([]int{0, 1, 1, 2, 3, 4, 5, 6, 6}))

}

//[0,0,1,1,2,3,4,5,6,6]
func sol(arr []int) []int {
	if len(arr) < 2 {
		return arr
	}
	preVal := arr[0]
	lastVal := arr[len(arr)-1]
	idx := 1

	for _, val := range arr {
		if preVal == val {
			continue
		} else {
			if preVal == lastVal {
				arr[idx] = 0
			} else {
				arr[idx] = val
			}
			idx++
		}
		preVal = val
	}

	return arr
}

func countOfAtoms(formula string) string {
	//map
	//bracket
	//recursive function

	idx := 0
	res := ""
	depth := 0
	temp := ""
	//when depth is 0, add res
	tempMap := make(map[int]map[string]int)
	num := ""
	resMap := make(map[string]int)

	insertTemp := func() {
		if depth == 0 {
			if len(num) > 0 {
				atomCount, _ := strconv.Atoi(num)
				resMap[temp] += atomCount
			} else {
				resMap[temp] += 1
			}
		} else {
			tempMap[depth][temp], _ = strconv.Atoi(num)
		}
		temp = ""
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
			//in bracket

		case c >= 'a' && c <= 'z': //downcase
			temp += string(c)
		case c == '(': //bracket open
			// insertTemp(temp, num, depth)
			insertTemp()
			depth++
		case c == ')': //bracket close

		case c >= '0' && c <= '9': //number
			if len(temp) > 0 {
				num += string(c)
			} else {

			}
		}
		idx++
		findSol()
	}
	findSol()

	return res
}
