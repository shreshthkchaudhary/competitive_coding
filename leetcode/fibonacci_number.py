class Solution:
    def fib(self, n: int) -> int:

# recursion-method
        # if n<=1:
        #     return n
        # return self.fib(n-1)+self.fib(n-2)

# dynamic-programming->bottom-up
        if n < 2:
            return n
        else:
            prev, curr= 0, 1
            for i in range (2,n+1):
                prev , curr = curr, prev + curr
            return curr
             

result=Solution()
print(result.fib(4))