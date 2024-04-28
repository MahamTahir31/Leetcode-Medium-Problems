class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        mapp = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }       
        def backtrack(combination, next_digits):
            if not next_digits:
                output.append(combination)
            else:
                for letter in mapp[next_digits[0]]:
                    backtrack(combination + letter, next_digits[1:])
        
        output = []
        backtrack('', digits)
        return output


solution = Solution()
dig = input("Enter digits: ")
res = solution.letterCombinations(dig)
print("Possible combinations are: ", res)