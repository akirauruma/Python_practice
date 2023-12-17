from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        def validRow(board):
            for i in range(9):
                l = [0] * 9
                for j in range(9):
                    if board[i][j] != ".":
                        if l[int(board[i][j]) - 1] == 1:
                            return False
                        else:
                            l[int(board[i][j]) - 1] = 1
            return True

        def validColumn(board):
            for i in range(9):
                l = [0] * 9
                for j in range(9):
                    if board[j][i] != ".":
                        if l[int(board[j][i]) - 1] == 1:
                            return False
                        else:
                            l[int(board[j][i]) - 1] = 1
            return True

        return validRow(board) and validColumn(board)

sudoku = Solution()

board = [
    ["5","3","4","6","7","8","9","1","2"],
    ["6","7","2","1","9","5","3","4","8"],
    ["1","9","8","3","2","4","5","6","7"],
    ["8","1","6","5","4","2","7","9","3"],
    ["4","2","3","9","6","7","8","5","1"],
    ["7","5","9","8","3","1","4","2","6"],
    ["9","6","1","7","5","3","2","8","4"],
    ["2","8","7","4","1","9","6","3","5"],
    ["3","4","5","2","8","6","1","7","9"]
]

result = sudoku.isValidSudoku(board)

print(result)
