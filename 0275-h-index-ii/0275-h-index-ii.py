class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            h = citations[mid]
            if h == n - mid:
                return n - mid
            elif h < n - mid:
                left = mid + 1
            else:
                right = mid - 1
        return n - left