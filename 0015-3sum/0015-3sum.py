class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        ans = []

        i = 0

        while i < len(nums) - 2:

            # Skip duplicate fixed elements
            if i > 0 and nums[i] == nums[i - 1]:
                i += 1
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:

                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    ans.append([nums[i], nums[left], nums[right]])

                    left += 1
                    right -= 1

                    # Skip duplicate values on the left
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    # Skip duplicate values on the right
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif total < 0:
                    left += 1

                else:
                    right -= 1

            i += 1

        return ans