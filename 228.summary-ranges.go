/*
 * @lc app=leetcode id=228 lang=golang
 *
 * [228] Summary Ranges
 */

// @lc code=start
type NumsObj struct {
	intArr [2]int
	res    []string
}

func summaryRanges(nums []int) []string {
	obj := new(NumsObj)
	if len(nums) > 0 {
		obj.intArr[0] = nums[0]
		obj.intArr[1] = nums[0]
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
		var strEle string
		if obj.intArr[0] >= obj.intArr[1] {
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

// @lc code=end
