#
# bitmask method
#
# Generate all the combinations of a bitmask, 
# add the elements based on the bitmask
#

def subset(nums, comb):
  out = []
  for i in range(16):
    if comb & 1 << i:
       out.append(nums[i]) 
  return out

nums = [1,2,3]

for i in range(2**len(nums)):
    print(subset(nums,i))
