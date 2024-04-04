class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Remove leading whitespace
        s = s.lstrip()
        
        if not s:
            return 0
        
        # Check if the first character is a sign
        sign = 1
        if s[0] == '-':
            sign = -1
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]

        # Read digits until non-digit character is found
        result = 0
        for char in s:
            if char.isdigit():
                result = result * 10 + int(char)
            else:
                break
        
        # Apply sign and clamp the result
        result *= sign
        result = max(min(result, 2**31 - 1), -2**31)
        
        return result

if __name__ == "__main__":
    solution = Solution()
    test_cases = ["42", "   -42", "4193 with words"]
    
    for s in test_cases:
        print("Input:","'",s,"'"
              )
        print("Output:", solution.myAtoi(s))
        print()
