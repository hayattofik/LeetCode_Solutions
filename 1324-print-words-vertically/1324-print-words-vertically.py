from collections import defaultdict
class Solution:
    def printVertically(self, s: str) -> List[str]:
            
        # split the given string
        s = s.split()
        d = defaultdict(list)
        output=[]
        # find the max length
        maximum=0
        for word in s:
            maximum = max(len(word), maximum)
        
        # for each word loop max len times
        for i in range(maximum):
            for word in s:
                if i >= len(word):
                    d[i].append(" ")
                else:
                    d[i].append(word[i])
        for col in range(maximum):
            word= ''.join(d[col])
            word = word.rstrip()
            output.append(word)
        return output
                    
                    
            
        #     store in the dictionary
        # join each string
        #     remove trailing spaces
        #     append it to the output
        # return the output
            
            
        
        
                
        