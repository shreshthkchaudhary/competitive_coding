class Solution:
    def sumOfDigits(self, n):
        
        # # to make negative integer absolute positive
        # n = abs(n)
        
        # # iterations method - time complexity O(log n) & space complexity O(1)
        # total = 0
        # while n!=0:
        #     total += n % 10
        #     n //= 10
        # return total
        
        # # recursion method - time complexity O(log n) & space complexity O(log n)
        if n == 0:
            return 0
        return n % 10 + self.sumOfDigits(n // 10)


result=Solution()
print(result.sumOfDigits(687))