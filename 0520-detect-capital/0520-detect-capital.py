class Solution(object):
    def detectCapitalUse(self, word):
        count=0
        for i in range(len(word)):
            if word[i].isupper():
                count += 1

        if count==len(word):
            return True
        elif count==0:
            return True
        elif count==1 and word[0].isupper():
            return True
        else:
            return False

    
        