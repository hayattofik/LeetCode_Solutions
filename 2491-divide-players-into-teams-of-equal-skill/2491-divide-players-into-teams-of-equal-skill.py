class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        l =0
        e = len(skill)-1
        num = skill[l] + skill[e]
        
        chemistry = skill[l] * skill[e]
        l +=1
        e -=1
        while(l < e):
            if skill[l] + skill[e]== num:
                chemistry += (skill[l] * skill[e])
            else:
                return -1
            l +=1
            e -=1
        return chemistry
            
            
        