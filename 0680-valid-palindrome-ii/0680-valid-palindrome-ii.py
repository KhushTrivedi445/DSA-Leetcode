class Solution(object):
    def validPalindrome(self, s):

        # Helper function to check if a substring is a palindrome
        def isPalindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        left = 0
        right = len(s) - 1

        while left < right:

            # If characters match, move both pointers
            if s[left] == s[right]:
                left += 1
                right -= 1

            # First mismatch
            else:
                # Try skipping the left character
                # OR try skipping the right character
                return isPalindrome(left + 1, right) or isPalindrome(left, right - 1)

        return True


