package testCode

import (
	"fmt"
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
	dep := 0
	resMap := make(map[int]map[string]int)

	findSol := func() {}
	findSol = func() {
		if idx >= len(formula) {
			return
		}
		c := formula[idx]
		switch {
		case c >= 'A' && c <= 'Z':
			ing = true
		case c >= 'a' && c <= 'z':

		case c == '(':

		}
		idx++
		findSol()
	}
	findSol()

	return res
}
