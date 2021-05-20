package main_test

import (
	"fmt"
	"testing"
)

func TestMain(t *testing.T) {

	//tf := "test param" //test function here
	tf := "23" //test function here

	fmt.Println("tf = ", tf)
	//fmt.Println(summaryRanges([]int{-1})) //print testFunc return value
}

type Obj struct {
	idxArr []int
	stack  []byte
	resStr string
}

func reverseVowels(s string) string {
	obj := new(Obj)
	//make stack and put vowels: stack
	//store vowels' index: idxArr

}

func (obj *Obj) getRes(s string) {

}
