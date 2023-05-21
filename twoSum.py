# https://leetcode.com/problems/two-sum/
# 1. Two Sum


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


# driver code
solution = Solution()
nums = [2, 7, 11, 15]
target = 9
testing = solution.twoSum(nums, target)
print(testing)


# https://www.youtube.com/watch?v=xZFoZvhnVTU
# class Solution:
#     def twoSum(self, nums: list[int], target: int) -> list[int]:
#         seen = {}

#         for i, num in enumerate(nums):
#             if target - num in seen:
#                 return [seen[target - num], i]
#             elif num not in seen:
#                 seen[num] = i

# for dictionaries, i is the index, and num is the number/value/key
# the elif stores the i/num into the dictionary

# Dictionaries are key-value pairs. In this example,
# key = The number/element value
# value = The index in the nums array

# What this is doing is enumerating each element of the nums list. If the element has not yet been seen, it is added to the seen dictionary as a key, the value being its index.

# The real trick is if target - num in seen. That means,

# "If the difference between target and num is in the seen dictionary, then we have already SEEN another element such that seen_element + num = target. That solves the problem.
# It's a pretty clever trick that works better than the nested loop
# In other words, that algorithm does this

# 0) Create a dictionary called seen
# 1) Iterate through each element in nums, call the current iteration num
# 2) If target - num in seen, then we know there are two elements within the nums list whose sum is target
# again it's pretty clever really
# The reason this works well is Dictionaries have access in O(1), unlike an array that has access in O(n)
# So instead of a potential O(n^2) brute force solution this solves the problem in O(n)
