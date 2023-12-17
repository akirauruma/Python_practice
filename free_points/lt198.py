from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        houses = len(nums)
        if houses == 0:
            return 0
        if houses == 1:
            return nums[0]
        if houses == 2:
            return max(nums[0], nums[1])

        robbed = nums.copy()
        robbed[1] = max(nums[0], nums[1])  # pervie i vtorie doma got robbed

        for i in range(2, houses):
            robbed[i] = max(robbed[i-1], nums[i] + robbed[i-2])
        return robbed[-1]


# zadacha iz uslovia
solution = Solution()
nums = [2, 7, 9, 3, 1]
result = solution.rob(nums)
print(result)