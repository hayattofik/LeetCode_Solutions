class Solution:
    def minDeletionSize(self, strs: list[str]) -> int:
        order = 0 
        col = len(strs[0])
        row = len(strs)
        columns =[]
        
        for i in range(col):
            temp=[]
            for j in range(row):
               
                temp.append(strs[j][i])

            columns.append(temp)
        
        for i in range(len(columns)):
            for j in range(len(columns[0])-1):
                
                if columns[i][j] > columns[i][j+1]:
                    order+=1
                    break
        return order