# https://leetcode.com/problems/plus-one/
# 66. Plus One


class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        last = digits[-1]
        if last == 9:
            if len(digits) == 1:
                return [1, 0]
            return self.plusOne(digits[:-1]) + [0]
        digits[-1] += 1
        return digits


# driver code
numbers = [1, 2, 3]

solution = Solution()
result = solution.plusOne(numbers)
print(result)
