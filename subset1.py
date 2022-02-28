#
# popping method
#
import math

nums = [1,2,3]

n = len(nums)
for r in range(n+1):
    # r = no of elements in a subset
    l = math.factorial(n)/(math.factorial(r) * math.factorial(n-r))
    # l = no of subsets with r elements
    for i in range(int(l)):
        # find the subset by popping r elements from the set
        out = []
        for j in range(n - r):
            item = nums.copy()
            out.append(item.pop((i+j)%n))
        print(out)
