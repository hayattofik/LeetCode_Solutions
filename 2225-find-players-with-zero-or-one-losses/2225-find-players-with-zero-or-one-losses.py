class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        
        los={}
        self.output = []
        self.win = []
        self.lose = []
        for i in range(len(matches)):
            # if matches [i][0] > matches[i][1]:
            winner= matches[i][0]
            loser = matches[i][1]
            
            if winner not in los:
                los[winner] = 0
            if loser  in los:
                los[loser] += 1
            else:
                los[loser] =1 
        for key in los:
            if los[key] == 0:
                self.win.append(key)
            elif los[key] == 1:
                self.lose.append(key)
        self.win.sort()
        self.lose.sort()
        self.output.append(self.win)
        self.output.append(self.lose)
        return self.output
                
        
    
            