class Solution:
    def trap(self, height: list[int]) -> int:

# prefix-suffix
        # n= len(height)
        # prefix = [0]*n
        # suffix = [0]*n
        # prefix[0] = height[0]
        # suffix[n-1] = height[n-1]
        # for i in range (1,n):
        #     prefix[i]=max(prefix[i-1],height[i])
        # for j in range (n-2,-1,-1):
        #     suffix[j]=max(suffix[j+1],height[j])
        # water=0
        # for i in range(n):
        #     if height[i]-min(prefix[i],suffix[i]) < 0:
        #         water+=(height[i]-min(prefix[i],suffix[i]))*-1

        # return water


# two-pointers
        n = len(height)
        l_max, r_max = height[0], height[n-1]
        l, r = 0, n-1
        water = 0
        while l < r:
            l_max = max(l_max, height[l])
            r_max = max(r_max, height[r])
            if l_max < r_max:
                water += l_max - height[l]
                l += 1
            else:
                water += r_max - height[r]
                r -= 1
        return water


        


result=Solution()
print(result.trap([0,1,0,2,1,0,1,3,2,1,2,1]))