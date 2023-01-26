class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        boats=0
        people.sort()
        light=0
        end=len(people)-1
        while(end>=light):
            wsum=people[light]+people[end]
            if wsum<=limit:
                boats+=1
                light+=1
                end-=1
            elif wsum>limit:
                boats+=1
                end-=1
        return boats
        