import copy
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.sumBefore = []
        sum_ = 0
        for num in nums:
            sum_ = sum_ + num
            self.sumBefore.append(copy.copy(sum_))

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if  i == 0:
            return self.sumBefore[j]
        else:
            return self.sumBefore[j] - self.sumBefore[i-1]




# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
