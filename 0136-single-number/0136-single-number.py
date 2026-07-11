class Solution(object):
    def singleNumber(self, nums):
        count=0
        i=0
        while i < len(nums):
            if nums.count(nums[i]) == 1:
                return nums[i]
            i += 1
        