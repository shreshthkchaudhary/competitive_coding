class Solution:
    def myPow(self, x: float, n: int) -> float:

# Direct Method
        # return x**n

# Brute Force  TDL    
        # res=1
        # if n>0:
        #     while n!=0:
        #         res*=x
        #         n-=1
        #     return res
        # elif n<0:
        #     while n!=0:
        #         res/=x
        #         n+=1
        #     return res

        # return 1


# Mathmatical Way
        pow = n
        if pow < 0:
              pow *= -1
              x = 1/x
        ans = 1
        while pow > 0:
                if pow % 2 == 1:
                      ans *= x
                      pow -= 1
                else:
                        x *= x
                        pow /= 2
        return ans


result=Solution()
print(result.myPow(2.10000, -1))