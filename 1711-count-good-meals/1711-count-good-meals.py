class Solution:
    # def check_powerof_two(self,num):
    #     if math.ceil(log2(num)) == math.floor(log2(num)):
    #         return True
    #     else:
    #         return False
    def countPairs(self, deliciousness: List[int]) -> int:
        count = 0
        for power in range(22):
            checkD=defaultdict(int)
            
            target = 2 **power
            for num in  deliciousness:
                check = target- num
                if check in checkD:
                    count += checkD[check]
                checkD[num] +=1
            
        return count % (10**9 + 7)
                    