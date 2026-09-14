class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix) - 1
        column = len(matrix[0]) - 1
        i, j = 0, 0

        while i <= row:
            curr = matrix[i][j]
            if curr == target:
                return True
            if target >= curr and target <= matrix[i][column]:
                j += 1
            else:
                i += 1
                j = 0
        
        return False