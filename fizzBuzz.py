# https://leetcode.com/problems/fizz-buzz/
# 412. Fizz Buzz


class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        fizzbuzz = []

        for i in range(1, n + 1):
            if i % 15 == 0:
                fizzbuzz.append("FizzBuzz")
            elif i % 3 == 0:
                fizzbuzz.append("Fizz")
            elif i % 5 == 0:
                fizzbuzz.append("Buzz")
            else:
                fizzbuzz.append(str(i))

        return fizzbuzz


# driver code
solution = Solution()
number = 23
print(solution.fizzBuzz(number))
