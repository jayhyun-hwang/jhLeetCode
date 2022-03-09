/*
 * @lc app=leetcode id=1 lang=golang
 *
 * [1] Two Sum
 */

// @lc code=start

package main

func twoSum(nums []int, target int) []int {
	//key: difference
	//value: indexInMap
	var checkMap = make(map[int]int)

	//i: index
	for i, numInNums := range nums {
		//return when one of difference + num == target
		if indexInMap, ok := checkMap[numInNums]; ok {
			return []int{indexInMap, i}
		}
		//store difference and index
		checkMap[target-numInNums] = i
	}
	return nil
}

// @lc code=end
