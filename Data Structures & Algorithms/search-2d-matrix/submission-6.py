class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        matrixRowLength = len(matrix)
        matrixColumnLength = len(matrix[0])
        r, c = 0, 0

        while r < matrixRowLength:
            if matrix[r][0] <= target <= matrix[r][matrixColumnLength-1]:
                while c < matrixColumnLength:
                    print(matrix[r][c])
                    if matrix[r][c] == target:
                        return True
                    c+=1
            r+=1
        return False