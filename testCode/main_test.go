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

	findSol := func() {}
	findSol = func() {
		if idx >= len(formula) {
			return
		}
		if formula[idx] == '(' {

		}
		idx++
		findSol()
	}
	findSol()

	return res
}
