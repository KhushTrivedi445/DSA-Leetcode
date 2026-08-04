class Solution(object):
    def findMissingElements(self, nums):
        low = min(nums)
        high = max(nums)

        full_range = set(range(low, high + 1))
        nums_set = set(nums)

        missing = sorted(list(full_range - nums_set))

        return missing