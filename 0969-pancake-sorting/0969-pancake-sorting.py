class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        result = []
        finish = 0
        while sorted(arr) != arr:
            ToCheck = arr[0:len(arr) - finish]
            ind = arr.index(max(ToCheck))
            if ind != 0:
                result.append(ind + 1)
            result.append(len(arr) - finish)
            arr = arr[:ind + 1][::-1] + arr[ind + 1:]
            arr[:len(arr) - finish] = arr[:len(arr) - finish][::-1]
            finish += 1
        return result
        