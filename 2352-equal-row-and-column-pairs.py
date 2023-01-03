class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        # object to be returned
        pairs = 0
        
        # number of rows and columns for simplicity
        rows = len(grid)
        cols = rows
        
        # find all row lines
        row_tuples = defaultdict(int)
        for row in grid:
            row_tuples[tuple(row)] += 1

        # check the column lines and look for pairs
        for col in range(cols):
            line = []
            for row in range(rows):
                line.append(grid[row][col])
            line = tuple(line)
            
            if line in row_tuples:
                pairs += row_tuples[line]

        return pairs
