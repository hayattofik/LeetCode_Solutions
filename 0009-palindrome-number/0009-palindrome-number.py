class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if (x < 0):
            return False
        start=0
        end=len(str(x))-1
        stri=str(x)

        while(start < len(stri)):
            if  stri[start] == stri[end]:
                start+=1
                end-=1
                continue
            
            else:
                return False
        return True

