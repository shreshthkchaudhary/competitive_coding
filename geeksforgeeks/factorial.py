class Solution:
    def factorial(self, n: int) -> int:

#  recursion-method       
        # if n <= 1:
        #     return 1
        # else:
        #     return n*(self.factorial(n-1))
            
            
# iteration-method-1
        # res, i = 1, 1
        # while i <= n:
        #     res *= i
        #     i += 1
        # return res


# iteration-method-2
        if n > 1:
            res = 1
            while n != 1:
                res *= n
                n -= 1
            return res
        return 1


result=Solution()
print(result.factorial(5))