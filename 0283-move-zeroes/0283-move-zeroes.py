class Solution(object):
    def moveZeroes(self, nums):
        i = 0
        j = 0

        while i < len(nums):

            # If the current element is non-zero,
            # move it to the j-th position.
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1

            # Always move i
            i += 1

        