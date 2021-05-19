package main_test

import (
	"fmt"
	"strconv"
	"testing"
)

func TestMain(t *testing.T) {

	//tf := "test param" //test function here
	tf := "23" //test function here

	fmt.Println("tf = ", tf)
	fmt.Println(summaryRanges([]int{-1})) //print testFunc return value
}

type NumsObj struct {
	intArr []int
	res    []string
}

func summaryRanges(nums []int) []string {
	obj := new(NumsObj)
	if len(nums) > 0 {
		obj.intArr = make([]int, 0, 2)
		obj.intArr[0] = nums[0]
		obj.recRange(nums, 0)
	}
	return obj.res
}
func (obj *NumsObj) recRange(nums []int, i int) {
	if len(nums)-1 == i {
		if obj.intArr[0] >= obj.intArr[1] {
			obj.res = append(obj.res, strconv.Itoa(obj.intArr[0]))
		} else {
			obj.res = append(obj.res, strconv.Itoa(obj.intArr[0])+"->"+strconv.Itoa(obj.intArr[1]))
		}
		return
	}
	if nums[i]+1 != nums[i+1] {
		obj.intArr[1] = nums[i]
		var strEle string
		if obj.intArr[0] == obj.intArr[1] {
			strEle = strconv.Itoa(obj.intArr[0])
		} else {
			strEle = strconv.Itoa(obj.intArr[0]) + "->" + strconv.Itoa(obj.intArr[1])
		}
		obj.res = append(obj.res, strEle)
		obj.intArr[0] = nums[i+1]
	} else {
		obj.intArr[1] = nums[i+1]
	}
	i++
	obj.recRange(nums, i)
}
