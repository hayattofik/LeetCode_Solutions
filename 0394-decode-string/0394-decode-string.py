class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        r=0
        while(r < len(s)):
               
            if s[r] != "]":
                stack.append(s[r])
            else:
                subS=""
                while(stack and stack[-1]!= "["):
                    subS=stack.pop() +subS
                stack.pop()
                
                n =""
                while(stack and stack[-1].isdigit()):
                    n= stack.pop() + n
                stack.append(int(n)* subS)
                  
            r +=1
        if len(stack) <=1 and stack[0].isdigit():
            return ""
                
        return ''.join(stack)
        
      
      