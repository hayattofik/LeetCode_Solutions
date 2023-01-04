class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        
        row_dic= {}
        count = 0
        
        for row in grid:
            if tuple(row) in row_dic:
                row_dic[tuple(row)] +=1
            else:
                row_dic[tuple(row)] = 1
                
        for inner in range(len(grid)):
            column = []
            for outer in range(len(grid)):
                column.append(grid[outer][inner])
                
            if tuple(column) in row_dic:
                count += row_dic[tuple(column)]
        return count
                
            
        