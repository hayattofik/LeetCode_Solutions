class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        my_coins=0
        
        for i in range(len(piles)-2,0,-2):
            my_coins+=piles[i]
            if i==len(piles)/3:
                return my_coins
            
        
        