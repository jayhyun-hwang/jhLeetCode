package main_test

import (
	"fmt"
	"testing"
)

func TestMain(t *testing.T) {

	//tf := "test param" //test function here
	tf := "23" //test function here

	fmt.Println("tf = ", tf)
	fmt.Println(tf) //print testFunc return value
}

type NumsObj struct {
	intArr [2]int
	res    []string
}

func summaryRanges(nums []int) []string {
	obj := new(NumsObj)
	if len(nums) > 0 {
		obj.intArr[0] = nums[0]
		obj.recRange(nums, 0)
	}
	return obj.res
}
func (obj *NumsObj) recRange(nums []int, i int) {
	if len(nums)-1 == i {
		if obj.intArr[0] > obj.intArr[1] {
			obj.res = append(obj.res, (string)(obj.intArr[0]))
		}
		return
	}
	if nums[i]+1 != nums[i+1] {
		obj.intArr[1] = nums[i]
		var strEle string
		if obj.intArr[0] == obj.intArr[1] {
			strEle = (string)(obj.intArr[0])
		} else {
			strEle = (string)(obj.intArr[0]) + "->" + (string)(obj.intArr[1])
		}
		obj.res = append(obj.res, strEle)
		obj.intArr[0] = nums[i+1]
	} else {
		obj.intArr[1] = nums[i+1]
	}
	i++
	obj.recRange(nums, i)
}
