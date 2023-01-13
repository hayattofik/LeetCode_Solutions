class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        col = len(matrix[0])
        row = len(matrix)
        
        for col in matrix:
            col = set(col)
        
        for row in matrix:
            if row[-1] >= target and target in row:
                return True
        return False
        