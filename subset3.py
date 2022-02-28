#
# Cascading
#
# loop through each element, add one element at a time and then create a new subset by adding the element to the each subset in the list

def subsets(nums):
    output = [[]]
        
    for num in nums:
        print(num,output)
        output += [curr + [num] for curr in output]
        print(output)
       
    return output


subsets([1,2,3])[1:]
