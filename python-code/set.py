# 1. 교집합
set1 = set([1, 2, 3, 4, 5, 6])
set2 = set([3, 4, 5, 6, 8, 9])
print(set1 & set2)
print(set1.intersection(set2))
# {3, 4, 5, 6}

# 2. 합집합
set1 = set([1, 2, 3, 4, 5, 6])
set2 = set([3, 4, 5, 6, 8, 9])
print(set1 | set2)
print(set1.union(set2))
# {1, 2, 3, 4, 5, 6, 8, 9}

# 차집합
set1 = set([1, 2, 3, 4, 5, 6])
set2 = set([3, 4, 5, 6, 8, 9])
print(set1 - set2)
print(set1.difference(set2))
# {1, 2}
