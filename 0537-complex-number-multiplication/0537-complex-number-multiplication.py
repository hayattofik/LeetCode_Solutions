class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        num1 = num1.split("+")
        
        a = int(num1[0])
        b = int(num1[1][:-1])
        num2 = num2.split("+")
        
        c = int(num2[0])
        d = int(num2[1][:-1])
        
        real = (a*c) -(b*d) 
        img = str(a*d + b*c) + "i"
        
        return str(real) + "+" + img
        