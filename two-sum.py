class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        dict1 = {}
        for i in range(len(nums)):
            if target - nums[i] in dict1:
                return [dict1[target - nums[i]],i]
            dict1[nums[i]]=i

        