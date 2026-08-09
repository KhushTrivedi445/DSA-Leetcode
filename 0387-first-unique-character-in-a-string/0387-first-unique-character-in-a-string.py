class Solution(object):
    def firstUniqChar(self, s):
        count = {}

        # Count each character
        for i in range(len(s)):
            count[s[i]] = count.get(s[i], 0) + 1

        # Find the first character that appears once
        for i in range(len(s)):
            if count[s[i]] == 1:
                return i

        return -1
        
        