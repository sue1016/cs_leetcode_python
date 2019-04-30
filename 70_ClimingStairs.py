class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        rec = [0]*(n+1)

        for stair in range(n+1):
            if stair == 0:
                # init
                rec[stair] = 1
            elif stair == 1:
                # first stair
                rec[stair] = 1
            else:
                rec[stair] = rec[stair-1] + rec[stair - 2]
        return rec[-1]


