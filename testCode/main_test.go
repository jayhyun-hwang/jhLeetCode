package testCode

import (
	"fmt"
	"testing"
)

//main
func TestMain(t *testing.T) {
	fmt.Println(reverseStr("abcdefgslkvnoasnlkkj", 4))
}
func reverseStr(s string, k int) string {
	asc := false
	var res []rune
	temp := make([]rune, k)
	findStr := func() {}
	findStr = func() {
		if len(s) < k {
			if asc {
				res = append(res, []rune(s)...)
			} else {
				temp = []rune(s)
				for i, j := 0, len(temp)-1; i < j; i, j = i+1, j-1 {
					temp[i], temp[j] = temp[j], temp[i]
				}
				res = append(res, temp...)
			}
			return
		}
		temp = []rune(s[:k])
		if asc {
			res = append(res, temp...)
		} else {
			for i, j := 0, len(temp)-1; i < j; i, j = i+1, j-1 {
				temp[i], temp[j] = temp[j], temp[i]
			}
			res = append(res, temp...)
		}
		s = s[k:]
		asc = !asc
		findStr()
	}
	findStr()
	return string(res)
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
