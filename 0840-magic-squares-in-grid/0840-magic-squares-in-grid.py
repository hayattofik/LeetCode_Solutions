class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def is_magic_square(i, j):
            nums_set = {k for k in range(1, 3 * 3 + 1)}
            target = 0
            
            # Traverse first row and use sum(first_row) as the target
            for num in grid[i][j:j + 3]:
                if 1 <= num <= 3 * 3:
                    nums_set.discard(num)
                    target += num
                else:
                    return 0
            
            # Traverse the other rows
            for k in range(i + 1, i + 3):
                t = 0
                for num in grid[k][j:j + 3]:
                    if 1 <= num <= 3 * 3:
                        nums_set.discard(num)
                        t += num
                    else:
                        return 0
                if t != target:
                    return 0
            
            # After traversing all rows, this set should be empty if all numbers were distinct
            if len(nums_set) != 0: return 0
            
            # Traverse the columns
            for q in range(j, j + 3):
                t = 0
                for p in range(i, i + 3):
                    t += grid[p][q]
                if t != target:
                    return 0
            
            # Traverse the top-left diagonal
            p, q = i, j
            t = 0
            while p < i + 3 and q < j + 3:
                t += grid[p][q]
                p += 1
                q += 1
            if t != target:
                return 0
            
            # Traverse the top-right diagonal
            p, q = i, j + 3
            t = 0
            while p < i + 3 and q > j:
                q -= 1
                t += grid[p][q]
                p += 1
            if t != target:
                return 0
                
            return 1
        
        # Go through all magic squares of length 3
        ans = 0
        for i in range(len(grid) - 3 + 1):
            for j in range(len(grid[0]) - 3 + 1):
                ans += is_magic_square(i, j)
        return ans
    