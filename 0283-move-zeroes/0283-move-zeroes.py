class Solution(object):
    def moveZeroes(self, nums):
        i=0
        j=0
        while(i<len(nums)):
            if (nums[i]!=0 and nums[j]==0) or (nums[i]==0 and nums[j]!=0) :
                nums[i],nums[j]=nums[j],nums[i]
                j+=1

            elif(nums[j]!=0):
                j+=1

            i+=1

        