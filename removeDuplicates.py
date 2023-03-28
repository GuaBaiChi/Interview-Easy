# https://leetcode.com/problems/remove-duplicates-from-sorted-array/solutions/?languageTags=python3
# 26. Remove Duplicates from Sorted Array

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i + 1


# driver code
numbers = [1, 2, 3, 4, 5, 5, 5, 5]

solution = Solution()
result = solution.removeDuplicates(numbers)
print(result)
