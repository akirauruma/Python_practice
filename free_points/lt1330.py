from typing import List


class Solution:
    def maxValueAfterReverse(self, nums: List[int]) -> int:
        originalValue = sum(abs(nums[i] - nums[i + 1]) for i in range(len(nums) - 1))
        finalValue = originalValue

        for i in range(1, len(nums) - 1):
            for j in range(i + 1, len(nums)):
                reversed_subarray = nums[:i] + list(reversed(nums[i:j + 1])) + nums[j + 1:]
                new_value = sum(abs(reversed_subarray[k] - reversed_subarray[k + 1]) for k in range(len(nums) - 1))
                finalValue = max(finalValue, new_value)

        return finalValue

