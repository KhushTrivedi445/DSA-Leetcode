class Solution(object):
    def lengthOfLongestSubstring(self, s):
        result=""
        max_length=0

        for i in range(len(s)):
            if (s[i] in result):
                result=result[result.index(s[i])+1:]

            result=result+s[i]
            max_length=max(max_length,len(result))
        
        return max_length
        
        