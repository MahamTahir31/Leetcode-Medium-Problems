class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def backtrack(board, word, row, col, index):
            if index == len(word):
                return True

            if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or board[row][col] != word[index]:
                return False
            temp = board[row][col]
            board[row][col] = '#'
            found = (backtrack(board, word, row+1, col, index+1) or
                     backtrack(board, word, row-1, col, index+1) or
                     backtrack(board, word, row, col+1, index+1) or
                     backtrack(board, word, row, col-1, index+1))

            board[row][col] = temp
            return found

        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(board, word, i, j, 0):
                    return True
        return False

solution = Solution()
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
print(solution.exist(board, word))  # Output: True

        