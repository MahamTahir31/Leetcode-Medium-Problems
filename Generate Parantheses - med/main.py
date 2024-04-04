class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def backtrack(s, left, right):
            if len(s) == 2 * n:
                result.append(s)
                return
            if left < n:
                backtrack(s + '(', left + 1, right)
            if right < left:
                backtrack(s + ')', left, right + 1)
        
        result = []
        backtrack("", 0, 0)
        return result


sol = Solution()
print(sol.generateParenthesis(3)) 
print(sol.generateParenthesis(1)) 
