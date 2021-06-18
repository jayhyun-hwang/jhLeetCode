package testCode

import (
	"fmt"
	"sort"
	"strconv"
	"testing"
)

func findRelativeRanks(score []int) []string {
	//map for matching scores and ranks
	mp := make(map[int]string)
	res := make([]string, 0)
	scoreCopy := make([]int, len(score))
	copy(scoreCopy, score)
	sort.Slice(scoreCopy, func(i, j int) bool {
		return scoreCopy[i] < scoreCopy[j]
	})
	lenCopy := len(scoreCopy)
	for idx, val := range scoreCopy {
		var ele string
		switch idx {
		case lenCopy - 1:
			ele = "Gold Medal"
		case lenCopy - 2:
			ele = "Silver Medal"
		case lenCopy - 3:
			ele = "Bronze Medal"
		default:
			ele = strconv.Itoa(lenCopy - idx)
		}
		mp[val] = ele
	}
	for _, val := range score {
		res = append(res, mp[val])
	}
	return res
}

// func findRelativeRanks(score []int) []string {
// 	//map for matching scores and ranks
// 	mp := make(map[int]string)
// 	res := make([]string, 0)
// 	scoreCopy := make([]int, len(score))
// 	copy(scoreCopy, score)
// 	sort.Slice(scoreCopy, func(i, j int) bool {
// 		return scoreCopy[i] > scoreCopy[j]
// 	})
// 	for idx, val := range scoreCopy {
// 		var ele string
// 		switch idx {
// 		case 0:
// 			ele = "Gold Medal"
// 		case 1:
// 			ele = "Silver Medal"
// 		case 2:
// 			ele = "Bronze Medal"
// 		default:
// 			ele = strconv.Itoa(idx + 1)
// 		}
// 		mp[val] = ele
// 	}
// 	for _, val := range score {
// 		res = append(res, mp[val])
// 	}
// 	return res
// }

func findRelativeRanks22(score []int) []string {
	fmt.Printf("score: %v\n", score)
	sort.Slice(score, func(i, j int) bool {
		return score[i] > score[j]
	})
	fmt.Printf("score: %v\n", score)
	return []string{"finish", "ed"}
}

//main
func TestMain(t *testing.T) {
	intArr := []int{1, 11, 4, 32, 1, 5, 6, 53, 11, 86}
	var res []string
	//res = findRelativeRanks22(intArr)
	res = findRelativeRanks(intArr)
	fmt.Printf("res: %v\n", res)

	res2 := reverseInt(1123366448877777777)
	fmt.Printf("res2: %v\n", res2)
}

// tf := "test param" //test function here
// tf := "ghdfasdf" //test function here
// bArr := []byte(tf)
// fmt.Println("value = ", bArr)
// s := string(bArr)
// fmt.Println("value = ", s)
// str := "abcabcabcd"
// sStr := strings.Split(str, str[:1])
// fmt.Println(sStr)
