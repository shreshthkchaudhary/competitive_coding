class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        if len(nums)<3:
            return nums[0]
        nums.sort()
        count=0
        for i in range(1,len(nums)):
            if nums[i-1]==nums[i]:
                count+=1
                if count>=len(nums)//2:
                    return nums[i]
            else:
                count=0


result=Solution()
print(result.majorityElement([2,2,1,1,1,2,2]))