/*
 * @lc app=leetcode id=389 lang=golang
 *
 * [389] Find the Difference
 */

// @lc code=start
func findTheDifference(s string, t string) byte {
	if len(s) == 0 {
		return t[0]
	}
	bmap := make(map[byte]int)
	sbarr := []byte(s)
	for _, val := range sbarr {
		bmap[val]++
	}

	tbarr := []byte(t)
	for _, val := range tbarr {
		bmap[val]--

		if bmap[val] == -1 {
			return val
		}
	}

	return t[0]
}

// @lc code=end

/*
func findTheDifference(s string, t string) byte {
	tbarr := []byte(t)
	bmap := make(map[byte]int)

	for _, val := range tbarr {
		if _, ok := bmap[val]; ok {
		bmap[val] += 1
		} else {
			bmap[val] = 0
		}
		bmap[val] += 1

	}

	sbarr := []byte(s)
	for _, val := range sbarr {
		if _, ok := bmap[val]; ok {
			bmap[val] += 1
		} else {
			bmap[val] = 0
		}
		bmap[val] += 1
	}
	for i, mval := range bmap {
		fmt.Println("value= ", mval)
		fmt.Println("key= ", i)

		if mval%2 == 1 {

			return i
		}
	}
	return 0
}
*/