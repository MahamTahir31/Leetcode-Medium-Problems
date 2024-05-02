class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        res = int(num1) * int(num2)
        return str(res)
        
solution = Solution()
num1 = input("Enter num1: ")
num2 = input("Enter num2: ")

res = solution.multiply(num1, num2)

print("Product of, ", num1, " and ", num2, " is ", res)