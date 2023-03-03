class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        preSum =[0] * len(s)
        for lis in  shifts:
            be = lis[0]
            e= lis[1]
            sh= lis[2]
            
            
            if sh == 0:
                preSum[be] -=1
                if e < len(s)-1:
                    preSum[e+1] +=1
            elif sh ==1:
                preSum[be] +=1
                
                if e < len(s)-1 :
                    preSum[e+1] -=1
        for i in range(1,len(preSum)):
            preSum[i] += preSum[i-1]
            
        for i,num in enumerate(preSum):
            char = (ord(s[i])-97 +num)%26
            char = chr(char+97)
            preSum[i] = char
        
           
        return ''.join(preSum)
        
                
        