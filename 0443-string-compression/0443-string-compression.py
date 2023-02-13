class Solution:
    def compress(self, chars: List[str]) -> int:
        count=1
        i=0
        for j in range(1,len(chars)+1):
            
            if j<len(chars) and chars[j]==chars[j-1]:
                count+=1
            else:
                chars[i]=chars[j-1]
              
                i+=1
                if count > 1:
                    for s in str(count):
                        chars[i]=s
                        i+=1
                count=1
        chars=chars[:i]
    
        return i
        