class Solution:
    def trap(self, height: list[int]) -> int:

# prefix-suffix
        n= len(height)
        prefix = [0]*n
        suffix = [0]*n
        prefix[0] = height[0]
        suffix[n-1] = height[n-1]
        for i in range (1,n):
            prefix[i]=max(prefix[i-1],height[i])
        for j in range (n-2,-1,-1):
            suffix[j]=max(suffix[j+1],height[j])
        water=0
        for i in range(n):
            if height[i]-min(prefix[i],suffix[i]) < 0:
                water+=(height[i]-min(prefix[i],suffix[i]))*-1

            
        return water
        


result=Solution()
print(result.trap([0,1,0,2,1,0,1,3,2,1,2,1]))