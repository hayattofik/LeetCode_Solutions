class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        
        result=[]
        for i in range(len(matrix[0])):
            arr=[]
            for j in range(len(matrix)):
                arr.append(matrix[j][i])
            result.append(arr)
        return result
            


       