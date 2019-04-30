class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        lineNum = len(grid)
        colNum = len(grid[0])
        if lineNum == 0 or colNum == 0:
            return 0
        if lineNum == 1:
            return sum(grid[0])
        if colNum == 1:
            sum_ = 0
            for line in range(lineNum):
                sum_ = sum_ + grid[line][0]
            return sum_

        map = [[0 for col in grid[0]] for line in grid]
        map[0][0] = grid[0][0]
        for line in range(lineNum):
            for col in range(colNum):
                if line == 0 and col == 0:
                    pass
                elif line == 0 and col != 0:
                    #first line and only come from left
                    map[line][col] = map[line][col-1] + grid[line][col]
                elif line != 0 and col == 0:
                    #first col and only come from up
                    map[line][col] = map[line-1][col] + grid[line][col]
                else:
                    # may come from up or left
                    if map[line - 1][col] > map[line][col - 1]:
                        map[line][col] = map[line][col-1] + grid[line][col]
                    else:
                        map[line][col] = map[line-1][col] + grid[line][col]

        return map[lineNum-1][colNum-1]



