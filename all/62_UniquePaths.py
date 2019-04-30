class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        lineNum = m
        colNum = n
        if ( n == 0) or (m == 0):
            return 0
        if m == 1 and n == 1:
            return 1
        map = [[0 for col in range(n)] for line in range(m)]


        for line in range(m):
               for col in range(n):
                    if line == 0 and col == 0:
                        map[line][col] = 1
                    elif line == 0 and col != 0:
                        map[line][col] =  map[line][col - 1]
                    elif col == 0 and line != 0:
                        map[line][col] = map[line-1][col]
                    else:
                        map[line][col] = map[line][col - 1] + map[line-1][col]


        return map[-1][-1]



