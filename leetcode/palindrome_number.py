class Solution:
    def isPalindrome(self, x: int) -> bool:
        # if x<0:
        #     return False
        # y,z=0,x
        # while x!=0:
        #     y=y*10+(x%10)
        #     x=x//10
        # return y==z

        if x < 0:
            return False
        else:
            rev ,temp = 0, x
            while temp != 0:
                rev = rev * 10 + temp % 10
                temp = temp // 10
            return rev == x
            

result=Solution()
print(result.isPalindrome(121))