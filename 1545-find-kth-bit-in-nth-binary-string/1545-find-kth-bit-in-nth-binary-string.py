class Solution:
	def findKthBit(self, n: int, k: int) -> str:
		
		if(n == 1):
			return '0'
		mid = (2**n)//2 
		if(k == mid):
			return "1"
		if(k < mid):
			return self.findKthBit(n-1,k)
		else:
			
			val = self.findKthBit(n-1,(2**n) - k)
			if(val == '0'):
				return '1'
			else:
				return '0'