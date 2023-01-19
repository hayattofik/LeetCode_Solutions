class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        row = len(mat)
        col = len(mat[0])
        if row * col != r * c :
            return mat
        else:
            output = [ [0 for j in range(c)]  for i in range(r)]
            print(output)
            allMat =[]
            for i in range(row):
                for j in range(col):
                    allMat.append(mat[i][j])
            print(allMat)
            i=0
            for j in range(r):
                
                for k in range(c):
                   
                    output[j][k] =  allMat[i]
                    i+=1
                    
            return output