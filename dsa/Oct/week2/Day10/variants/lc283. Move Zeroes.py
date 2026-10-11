class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            if nums[i]==0:
                for j in range(i,len(nums)):
                    if nums[j]!=0 :
                        nums[i],nums[j]=nums[j],nums[i]
                        break
'''
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Input: nums = [0]
Output: [0]
'''