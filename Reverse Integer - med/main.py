class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # Handle negative numbers
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        # Reversing the digits
        reverse_x = 0
        while x != 0:
            # Pop the last digit from x
            pop = x % 10
            x //= 10
            
            # Check for overflow
            if reverse_x > (2**31 - 1) // 10 or (reverse_x == (2**31 - 1) // 10 and pop > 7):
                return 0
            if reverse_x < (-2**31) // 10 or (reverse_x == (-2**31) // 10 and pop < -8):
                return 0
            
            # Push the popped digit to reverse_x
            reverse_x = reverse_x * 10 + pop
        
        return sign * reverse_x

# Main program
if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    test_cases = [123, -123, 120]
    for x in test_cases:
        print("Input:", x)
        print("Output:", solution.reverse(x))
