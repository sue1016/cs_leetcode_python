class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        len_ = len(nums)
        if len_ == 0:
            return -1
        return self.half_search(nums,0,len_-1,target)

    def half_search(self, nums, low, high, target):
        mid = (high + low)//2

        if low == high and nums[mid] != target:
            return -1
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return self.half_search(nums,mid+1,high,target)
        else:
            return self.half_search(nums,low,mid,target)



