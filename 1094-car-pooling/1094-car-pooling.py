class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        preL=[0]*1001
        Tsum=0
        for i in range(len(trips)):
            preL[trips[i][1]]+=trips[i][0]
            preL[trips[i][2]]-=trips[i][0]
        for i in preL:
            Tsum+=i
            if Tsum>capacity:
                return False
        return True
        