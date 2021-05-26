package main_test

import (
	"fmt"
	"strconv"
	"testing"
)

func TestMain(t *testing.T) {

	//tf := "test param" //test function here
	tf := "ghdfasdf" //test function here
	bArr := []byte(tf)
	fmt.Println("value = ", bArr)
	s := string(bArr)
	fmt.Println("value = ", s)
	_ = addStrings("9333852702227987", "85731737104263")

	//fmt.Println(summaryRanges([]int{-1})) //print testFunc return value
}
func addStrings(num1 string, num2 string) string {
	conNum1, _ := strconv.ParseFloat(num1, 64)
	conNum2, _ := strconv.ParseFloat(num2, 64)
	res := fmt.Sprintf("%f", conNum1+conNum2)
	return res[:len(res)-7]
}
