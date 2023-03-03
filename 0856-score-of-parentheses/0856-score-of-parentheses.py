class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack =[0]
        
        for p in s:
            if p == "(":
                stack.append(0)
            else:
                check = stack.pop()
                if check ==0:
                    stack[-1]+=1
                else:
                    stack[-1] += 2 * check
        return stack.pop()
        