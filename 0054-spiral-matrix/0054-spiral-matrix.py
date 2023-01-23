class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        output= [ ]
        left = 0
        right = len(matrix[0])
        top= 0
        bot= len(matrix)
        
        while(top < bot and left < right):
            # get the elements in the top row
            for i in range(left,right):
                output.append(matrix[top][i])
            top+=1
            # get the elements  in the right col
            for j in range(top,bot):
                output.append(matrix[j][right-1])
            right -=1
            
            # to incompass one row and one column matrices
            if not(left < right and top < bot):
                break
            
            # get the elements in the bottom ro
            for i in range(right-1,left-1,-1):
                output.append(matrix[bot-1][i])
            bot -=1
            # get every element in the left from bottom to top
            for i in range(bot - 1 , top - 1, -1):
                output.append(matrix[i][left])
            left +=1
            
        return output
        