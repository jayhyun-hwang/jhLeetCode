package benchMark

var Case1 = []int{1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1}
var Case2 = []int{1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2}

func testFunc1() {
	testFunc11(Case1)
	testFunc11(Case2)
}
func testFunc11(arr []int) {
	isOneUser := true
	totalWorkTime := 0
	var userID int
	if len(arr) > 0 {
		userID = arr[0]
	}
	for idx, val := range arr {
		if isOneUser {
			totalWorkTime += val
			if userID != arr[idx] {
				isOneUser = false
				totalWorkTime = 0
			}
		}
	}
}
