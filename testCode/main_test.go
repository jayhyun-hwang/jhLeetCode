package main_test

import (
	"fmt"
	"strings"
	"testing"
)

//main
func TestMain(t *testing.T) {
	// tf := "test param" //test function here
	// tf := "ghdfasdf" //test function here
	// bArr := []byte(tf)
	// fmt.Println("value = ", bArr)
	// s := string(bArr)
	// fmt.Println("value = ", s)
	// str := "abcabcabcd"
	// sStr := strings.Split(str, str[:1])
	// fmt.Println(sStr)

	param := "2-5g-3-J"
	sArr := strings.SplitN(param, "-", 2)
	fmt.Println(sArr)

	var r byte
	r = '-'
	fmt.Println('a')
	fmt.Println(int('A'))
	fmt.Println(int('z'))
	fmt.Println(int('Z'))
	fmt.Println("\n@", r)
	//123 > byte value > 96, -32
	//'-' == 45
	k := 4
	idx := k
	needDash := true
	resR := make([]byte, 0)
	for i := 0; i < k; i++ {
		resR = append(resR, param[i])
		if param[i] == '-' {
			needDash = false
			idx = i
			break
		}
	}
	if needDash {
		resR = append(resR, '-')
	}
	count := 0
	for i := idx; i < len(param); i++ {
		switch {
		case param[i] == '-':
			continue
		case param[i] < 123 && param[i] > 96:
			resR = append(resR, param[i]-32)
			count++
		default:
			resR = append(resR, param[i])
			count++
		}
		if count == k {
			resR = append(resR, '-')
			count = 0
		}

	}
	if resR[len(resR)-1] == '-' {
		resR = resR[:len(resR)-1]
	}
	fmt.Println(string(resR))
}
