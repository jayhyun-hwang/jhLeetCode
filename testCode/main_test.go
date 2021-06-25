package testCode

import (
	"testing"
)

//main
func TestMain(t *testing.T) {

}

// A65
// Z90
// a97
// z122
type Obj struct {
	word        string
	idx         int
	shouldUpper bool
}

func detectCapitalUse(word string) bool {
	if len(word) == 1 {
		return true
	}
	var firstIsUp bool
	if word[0] < 91 {
		firstIsUp = true
	} else {
		firstIsUp = false
	}
	obj := new(Obj)
	obj.word = word
	if word[1] < 91 {
		obj.shouldUpper = true
	} else {
		obj.shouldUpper = false
	}
	if !firstIsUp && obj.shouldUpper {
		return false
	}
	var piv byte
	if obj.shouldUpper {
		piv = 64
	} else {
		piv = 96
	}
	obj.idx = 2
	return obj.findSol(piv)
}
func (obj *Obj) findSol(piv byte) bool {
	if obj.idx >= len(obj.word) {
		return true
	}
	if obj.word[obj.idx] > piv && obj.word[obj.idx] < piv+27 {
		obj.idx++
		return obj.findSol(piv)
	}
	return false
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
