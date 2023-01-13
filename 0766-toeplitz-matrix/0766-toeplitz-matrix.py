class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
#         cores =[]
#         for i in range(len(matrix[0])):
#             cores.append([0,i])
#         for j in range(len(matrix)):
#             cores.append([j,0])
      
#         for value in cores:
#             row=value[0]
#             col = value[1]
#             r=row 
#             c=col 
            
#             while(r<len(matrix) and col<len(matrix[0])):
#                 r+=1
#                 c+1
#                 if matrix[row][col] != matrix[r][c]:
#                         return False
                
                
#         return True
          for i in range(len(matrix)-1):
                for j in range(len(matrix[0])-1):
                    if(matrix[i][j] != matrix[i+1][j+1]):
                        return False
        
    
          return True;
