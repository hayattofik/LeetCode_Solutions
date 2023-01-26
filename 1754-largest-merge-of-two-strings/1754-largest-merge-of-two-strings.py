class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        w1_ptr = 0
        w2_ptr = 0
        
        merged =[]
        while(w1_ptr < len(word1) and w2_ptr < len(word2)):
            cur = word1[w1_ptr:]
            cur2 = word2[w2_ptr:]
            if cur  > cur2:
                merged.append(cur[0])
                w1_ptr +=1  
            else: 
               
                merged.append(cur2[0])
                w2_ptr +=1
        merged.extend(word1[w1_ptr:])
        merged.extend(word2[w2_ptr:])
        return ''.join(merged)
                
                
                
            
            
        
        