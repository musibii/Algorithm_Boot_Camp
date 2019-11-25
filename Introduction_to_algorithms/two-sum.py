class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # nums1 = sorted(nums)
        # for i in range(len(nums)):
        #     if nums[i]>=target:
        #         a = i
        #         global a
        #         for i in range(a-1):
        #             for j in range(i+1,a):
        #         # if nums[i] == nums[j] and i == j:
        #         #     continue
        #         # else:
        #                 if nums[i] + nums[j] == target:
        #                     return [i,j]
        #     else:
        #         for i in range(len(nums)-1):
        #             for j in range(i+1,len(nums)):
        #                 if nums[i] + nums[j] == target:
        #                     return [i,j]
        # n = len(nums)
        # for i in range(n):
        #     a = target - nums[i]
        #     if a in nums:
        #         j = nums.index(a)
        #         if i != j:
        #             return [i,j]
                
        mirror = {}
        for idx, num in enumerate(nums):
            if num in mirror:
                return [mirror[num], idx]
            mirror[target - num] = idx
                    
                    
