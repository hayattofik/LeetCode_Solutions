class Solution(object):
    
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        output=""
        let=len(s)-1
        while(let >=0):
            if s[let]=='#':
                num=int(s[let-2:let:1])
                character= chr(num+96)
                output+=character
                let-=3
            else:
                num=int(s[let])
                character= chr(num+96)
                output+=character
                let-=1
        return output[::-1]
                
        
        