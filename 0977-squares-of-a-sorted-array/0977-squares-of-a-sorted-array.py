class Solution(object):
    def sortedSquares(self, nums):
        i=0
        for i in range(len(nums)):
            nums[i]=nums[i]*nums[i]
        nums.sort()
        return nums
         