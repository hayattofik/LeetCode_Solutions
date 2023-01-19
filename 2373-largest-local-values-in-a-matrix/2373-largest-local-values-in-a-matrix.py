class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        outer = len(grid)-2
        
        output = [[0] * outer for i in range(outer)]
        
        for i in range(outer):
            for j in range(outer):
                maximum = grid[i][j]
                
                for inner in range(i,i+3):
                    for inCol in range(j,j+3):
                        maximum = max(maximum,grid[inner][inCol])
                output[i][j]= maximum
        return output
                        
        