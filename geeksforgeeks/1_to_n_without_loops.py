class Solution:
    def printTillN(self, n):
        #code here
        # 	recursion method - time & space complexity O(n)
        if n == 0:
            return
        self.printTillN(n-1)
        print(n, end = " ")

        
result=Solution()
print(result.printTillN(6))