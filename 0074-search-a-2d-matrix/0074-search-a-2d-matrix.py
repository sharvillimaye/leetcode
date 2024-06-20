class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        num_rows, num_cols = len(matrix), len(matrix[0])
        total_length = num_rows * num_cols
        left, right = 0, total_length - 1

        while left <= right:
            middle = (left + ((right - left) // 2))
            row, column = middle // num_cols, middle % num_cols
            if (matrix[row][column] < target):
                left = middle + 1
            elif (matrix[row][column] > target):
                right = middle - 1
            else:
                return True
        
        return False