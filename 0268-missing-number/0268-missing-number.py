class Solution(object):
    def missingNumber(self, nums):
        len_n=len(nums)
        sum=len_n*(len_n+1)//2
        s=0
        for i in range(len(nums)):
            s=s+nums[i]
        
        result=sum-s
        return result
        