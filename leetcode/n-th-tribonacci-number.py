# This line loads lru_cache from Python’s built-in functools module so you can use it as @lru_cache.

# lru_cache vs cache:
# @lru_cache(maxsize=None) is the older way. maxsize=None means unlimited storage.
# @cache (Python 3.9+) is the same thing with no size limit, just shorter to write.

# The name lru_cache stands for “Least Recently Used cache”. If you give it a number like maxsize=128, it keeps only 128 results and throws away the least recently used when full. You don’t need that here.



# from functools import lru_cache
# from functools import cache
class Solution:
    # @lru_cache(maxsize=None)
    def tribonacci(self, n: int) -> int:

        # # recursion method - Time Limit Exceeded 32 / 38 testcases passed
        # if n < 2:
        #     return n
        # elif n == 2:
        #     return 1
        # return self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)

        # # recursion memoization method - time & space complexity O(n)
        # @lru_cache(maxsize=None)
        # # @cache
        # def t(x):
        #     if x < 2:
        #         return x
        #     elif x == 2:
        #         return 1
        #     return t(x-1) + t(x-2) + t(x-3)
        # return t(n)


        # iteration method - time complexity O(n) & space complexity O(1)
        if n == 0:
            return 0
        elif n <= 2:
            return 1
        a, b, c = 0, 1, 1
        for _ in range (n-2):
            a, b, c = b, c, a+b+c
        return c

result=Solution()
print(result.tribonacci(15000))