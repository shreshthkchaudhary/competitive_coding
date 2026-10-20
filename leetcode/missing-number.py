class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        
        # # XOR properties you need - time complexity O(n) & space complexity O(1)
        # # x ^ x = 0: a number XORed with itself cancels out.
        # # x ^ 0 = x: XOR with 0 changes nothing.
        # # XOR is commutative and associative: order doesn’t matter.

        # missing = len(nums)
        # for i, x in enumerate(nums):
        #     missing ^= i ^ x
        # return missing




        # mathematical method - time complexity O(n) & space complexity O(1)
        n = len(nums)
        return n*(n+1)//2 - sum(nums)
        # expected = n*(n+1)//2
        # total = sum(nums)
        # return expected - total


result=Solution()
print(result.missingNumber([9,6,4,2,3,5,7,0,1]))