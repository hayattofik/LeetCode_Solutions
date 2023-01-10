class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        onesRow = defaultdict(int)
        onesColumn = defaultdict(int)
        output=[]
        
        #make reference for rows and columns with 1 value
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    onesRow[row] += 1
                    onesColumn[col] +=1
                    
        #calculate the difference 
        for row in range(len(grid)):
            diffRow=[]
            for col in range(len(grid[0])):
                diff = onesRow[row] + onesColumn[col] - (len(grid[0])-onesRow[row]) - (len(grid)-onesColumn[col])
                diffRow.append(diff)
            output.append(diffRow)
            
            
        return output
                
                
        