class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        pdic={}
        sdic={}
        for i in range(len(p)):
            pdic[p[i]]=1+pdic.get(p[i],0)
            sdic[s[i]]=1 + sdic.get(s[i],0)
        output=[]
        if pdic==sdic:
            output.append(0)
        leftP=0
        for i in range(len(p),len(s)):
            sdic[s[i]]=1+ sdic.get(s[i],0)
            sdic[s[leftP]]-=1

            if sdic[s[leftP]]==0:
                sdic.pop(s[leftP])
            leftP+=1
            if sdic==pdic:
                output.append(leftP)
        return output

            
   
        
