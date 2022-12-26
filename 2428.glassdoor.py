class Solution(object):
    def maxSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        total=0
        rows=len(grid)
        col=len(grid[0])
        for i in range(1,rows-1):
            for j in range(1,col-1):
                sumis=grid[i][j] + sum(grid[i-1][j-1:j+2])+sum(grid[i+1][j-1:j+2])
                if sumis >total:
                    total=sumis
        return total