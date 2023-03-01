class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        value = self.getRow(rowIndex-1)
        output =[1]
        for i in range(1,len(value)):
          
            output.append(value[i]+value[i-1])
                
        output.append(1)
            
        return output
        
        