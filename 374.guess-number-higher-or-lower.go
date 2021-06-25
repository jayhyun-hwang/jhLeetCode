/*
 * @lc app=leetcode id=374 lang=golang
 *
 * [374] Guess Number Higher or Lower
 */

// @lc code=start
/**
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is lower than the guess number
 *			      1 if num is higher than the guess number
 *               otherwise return 0
 * func guess(num int) int;
 */
type Obj struct {
	low    int
	top    int
	picked int
	res    int
}

//yet
func guessNumber(n int) int {
	obj := new(Obj)
	obj.picked = n
	obj.low = 1
	obj.top = int(math.Pow(2, 31) - 1)
	guess := int(math.Pow(2, 30))
	return obj.findPicked(guess)
}
func (obj *Obj) findPicked(n int) int {
	if obj.picked == n {
		return 0
	}
	return 0
}

// @lc code=end

