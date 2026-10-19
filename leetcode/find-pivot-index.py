class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        # self - time complexity O(n) & space complexity O(1)
        total = sum(nums)
        if total - nums[0] == 0:
            return 0
        curr = 0
        for i, x in enumerate (nums):
            if (curr + x) == total- curr:
                return i
            curr += x
        return -1


        # Prefix Sum technique - time complexity O(n) & space complexity O(1)
        # total = sum(nums)
        # left = 0
        # for i, x in enumerate(nums):
        #     if left == total - left - x:
        #         return i
        #     left += x
        # return -1

result=Solution()
print(result.pivotIndex([1,7,3,6,5,6]))