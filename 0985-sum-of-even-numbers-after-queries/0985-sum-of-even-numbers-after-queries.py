class Solution:
        
        
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        output=[]
        even_sum=0
        even_list = filter(lambda n : n%2==0 ,nums)
        even_sum = sum(even_list)
        for i in range(len(nums)):
            if nums[queries[i][1]] %2 ==0:
                even_sum -= nums[queries[i][1]]
            nums[queries[i][1]] = nums[queries[i][1]] + queries[i][0]
            if nums[queries[i][1]] %2 ==0:
                even_sum += nums[queries[i][1]]
            output.append(even_sum)
        return output
            
            
           
            
           
      
       
            
            
        return final
        