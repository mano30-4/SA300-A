class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        freq={0:0,1:0,2:0}
        for i in nums :
            freq[i]+=1
        tracker= 0
        for i in freq:
            for j in range(freq[i]):
                nums[tracker]=i
                tracker+=1
"""
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Input: nums = [2,0,1]
Output: [0,1,2]
"""