function solution(k, tangerine) {
  var answer = 0
  const count_map = {}
  tangerine.forEach((ele) => {
    if (count_map[ele] == null) count_map[ele] = 0
    count_map[ele]++
  })

  // const sorted_count_list = Object.entries(count_map)
  // sorted_count_list.sort((a, b) => b.at(1) - a.at(1))
  // for (const [_, v] of sorted_count_list) {
  //     if (k <= 0) break
  //     answer++
  //     k -= v
  // }

  const sorted_value_list = Object.values(count_map)
  sorted_value_list.sort((a, b) => b - a)
  for (const count of sorted_value_list) {
    if (k <= 0) break
    answer++
    k -= count
  }
  return answer
}
