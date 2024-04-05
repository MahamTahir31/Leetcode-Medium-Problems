class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        left = 0
        right = len(height) - 1
        
        while left < right:
            current_area = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, current_area)
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area

if __name__ == "__main__":
    height1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    height2 = [1, 1]
    
    solution = Solution()
    
    print("Max area for height1:", solution.maxArea(height1))  # Output: 49
    print("Max area for height2:", solution.maxArea(height2))  # Output: 1
