class Solution:
    def myPow(self, x: float, n: int) -> float:
       
        if n == 0 :
            return 1
        if n == 1:
            return x
        if n == -1:
            return 1/x
        val = 1
        if n % 2 != 0:
            val = x
        
        return self.myPow(x*x,n//2) * val
        