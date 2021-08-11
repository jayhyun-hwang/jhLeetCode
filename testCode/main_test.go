package testCode

import (
	"testing"
)

//main
func TestMain(t *testing.T) {
	countOfAtoms("kkk")
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
