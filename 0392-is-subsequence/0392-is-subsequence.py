class Solution(object):
    def isSubsequence(self, s, t):
        i=0
        j=0

        if s=="":
            return True

        while(i<len(t) and j<len(s)):
            if (t[i]==s[j]):
                j+=1
            i+=1  
        if j==len(s):
            return True
        else:
            return False
