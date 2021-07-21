/*
 * @lc app=leetcode id=726 lang=golang
 *
 * [726] Number of Atoms
 */

// @lc code=start
func countOfAtoms(formula string) string {
	//map
	//bracket
	//recursive function
}

// func countOfAtoms(formula string) string {

// 	hash := map[string]int{}
// 	atoms := []string{}
// 	count := []int{}
// 	parenthesis := []int{}
// 	for i := 0; i < len(formula); {
// 		if formula[i] == '(' {
// 			parenthesis = append(parenthesis, len(atoms))
// 			i++
// 		} else if formula[i] == ')' {
// 			i++
// 			numInBytes := []byte{}
// 			for i < len(formula) {
// 				if formula[i] >= '0' && formula[i] <= '9' {
// 					numInBytes = append(numInBytes, formula[i])
// 					i++
// 				} else {
// 					break
// 				}
// 			}
// 			times, _ := strconv.Atoi(string(numInBytes))
// 			for i := parenthesis[len(parenthesis)-1]; i < len(atoms); i++ {
// 				count[i] *= times
// 			}
// 			parenthesis = parenthesis[:len(parenthesis)-1]
// 		} else {
// 			atomInBytes := []byte{formula[i]}
// 			i++
// 			for i < len(formula) {
// 				if formula[i] >= 'a' && formula[i] <= 'z' {
// 					atomInBytes = append(atomInBytes, formula[i])
// 					i++
// 				} else {
// 					break
// 				}
// 			}
// 			atoms = append(atoms, string(atomInBytes))
// 			numInBytes := []byte{}
// 			for i < len(formula) {
// 				if formula[i] >= '0' && formula[i] <= '9' {
// 					numInBytes = append(numInBytes, formula[i])
// 					i++
// 				} else {
// 					break
// 				}
// 			}
// 			if len(numInBytes) == 0 {
// 				count = append(count, 1)
// 			} else {
// 				times, _ := strconv.Atoi(string(numInBytes))
// 				count = append(count, times)
// 			}
// 		}
// 	}
// 	for i := range atoms {
// 		hash[atoms[i]] += count[i]
// 	}
// 	atomsDistinct := []string{}
// 	for k := range hash {
// 		atomsDistinct = append(atomsDistinct, k)
// 	}
// 	sort.Strings(atomsDistinct)
// 	resultInBytes := []byte{}
// 	for _, atom := range atomsDistinct {
// 		resultInBytes = append(resultInBytes, []byte(atom)...)
// 		if hash[atom] != 1 {
// 			resultInBytes = append(resultInBytes, []byte(strconv.Itoa(hash[atom]))...)
// 		}
// 	}
// 	return string(resultInBytes)
// }

// @lc code=end

