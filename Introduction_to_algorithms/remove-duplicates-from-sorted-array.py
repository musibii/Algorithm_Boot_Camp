class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        # 第一种解法
        # index = 0
        # while index + 1 < len(nums):
        #     if nums[index] != nums[index+1]:
        #         index += 1
        #     else:
        #         nums.remove(nums[index+1])

        # 第二种解法
        i = 0  # 慢指针
        j = 0  # 快指针
        l = len(nums)
        while i < l:
            if nums[i] == nums[j]:
                i += 1
            else:
                j += 1
                nums[j] = nums[i]
                i += 1

        return len(nums[0:j+1])
