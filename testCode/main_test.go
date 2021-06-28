package testCode

import (
	"fmt"
	"testing"
)

//main
func TestMain(t *testing.T) {
	fmt.Println(reverseStr("abcdefg", 2))
}
func reverseStr(s string, k int) string {
	// s = s[:k]
	// fmt.Println(s)
	asc := false
	var res string
	findStr := func() {}
	findStr = func() {
		if len(s) <= k {
			if asc {
				res += s
			} else {
				runeArr := []rune(s)
				for i, j := 0, len(runeArr)-1; i < j; i, j = i+1, j-1 {
					runeArr[i], runeArr[j] = runeArr[j], runeArr[i]
				}
				res += string(runeArr)
			}
			return
		}
		temp := s[:k]
		if asc {
			res += temp
		} else {
			runeArr := []rune(s)
			for i, j := 0, len(runeArr)-1; i < j; i, j = i+1, j-1 {
				runeArr[i], runeArr[j] = runeArr[j], runeArr[i]
			}
			res += string(runeArr)
		}
		s = s[k:]
		findStr()
	}
	return res
}

// func findMedianSortedArrays(nums1 []int, nums2 []int) float64 {
// 	res := 0.0
// 	numsSum := append(nums1, nums2...)
// 	sort.Ints(numsSum)
// 	nlen := len(numsSum)
// 	median := int(nlen / 2)
// 	if nlen%2 != 0 {
// 		res = float64(numsSum[median])
// 	} else {
// 		res = float64(numsSum[median-1]+numsSum[median]) / 2
// 	}
// 	return res
// }

// func findMedianSortedArrays(nums1 []int, nums2 []int) float64 {
// 	mp := make(map[int]bool)
// 	numsSum := make([]int, 0)
// 	res := 0.0
// 	for _, val := range nums1 {
// 		if !mp[val] {
// 			numsSum = append(numsSum, val)
// 			mp[val] = true
// 		}
// 	}
// 	for _, val := range nums2 {
// 		if !mp[val] {
// 			numsSum = append(numsSum, val)
// 			mp[val] = true
// 		}
// 	}
// 	sort.Slice(numsSum, func(i, j int) bool {
// 		return numsSum[i] < numsSum[j]
// 	})
// 	nlen := len(numsSum)
// 	median := int(nlen / 2)
// 	if nlen%2 == 1 {
// 		res = float64(numsSum[median])
// 	} else {
// 		res = float64(numsSum[median-1]+numsSum[median]) / 2
// 	}
// 	return res
// }

// tf := "test param" //test function here
// tf := "ghdfasdf" //test function here
// bArr := []byte(tf)
// fmt.Println("value = ", bArr)
// s := string(bArr)
// fmt.Println("value = ", s)
// str := "abcabcabcd"
// sStr := strings.Split(str, str[:1])
// fmt.Println(sStr)
