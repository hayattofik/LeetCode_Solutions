class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        def helper(r,l,s):
            if l > r:
                return s
            s[l],s[r] = s[r],s[l]
            
            return helper(r-1,l+1,s)
            
        
       
        helper(len(s)-1,0,s)
    