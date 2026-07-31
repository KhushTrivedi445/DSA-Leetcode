class Solution(object):
    def rotateString(self, s, goal):
        if len(s)!=len(goal):
            return False
        
        concatenated=s+s

        if goal in concatenated:
            return True
        else:
            return False
        