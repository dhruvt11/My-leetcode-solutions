class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        count = 0
        key = 0
        for num in nums:
            if count == 0:
                key = num
            count += (1 if num == key else -1)
        return key