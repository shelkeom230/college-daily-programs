# 19. Find the index of two array elements whose sum is equal to the given value

# using hasmap - 0(n)
class Solution:
    def twoSum(self,nums,target):
        prevMap={}

        for i,n in enumerate(nums):
            diff=target-n 
            if diff in prevMap:
                return [prevMap[diff],i]
            prevMap[n]=i 
        return None 

solution=Solution()
nums=[2,7,11,15]
target=26
result=solution.twoSum(nums,target)
print(result)