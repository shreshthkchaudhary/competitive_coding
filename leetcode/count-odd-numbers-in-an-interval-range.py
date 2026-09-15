class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high+1)//2-low//2

        # if low % 2 != 0 and high % 2 != 0:
        #     return (((high - low) + 1 ) // 2) + 1
        # return ((high - low) + 1 ) // 2



result=Solution()
print(result.countOdds(1,9))