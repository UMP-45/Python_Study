
def two(nums , target):
    for i in range(len(nums)-1):
        for j in range(i+1,len(nums)):
            if target == nums[i] + nums[j]:
                print(nums[i],nums[j],i,j)
.
two([1,2,3,4],5)