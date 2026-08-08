class Solution(object):
    def findLonely(self, nums):
        result = []
        count = {}

        for x in nums:
            count[x] = count.get(x, 0) + 1

        for x in nums:
            if count[x] == 1:
                if (x - 1 not in count) and (x + 1 not in count):
                    result.append(x)

        return result