class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        onesRow=defaultdict(int)
        onesColumn = defaultdict(int)
        output=[]
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    onesRow[row] += 1
                    onesColumn[col] +=1
        
        for i in range(len(grid)):
            temp=[]
            for j in range(len(grid[0])):
                
                diff = onesRow[i] + onesColumn[j] - (len(grid[0])-onesRow[i]) - (len(grid)-onesColumn[j])
               
                temp.append(diff)
            output.append(temp)
        return output
                
                
        