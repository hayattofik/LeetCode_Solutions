class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        f_pointer=0
        l_pointer=0
        checkLi=[]
        msum=0
        while(l_pointer<=len(s)-1):
            if (s[l_pointer] not in checkLi):
                checkLi.append(s[l_pointer])
                l_pointer+=1
                msum=max(msum,len(checkLi))
            else:
                
               
                checkLi.remove(s[f_pointer])
               
                f_pointer+=1

               
        return msum
        