package main

import (
	"fmt"

	"github.com/dustin/go-humanize"
)

type Obj2 struct {
	res           float64
	res2          float64
	monthSave     float64
	seed          float64
	seed2         float64
	monthInterest float64
	months        float64
}

func (obj *Obj2) calcul() {

	for i := 0; i < int(obj.months); i++ {
		obj.seed += obj.monthSave
		obj.seed2 += obj.monthSave
		obj.seed *= obj.monthInterest
		obj.res2 += obj.seed2 * (obj.monthInterest - 1)
	}
	obj.res = obj.seed
	obj.res2 += obj.seed2
}
func main() {
	for {
		inputCalculate()
	}
}
func inputCalculate() {

	var inSeed float64
	var err error
	err = nil
LABEL1:
	fmt.Print("초기 시드머니(원): ")
	_, err = fmt.Scanln(&inSeed)
	if err != nil {
		fmt.Scanln()
		fmt.Println("숫자만 입력해주세요 수현님...")
		goto LABEL1
	}
	fmt.Println()

	var inMonthSave float64
LABEL2:
	fmt.Print("매달 저금할 금액(원): ")
	_, err = fmt.Scanln(&inMonthSave)
	if err != nil {
		fmt.Scanln()
		fmt.Println("숫자만 입력해주세요 수현님...")
		goto LABEL2
	}
	fmt.Println()
	var inInterest float64
LABEL3:
	fmt.Print("수익율(%, 예: 2% => 2 입력): ")
	_, err = fmt.Scanln(&inInterest)
	if err != nil {
		fmt.Scanln()
		fmt.Println("숫자만 입력해주세요 수현님...")
		goto LABEL3
	}
	fmt.Println()
	var inMonths float64
LABEL4:
	fmt.Print("기간(개월): ")
	_, err = fmt.Scanln(&inMonths)
	if err != nil {
		fmt.Scanln()
		fmt.Println("숫자만 입력해주세요 수현님...")
		goto LABEL4
	}
	//fmt.Println("seed ", inSeed, " monthSave ", inMonthSave)
	//fmt.Println("interest ", inInterest, " months ", inMonths)

	obj := new(Obj2)
	obj.monthSave = inMonthSave
	obj.seed = inSeed
	obj.seed2 = inSeed
	var interest float64
	interest = inInterest
	obj.monthInterest = 1 + interest/100
	//fmt.Printf("수익률= %f\n", obj.monthInterest)
	fmt.Printf("\n결과는...........\n두구두구\n두구두구두구두구두구\n\n")
	obj.months = inMonths
	obj.calcul()
	a := humanize.Comma(int64(obj.res))
	b := humanize.Comma(int64(obj.res2))
	fmt.Printf("복리결과= %s 원\n", a)
	fmt.Printf("단리결과= %s 원\n", b)
	fmt.Printf("\n---------------reset---------------")
	fmt.Printf("\n-----------종료: Ctrl + c----------\n\n")
	//fmt.Printf("복리결과= %d 원\n", int(obj.res))
	//fmt.Printf("단리결과= %d 원\n", int(obj.res2))
	//fmt.Printf("복리결과= %f원\n", obj.res)
	//fmt.Printf("단리결과= %f원\n", obj.res2)
}
