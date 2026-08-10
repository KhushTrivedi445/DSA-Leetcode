class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        count = {}

        # Count characters in magazine
        for i in range(len(magazine)):
            count[magazine[i]] = count.get(magazine[i], 0) + 1

        # Use characters for ransomNote
        for i in range(len(ransomNote)):
            if count.get(ransomNote[i], 0) == 0:
                return False

            count[ransomNote[i]] -= 1

        return True
        

      
        