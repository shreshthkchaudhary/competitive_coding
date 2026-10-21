class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:

        # brute forces - O(m+n)
        i = j = 0
        new_nums=[]
        while i<len(nums1) and j<len(nums2):
            if nums1[i]<=nums2[j]:
                new_nums.append(nums1[i])
                i+=1
            else:
                new_nums.append(nums2[j])
                j+=1
        new_nums.extend(nums1[i:])
        new_nums.extend(nums2[j:])
        n = len(new_nums)
        if n%2:
            return float(new_nums[n//2])
        return (new_nums[n//2] + new_nums[(n//2)-1])/2



result=Solution()
print(result.findMedianSortedArrays([1,2], [3,4]))