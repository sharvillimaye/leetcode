class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            row = set()
            for j in range(len(board[0])):
                if board[i][j] in row:
                    return False
                if board[i][j] != ".":
                    row.add(board[i][j])

        for i in range(len(board[0])):
            column = set()
            for j in range(len(board)):
                if board[j][i] in column:
                    return False
                if board[j][i] != ".":
                    column.add(board[j][i])
        
        for count in range(9):
            block = set()
            row_region = (int) (count / 3)
            column_region = (int) (count % 3)
            for i in range(0 + (3 * row_region), 3 + (3 * row_region)):
                for j in range(0 + (3 * column_region), 3 + (3 * column_region)):
                    if board[i][j] in block:
                        return False
                    if board[i][j] != ".":
                        block.add(board[i][j])
    
        return True