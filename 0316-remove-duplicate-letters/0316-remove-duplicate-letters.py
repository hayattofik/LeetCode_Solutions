class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        mainRef = defaultdict(int)
        
        stackRef = defaultdict(int)
        stack =[]
        
        

        for let in s:
            mainRef[let]+=1
        for let in s:
            if not stack:
                stack.append(let)
                stackRef[let]+=1
                mainRef[let]-=1
            elif stackRef[let] < 1:
                while(stack and stack[-1] >=let and mainRef[stack[-1]] > 0):
                    val = stack.pop()
                    stackRef[val] -=1
                
                stack.append(let)
                stackRef[let] +=1
                mainRef[let] -=1

                
            else:
                mainRef[let] -=1
                
        return ''.join(stack)