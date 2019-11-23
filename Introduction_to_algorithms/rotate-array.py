class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 第一种解法
        # new_list = []
        # new_list.extend(nums[-k:])
        # new_list.extend(nums[0:k+1])
        # nums = new_list
        # return nums

        # 第二种解法
        # n = len(nums)
        # k %= n
        # nums[:] = nums[n-k:] + nums[:n-k]

        # 第三种解法
        # index = 0
        # num = 0
        # l = len(nums)
        # while True num < k:
        #     while index < l:
        #         nums[index] = nums[-k]
        #         index += 1

        # 第四种解法
        index = 0
        n = len(nums)
        k %= n
        while index < k:
            nums.insert(0, nums.pop())
            index += 1
