from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        valid_set = set()
        """Rows"""
        for i in range(9):
            for j in range(9):
                if not board[i][j].isnumeric():
                    continue

                if board[i][j] in valid_set:
                    return False
                valid_set.add(board[i][j])
            valid_set = set()

        """Columns"""
        for i in range(9):
            for j in range(9):
                if not board[j][i].isnumeric():
                    continue

                if board[j][i] in valid_set:
                    return False
                valid_set.add(board[j][i])
            valid_set = set()

        """Squares"""
        for k in range(9):
            for i in range(3):
                for j in range(3):
                    if not board[i + ((k % 3) * 3)][j + (int(k / 3) * 3)].isnumeric():
                        continue

                    if board[i + ((k % 3) * 3)][j + (int(k / 3) * 3)] in valid_set:
                        return False
                    valid_set.add(board[i + ((k % 3) * 3)][j + (int(k / 3) * 3)])
            valid_set = set()

        return True
