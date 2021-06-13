package main_test

import (
	"testing"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func findMode(root *TreeNode) []int {
	return nil
}

//main
func TestMain(t *testing.T) {

}

func quickSort(arr []int, left int, right int) {
	if left < right {
		pivot := partition(arr, left, right)

		quickSort(arr, left, pivot-1)
		quickSort(arr, pivot+1, right)
	}
}
func partition(arr []int, left int, right int) int {
	pivot := arr[right]
	i := left - 1

	for j := left; j <= right-1; j++ {
		if arr[j] <= pivot {
			i++
			//swap
			arr[i], arr[j] = arr[j], arr[i]
		}
	}
	arr[i+1], arr[right] = arr[right], arr[i+1]
	return i + 1
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
