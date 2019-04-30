class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        else:
            last_num = nums[0]
            ini_len = len(nums)
            for num in nums[1:]:
                if num == last_num:
                    nums.remove(num)
                last_num = num
            return len(nums)


