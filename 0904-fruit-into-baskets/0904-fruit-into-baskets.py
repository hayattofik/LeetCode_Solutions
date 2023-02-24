class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        dic = defaultdict(int)
        left,right,ans = 0,0,0
        while right < len(fruits):  
            if len(dic) == 2 and fruits[right] not in dic:
                dic[fruits[left]]-=1
                if dic[fruits[left]]==0:
                    del dic[fruits[left]]
                left+=1
            else:
                dic[fruits[right]]+=1
                right+=1
            ans = max(ans,right - left)
        return ans
        