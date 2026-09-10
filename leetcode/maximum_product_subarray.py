class Solution:
    def maxProduct(self, nums: list[int]) -> int:

        # # CLAUDE
        # curr_max = curr_min = result = nums[0]

        # for num in nums[1:]:
        #     if num < 0:
        #         curr_max, curr_min = curr_min, curr_max

        #     curr_max = max(num, curr_max * num)
        #     curr_min = min(num, curr_min * num)

        #     result = max(result, curr_max)

        # return result


        currMin = nums[0]
        currMax = nums[0]
        prodMax = nums[0]
        
        for i in range(1, len(nums)):
            prevMin = currMin
            prevMax = currMax
            
            currMin = min(nums[i], nums[i] * prevMin, nums[i] * prevMax)
            currMax = max(nums[i], nums[i] * prevMin, nums[i] * prevMax)
            
            prodMax = max(prodMax, currMax)
            
        return prodMax



result=Solution()
print(result.maxProduct([2,3,-2,4]))