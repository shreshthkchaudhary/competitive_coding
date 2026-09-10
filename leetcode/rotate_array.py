class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # n=len(nums)
        # for i in range(k%n):
        #     nums.insert(0,nums[n-1])
        #     nums.pop(n)
        # return nums

        n = len(nums)
        k %= n

        def reverse(left: int, right: int) -> None:
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)
        return nums



result=Solution()
print(result.rotate([1,2,3,4,5,6,7],3))