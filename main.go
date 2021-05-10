package main

import "fmt"

func main() {
	tf := isValid("(){}{()}[]")
	fmt.Println("tf = ", tf)
}
func isValid(s string) bool {
	bmap := map[rune]rune{
		'{': '}',
		'[': ']',
		'(': ')',
	}
	sslice := make([]rune, 0)

	for _, val := range s {
		if mval, ok := bmap[val]; ok {
			sslice = append(sslice, mval)
		} else {
			if val != sslice[len(sslice)-1] {
				return false
			} else {
				sslice = sslice[:len(sslice)-2]
			}
		}
	}
	if len(sslice) > 0 {
		return false
	}
	return true
}
