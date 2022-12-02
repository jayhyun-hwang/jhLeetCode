import sys

print(sys.getrecursionlimit)
def minimumBribes(q):
    # Write your code here
    bribes = 0
    mins = [sys.maxsize, sys.maxsize]
    for i, p in reversed(list(enumerate(q, 1))):
        if p - i > 2:
            print('Too chaotic')
            return
        elif p > mins[1]:
            bribes += 2
        elif p > mins[0]:
            bribes += 1
            mins = (p, mins[0])
        elif p < mins[1]:
            mins = (mins[0], p)
    print(bribes)


print(minimumBribes([1, 2, 5, 3, 7, 8, 6, 4]))  # 7
