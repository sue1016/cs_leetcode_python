class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        set_ = set()
        for num in nums:
            if num in set_:
                return True
            else:
                set_.add(num)
        return False
