class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest_length = 0
        start = 0
        seen = {}  

        for i, char in enumerate(s):
            # If the current character is already seen within the window
            if char in seen and seen[char] >= start:
                # Update the start of the window to exclude the repeating character
                start = max(start, seen[char] + 1)

            # Update the length of the current substring
            longest_length = max(longest_length, i - start + 1)

            # Add the current character and its index to the seen dictionary
            seen[char] = i

        return longest_length

solution = Solution()

input_string = "abcabcbb"  
longest_length = solution.lengthOfLongestSubstring(input_string)
print("Length of the longest substring without repeating characters:", longest_length)