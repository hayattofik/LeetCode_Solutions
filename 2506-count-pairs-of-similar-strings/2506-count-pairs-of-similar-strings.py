class Solution:
    # def are_similar(self,str1,str2):
    #     for i in range(len(str1)):
    #         if str1[i] not in str2:
    #             return False
    #     return True
            
    def similarPairs(self, words: List[str]) -> int:
        # left=0
        # right=1
        # count=0
        # while(left < len(words)-1):
        #     if self.are_similar(words[right],words[left]):
        #         count+=1
        #     if right == len(words)-1:
        #         left+=1
        #         right = left +1
        #     else:
        #         right+=1
        # return count
        count=0
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if set(words[i]) == set(words[j]):
                    count+=1
        return count
                
                
                       
                      
        