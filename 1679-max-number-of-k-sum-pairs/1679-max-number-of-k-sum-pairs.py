class Solution:
	def maxOperations(self, nums: List[int], k: int) -> int:
		count = 0
		numMap = {}

		for num in nums:
			if k - num in numMap:
				count += 1
				numMap[k - num] -= 1

				if numMap[k - num] == 0:
					numMap.pop(k-num)

				continue

			if num in numMap:
				numMap[num] += 1
			else:
				numMap[num] = 1

		return count