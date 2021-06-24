package benchMark

func testFunc2() {
	testFunc22(Case1)
	testFunc22(Case2)
}

//fix here
func testFunc22(arr []int) {
	isOneUser := true
	totalWorkTime := 0
	mp := make(map[int]bool)
	for idx, val := range arr {
		if isOneUser {
			totalWorkTime += val
			if !mp[arr[idx]] {
				mp[arr[idx]] = true
				if len(mp) > 1 {
					isOneUser = false
					totalWorkTime = 0
				}
			}
		}
	}
}
