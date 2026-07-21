class Solution(object):
    def maxArea(self, height):
        left=0
        right=len(height)-1
        max_water=0
        while(left<right):
            width=right-left
            length=min(height[left],height[right])
            crr_water=width*length
            max_water=max(max_water,crr_water)
            if(height[left]<height[right]):
                left+=1
            else:
                right-=1
        return max_water
