class Solution:
    def myAtoi(self, s):
        i = 0
        n = len(s)

        # Skip leading whitespaces
        while i < n and s[i] == ' ':
            i += 1

        # Check sign
        sign = 1
        if i < n and (s[i] == '+' or s[i] == '-'):
            if s[i] == '-':
                sign = -1
            i += 1

        num = 0
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # Convert digits
        while i < n and s[i].isdigit():
            num = num * 10 + int(s[i])

            # Clamp to 32-bit signed integer range
            if sign == 1 and num > INT_MAX:
                return INT_MAX
            if sign == -1 and -num < INT_MIN:
                return INT_MIN

            i += 1

        return sign * num