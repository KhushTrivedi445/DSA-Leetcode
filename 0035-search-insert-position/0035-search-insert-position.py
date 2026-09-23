class Solution(object):
    def searchInsert(self, nums, target):
        s=len(nums)-1
        for i in range(len(nums)):
            if nums[i]==target:
                return i
            else:
                if nums[s]<target:
                    return s+1
                elif nums[i]<target and nums[i+1]>target:
                    return i+1
                elif nums[0]>target:
                    return 0