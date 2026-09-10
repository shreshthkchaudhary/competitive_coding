class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        # for i in range(len(nums)-1):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]+nums[j]==target:
        #             return [i,j]

        # # n=len(nums)
        # # for i in range(n):
        # #     for j in range (i+1,n):
        # #         if nums[i]+nums[j]==target:
        # #             return [i,j]

        # arr=[]
        # for i in range(len(nums)-1):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]+nums[j]==target:
        #             arr.append(i)
        #             arr.append(j)
        #             break
        # return arr   

        # these all are O(n^2)



        # seen = {}
        # for i, num in enumerate(nums):
        #     partner = target - num
        #     if partner in seen:
        #         return [seen[partner], i]
        #     seen[num] = i



        # O(nlogn) this is not leetcode question solution
        # i, j = 0, len(nums)-1
        # nums.sort()
        # while i<j:
        #     if nums[i]+nums[j]==target:
        #         return [nums[i],nums[j]]
        #     elif nums[i]+nums[j]>target:
        #         j-=1
        #     elif nums[i]+nums[j]<target:
        #         i+=1
            
        # return False



        seen={}
        for i in range(len(nums)):
            needed = target - nums [i]
            if needed in seen:
                return [seen [needed], i]
            seen[nums [i]] = i
            



result=Solution()
print(result.twoSum([2,7,11,15],22))