class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        opera=["+","-","*","/"]
        for i in range(len(tokens)):
            if tokens[i] not in opera:
                stack.append(tokens[i])
            else:
                num1=int(stack.pop())
                num2=int(stack.pop())
                if tokens[i]=="+":
                    num=num1 + num2
                    stack.append(num)
                    
                elif tokens[i]=="-":
                    num=num2-num1
                    stack.append(num)
                elif tokens[i]=="/":
                    num=num2/num1
                    stack.append(num)
                elif tokens[i]=="*":
                    num=num1 * num2
                    stack.append(num)
        return int(stack[0])
                
