class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
# Brute Force
        res = []
        n = len(nums)
        for i in range (n):
            count = 0
            for j in range (n):
                if i == j:
                    continue
                elif nums [i] > nums [j]:
                    count += 1
            res.append(count)
        return res

result=Solution()
print(result.smallerNumbersThanCurrent([8,1,2,2,3]))