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
	copyTest()
	copyTest2()
}

type strStruct struct {
	strvar1 string
	strvar2 string
	strvar3 string
}

func copyTest() {
	strStructList := []strStruct{}
	strstruct := strStruct{}
	for i := 1; i <= 100; i++ {
		strval := strconv.Itoa(i)
		switch i % 3 {
		case 1:
			strstruct = strStruct{}
			strstruct.strvar1 = strval
		case 2:
			strstruct.strvar2 = strval
		case 0:
			strstruct.strvar3 = strval
			strStructList = append(strStructList, strstruct)
		}
	}
	fmt.Println(strStructList)

	for _, val := range strStructList {
		val.strvar1 += "#"
		val.strvar2 += "#"
		val.strvar3 += "#"
		fmt.Println(val)
	}
	fmt.Println(strStructList)
}

type intStruct struct {
	intvar1 int
	intvar2 int
	intvar3 int
}

func copyTest2() {
	intStructList := []intStruct{}
	intstruct := intStruct{}
	for i := 1; i <= 100; i++ {
		switch i % 3 {
		case 1:
			intstruct = intStruct{}
			intstruct.intvar1 = i
		case 2:
			intstruct.intvar2 = i
		case 0:
			intstruct.intvar3 = i
			intStructList = append(intStructList, intstruct)
		}
	}
	fmt.Println(intStructList)

	for _, val := range intStructList {
		val.intvar1 += 1000
		val.intvar2 += 1000
		val.intvar3 += 1000
		fmt.Println(val)
	}
	fmt.Println(intStructList)
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
