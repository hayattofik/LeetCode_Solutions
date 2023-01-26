class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        #save in dic the last ocurrence
        #if there is a letter more than the current expand paritiono
        sdic={}
        lis=[]
        for i in range(len(s)):
            if s[i] in sdic and sdic[s[i]]<i:
                sdic[s[i]]=i
            else:
                sdic[s[i]]=i


        start=0
        end=0
        lis=[]
        
        for i in range(len(s)):
           end=max(end,sdic[s[i]])
           if i==end:
               lis.append(end-start+1)
               start=end+1
        return lis
           