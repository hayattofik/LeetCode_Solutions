class Solution:
    def __init__(self):
        self.order =defaultdict()
    def check_wordOrder(self,word1,word2):
        ptr=0
        while(ptr < len(word1)):
            if ptr==len(word2):
                return False
                break
            if self.order[word1[ptr]] > self.order[word2[ptr]]:
                return False
                break
            elif  self.order[word1[ptr]] < self.order[word2[ptr]]:
                return True
                break
            else:
                ptr+=1
        return True
    
    
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        for i in range(len(order)):
            self.order[order[i]] = i
        for j in range(len(words)-1):
            if self.check_wordOrder(words[j],words[j+1]):
                continue
            else:
                return False
        return True
      
            
        
                        
                    
                
            
            
            
        
    
        
        