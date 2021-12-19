- for문 step

```python
from typing import List


def solution(x: int, n: int) -> List[int]:
    answear = []
    for i in range(n):
        answear.append(i * x)
    return answear
```

- dequeue 캐시

```python
import collections
from typing import List


def solution(cacheSize: int, cities: List[str]) -> int:
    if cacheSize < 1:
        return len(cities) * 5
    answer = 0
    cache = collections.deque()
    for city in cities:
        city = city.lower()
        if city in cache:
            cache.remove(city)
            cache.append(city)
            answer += 1
        else:
            if len(cache) >= cacheSize:
                cache.popleft()
            cache.append(city)
            answer +=5
    return answer
```

- 이진변환

```python
from typing import List

# 문자열을 이진수로 바꾸고 0 지우기
def solution(s: str) -> List[int]:
    answer = [0,0]

    while True:
        if len(s) == 1:
            break
        for val in s:
            if val == "0":
                answer[1] += 1
        s = s.replace("0","")
        s = bin(len(s))[2:]
        answer[0] += 1

    return answer
```

- 재귀, DFS

```python
from typing import List

def solution(arr: List[List[int]]) -> List[int]:
    answer = [0,0]
    if len(arr) == 1:
        if arr[0][0] == 0:
            return [1,0]
        else:
            return [0,1]
    #정사각 2차 배열    
    n = len(arr)
    tempArr = arr
    def comp(row: int, col: int, leng: int):
        val = arr[row][col]
        for rowIdx in range(row, row+leng):
            for colIdx in range(col, col+leng):
                if arr[rowIdx][colIdx] != val:
                    leng //= 2
                    comp(row, col, leng)
                    comp(row, col + leng, leng)
                    comp(row + leng, col, leng)
                    comp(row + leng, col + leng, leng)
                    return
        answer[val] += 1
    comp(0, 0, n)
    return answer
```

- 힙

```python
from typing import List
import heapq

# 정렬을 유지하는 스코빌 리스트
def solution(scoville: List[int], K: int) -> int:
    if K < 1:
        return 0
    
    answer = 0

    # 리스트를 힙으로(이진 min 힙)
    # heapq.heapify(scoville)
    heap = []
    for val in scoville:
        heapq.heappush(heap, val)
    print(heap)    

    # 
    while True:
        if heap[0] >= K:
                break
        else:
            if len(heap) == 1:
                return -1
            else:
                heapq.heappush(heap, heapq.heappop(heap) + heapq.heappop(heap) * 2)
                answer += 1
    return answer
```

- List + set 검사

```python
from typing import List

# 신고 리스트 보고 결과(횟수와 여부) 구현 - 중복 검사
def solution(id_list: List[str], report: List[str], k: int):
    answer = []

    dic1 = dict()
    for rep in report:
        spl = rep.split(" ")
        reporter, reported = spl[0], spl[1]
        if reported not in dic1:
            dic1[reported] = [0,set()]
        if reporter not in dic1[reported][1]:
            dic1[reported][1].add(reporter)
            dic1[reported][0] += 1
    
    print(dic1)

    dic2 = dict()
    for val in dic1.values():
        if val[0] >= k:
            for re in val[1]:
                if re not in dic2:
                    dic2[re] = 0
                dic2[re] += 1
    print(dic2)

    for id in id_list:
        if id in dic2:
            answer.append(dic2[id])
        else:
            answer.append(0)
    return answer
```

