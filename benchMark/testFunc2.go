package benchMark

import (
	"strings"
)

func testFunc2() {
	// fmt.Println(testFunc22(Case1))
	// fmt.Println(testFunc22(Case2))
	// fmt.Println(testFunc22(Case3))
	// fmt.Println(testFunc22(Case4))
	testFunc22(Case1)
	testFunc22(Case2)
	testFunc22(Case3)
	testFunc22(Case4)
}

//fix here
func testFunc22(word string) bool {
	if len(word) == 1 {
		return true
	}
	if word[1:] == strings.ToLower(word[1:]) {
		return true
	}
	if word == strings.ToUpper(word) {
		return true
	}
	return false
}
