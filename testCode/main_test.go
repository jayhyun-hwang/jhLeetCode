package main_test

import (
	"fmt"
	"log"
	"net/http"
	_ "net/http/pprof"
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

type WorkResult struct {
	UserID  int64
	Wt1Time int32
	Payment int64
}

//main
func TestMain(t *testing.T) {
	param1 := "a"
	param2 := "c"
	wWorkResults := []WorkResult{}
	for i := 0; i < 100; i++ {
		w := new(WorkResult)
		w.UserID = int64(i % 10)
		w.Wt1Time = int32(i)
		w.Payment = int64(i * 1000)
		wWorkResults = append(wWorkResults, *w)
	}
	wWorkResults2 := make([]WorkResult, 100)
	var totalWorkTime int32
	var totalPayment int64
	totalWorkTime = 0
	totalPayment = 0
	if param1 != "" {
		//이름으로 검색할 경우, 여러 id의 사용자가 조회될 수 있다. 이럴 때는 total 수치를 넘겨주지 않는다.
		if param2 == "b" {
			//검색된 id의 개수를 체크하기위한 map
			checkUserCountMp := make(map[int64]bool)
			isOneUser := true
			for idx, wWorkResult := range wWorkResults {
				tnaResult := wWorkResult
				if isOneUser {
					totalWorkTime += wWorkResult.Wt1Time
					totalPayment += wWorkResult.Payment
					if !checkUserCountMp[wWorkResult.UserID] {
						checkUserCountMp[wWorkResult.UserID] = true
						if len(checkUserCountMp) > 1 {
							isOneUser = false
							totalWorkTime = 0
							totalPayment = 0
						}
					}
				}
				wWorkResults2[idx] = tnaResult
			}
			fmt.Println("1 finished")
		} else {
			for idx, wWorkResult := range wWorkResults {
				tnaResult := wWorkResult
				totalWorkTime += wWorkResult.Wt1Time
				totalPayment += wWorkResult.Payment
				wWorkResults2[idx] = tnaResult
			}
			fmt.Println("2 finished")
		}
	} else {
		//total 연산없이 진행
		for idx, wWorkResult := range wWorkResults {
			tnaResult := wWorkResult
			wWorkResults2[idx] = tnaResult
		}
		fmt.Println("3 finished")
	}

	log.Println(http.ListenAndServe("localhost:6060", nil))
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
