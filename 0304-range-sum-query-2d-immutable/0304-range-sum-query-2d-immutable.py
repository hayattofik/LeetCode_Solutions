class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows,cols=len(matrix),len(matrix[0])
        self.sum=[[0] *(cols +1) for i in range(rows+1)]
    
        for r in range(rows):
            presum=0
            for c in range(cols):
                presum+=matrix[r][c]
                above=self.sum[r][c+1]
                self.sum[r+1][c+1]=presum + above
       

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
       return self.sum[row2+1][col2+1]-self.sum[row2+1][col1]-self.sum[row1][col2+1]+self.sum[row1][col1]




        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)