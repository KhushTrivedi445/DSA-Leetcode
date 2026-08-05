class Solution(object):
    def removeDuplicates(self, s):
        result=[]
        for i in range(len(s)):
            if result and result[-1] == s[i]:
                result.pop()
            else:
                result.append(s[i])
                
        return "".join(result)
                            
        